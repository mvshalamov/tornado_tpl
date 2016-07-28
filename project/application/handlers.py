import json
import datetime

from ..base.base_handlers import BaseHandler
from ..application.models import Draft


class ImportDraftsListHandler(BaseHandler):

    async def get(self):
        res = await Draft.all(self.db, 'test')
        self.response(result=res)
