#! ../env/bin/python
# -*- coding: utf-8 -*-

from app.books.model import Book


class TestURLs:
    def test_bookhome(self, testapp):
        """ Tests if the index page loads when not logged in"""

        rv = testapp.get('/books')
        assert rv.status_code == 308

    def test_bookhome_logged_in(self, testapp):
        """ Tests if the book page returns a 200
                if the user is logged in
        """

        rv = testapp.post('/login', data=dict(
            username='admin',
            password="test"
        ), follow_redirects=True)

        rv = testapp.get('/books/')
        assert 200 == rv.status_code

    def test_insert_book(self, testapp, test_entry):
        """ Tests if books are inserted """

        # login
        rv = testapp.post('/login', data=dict(
            username='admin',
            password="test"
        ), follow_redirects=True)

        # add book
        rv = testapp.post('/books/add', data=dict(
            title=test_entry['title'],
            author=test_entry['author'],
            year=test_entry['year']
        ), follow_redirects=True)
        assert 200 == rv.status_code

        # check if book is inserted

        # get first book
        result = Book.objects().first()

        # check existence
        assert result is not None

        # check properties
        assert result['author'] == test_entry['author']
        assert result['title'] == test_entry['title']
        assert result['year'] == test_entry['year']
