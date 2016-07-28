from ..project.app import application
from .test_db import TestDB
from tornado.testing import AsyncHTTPTestCase


class TestHandlers(TestDB, AsyncHTTPTestCase):
    def get_app(self):
        return application

    def setUp(self):
        super().setUp()
        app = self.get_app()
        app.db = self.db
