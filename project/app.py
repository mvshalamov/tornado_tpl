import os

from raven.contrib.tornado import AsyncSentryClient

from tornado.httpserver import HTTPServer
from tornado.options import parse_command_line
from tornado import web
from tornado.ioloop import IOLoop
from urllib.parse import urlparse
IOLoop.configure('tornado.platform.asyncio.AsyncIOLoop')


import momoko

from .application import handlers as send_handlers
from .base.base_handlers import PingHandler


ioloop = IOLoop.instance()


application = web.Application([
    (r'/drafts/', send_handlers.ImportDraftsListHandler),
    (r'/ping/', PingHandler),
], debug=True)


port = int(os.environ.get('PORT', 8000))
defaultdburl = 'postgres://vagrant:dbpass@localhost:5432/project_prj_db'
dburl = urlparse(os.environ.get("DATABASE_URL", defaultdburl))

if __name__ == '__main__':
    parse_command_line()
    # application.sentry_client = AsyncSentryClient(
    # )
    application.db = momoko.Pool(
        # connection_factory=psycopg2.extras.LoggingConnection,
        dsn='dbname=%(database)s user=%(user)s password=%(password)s host=%(host)s port=%(port)i' % dict(
            database=dburl.path[1:],
            user=dburl.username,
            password=dburl.password,
            host=dburl.hostname,
            port=int(dburl.port)),
        size=1,
        max_size=5,
        ioloop=ioloop,
    )

    future = application.db.connect()
    ioloop.add_future(future, lambda f: ioloop.stop())
    ioloop.start()
    future.result()

    http_server = HTTPServer(application)
    http_server.listen(port, '0.0.0.0')
    ioloop.start()
