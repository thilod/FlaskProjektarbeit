import os

from app.factory import create_app

# default to dev config because no one should use this in
# production anyway
env = os.environ.get('FLASK_ENV', 'testing')

# create app with factory method
app = create_app('app.config.%sConfig' % env.capitalize())
