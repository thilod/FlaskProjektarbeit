#!/usr/bin/env python

import os, sys

from werkzeug.security import generate_password_hash
from flask_script import Manager
from flask_script.commands import ShowUrls, Clean, Command, prompt_bool
from app.factory import create_app, assets_env
from app.users.models import User


# new command:
# create first user
class InitDatabase(Command):
    def __index__(self):
        super(InitDatabase, self).__init__()

    def run(self):
        verified = prompt_bool('Do you really want to create a new user')
        if verified:
            admin = User(username="admin", password=generate_password_hash("test"))
            admin.save()
            sys.stdout.write('Admin user with password test created')


# default to dev config because no one should use this in
# production anyway
env = os.environ.get('APPNAME_ENV', 'dev')
app = create_app('app.config.%sConfig' % env.capitalize())

manager = Manager(app)

manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())
manager.add_command("init-db", InitDatabase())

from flask_assets import ManageAssets
manager.add_command("assets", ManageAssets(assets_env))

@manager.shell
def make_shell_context():

    return dict(app=app)


if __name__ == "__main__":
    manager.run()
