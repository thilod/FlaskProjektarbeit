import click
from flask import Flask
from flask.cli import with_appcontext
from flask_assets import Environment
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension

from webassets.loaders import PythonLoader as PythonAssetsLoader
from werkzeug.security import generate_password_hash

from app import assets
from app.users.models import User

assets_env = Environment()


def create_app(config=None):
    """
    Factory pattern; create new app with specified config
    :param config: configuration object
    :return: app object
    """

    # new app object
    app = Flask('flask-example')

    # configure app
    app.config.from_object(config)

    # set up database
    db = MongoEngine()
    db.init_app(app)

    # use mongo engine for session store
    app.session_interface = MongoEngineSessionInterface(db)

    # set up assets
    assets_env.init_app(app)

    # setup init command
    app.cli.add_command(init_db_command)

    # set up toolbar
    debug_toolbar = DebugToolbarExtension()
    debug_toolbar.init_app(app)

    # initialize login manager
    login_manager = LoginManager()
    login_manager.login_view = "main.login"
    login_manager.login_message_category = "warning"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.objects.get(pk=user_id)

    # import and register the different asset bundles
    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().items():
        assets_env.register(name, bundle)

    # load blueprints
    load_blueprints(app)

    return app


def load_blueprints(app):
    """
    Load all blueprints
    :param app: app in which blueprints are registered
    :return:
    """

    from app.users.views import bp_users
    from app.main.views import bp_main
    from app.books.views import bp_books
    from app.student.views import bp_student
    from app.administrator.views import bp_administrator
    from app.lecturer.views import bp_lecturer

    # register blueprints
    app.register_blueprint(bp_main)
    app.register_blueprint(bp_users, url_prefix='/users')
    app.register_blueprint(bp_books, url_prefix='/books')
    app.register_blueprint(bp_student, url_prefix='/student')
    app.register_blueprint(bp_administrator, url_prefix='/administrator')
    app.register_blueprint(bp_lecturer, url_perfix='/lecturer')


from app.models.course import Course
from app.models.lesson import Lesson
from app.models.users  import Administrator, Lecturer, Student

# new cli command to generate user
@click.command('init-db')
@with_appcontext
def init_db_command():
    admin = User(username="admin", password=generate_password_hash("test"))
    admin.save()
    click.echo('Admin user with password test created')
    
    course = Course(name="Test-Englischkurs", description="Anfängerfreundliche Einführung in die englische Sprache")
    course.save()
    admin =    Administrator(email="a.turner@examplemail.org",   firstName="Alan",            lastName="Turner",    password=generate_password_hash("test"), active=True)
    admin.save()
    student =  Student      (email="g.zeichner@examplemail.org", firstName="Gustav",          lastName="Zeichner",  password=generate_password_hash("test"), active=True)
    student.save()
    lecturer = Lecturer     (email="jw.ag@examplemail.org",      firstName="Johann Wolfgang", lastName="aus Gotha", password=generate_password_hash("test"), active=True)
    lecturer.save()

    lesson = Lesson(course=course, lecturer=lecturer, participants=[student, admin], description="Englisch 1", date="32.02.2029", maxStudents=15, canceled=False)
    lesson.save()

    click.echo('Lesson created')
