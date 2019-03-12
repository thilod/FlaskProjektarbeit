from flask import Flask
from flask_assets import Environment
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension

from webassets.loaders import PythonLoader as PythonAssetsLoader

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
    db.init_app(app);

    #use mongo engine for session store
    app.session_interface = MongoEngineSessionInterface(db)

    # set up assets
    assets_env.init_app(app)

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

    from .users.views import users
    from .main.views import main
    from .books.views import books

    # register blueprints
    app.register_blueprint(main)
    app.register_blueprint(users, url_prefix='/users')
    app.register_blueprint(books, url_prefix='/books')

