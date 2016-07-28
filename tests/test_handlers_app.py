from .test_handlers import TestHandlers


class TestPingHandlers(TestHandlers):

    def test_ping(self):
        response = self.fetch('/ping/')
        self.assertEqual(response.code, 200)


class TestDraftHandlers(TestHandlers):

    def test_drafts_get(self):
        response = self.fetch('/drafts/')
        self.assertEqual(response.code, 200)
