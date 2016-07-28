import copy
import json

from tornado import web
from raven.contrib.tornado import SentryMixin

from ..utils.answers import STANDART_ANSWER
from ..utils.tools import json_serial


class BaseHandler(SentryMixin, web.RequestHandler):
    sclient = None

    @property
    def db(self):
        return self.application.db

    @property
    def answer(self):
        return copy.deepcopy(STANDART_ANSWER)

    def response(self, result='done', error=None):
        self.set_header('Content-Type', 'application/json')
        answer = self.answer
        answer['result'] = result
        answer['error'] = error
        self.write(
            json.dumps(answer, default=json_serial)
        )
        self.finish()


class PingHandler(BaseHandler):
    def get(self):
        self.response('pong')
