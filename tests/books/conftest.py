import pytest

from app.factory import create_app
from app.books.model import Book


@pytest.fixture()
def testapp():
    app = create_app('app.config.TestingConfig')
    client = app.test_client()

    # clear data base
    Book.objects().delete()

    return client


@pytest.fixture()
def test_entry():
    """
    create test entry
    """
    return Book(title="Testbook", author='Testauthor', year=2021)
