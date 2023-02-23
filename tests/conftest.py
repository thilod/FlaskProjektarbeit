import pytest

from app.factory import create_app


@pytest.fixture()
def testapp(request):
    app = create_app('app.config.TestingConfig')
    client = app.test_client()

    return client
