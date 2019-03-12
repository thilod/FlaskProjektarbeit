#! ../env/bin/python
# -*- coding: utf-8 -*-

import pytest

@pytest.mark.usefixtures("testapp")
class TestURLs:
    def test_bookhome(self, testapp):
        """ Tests if the index page loads when not logged in"""

        rv = testapp.get('/books')
        assert rv.status_code == 301

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