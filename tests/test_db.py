import subprocess
import momoko

from tornado.testing import AsyncTestCase


NAME_TEST_DB = 'testdb'
good_dsn = 'dbname=%s user=%s password=%s host=%s port=%s' % (
    NAME_TEST_DB, 'vagrant', 'dbpass', '127.0.0.1', '5432'
)


class TestDB(AsyncTestCase):
    good_dsn = 'dbname=%s user=%s password=%s host=%s port=%s' % (
        NAME_TEST_DB, 'vagrant', 'dbpass', '127.0.0.1', '5432'
    )

    @classmethod
    def tearDownClass(cls):
        process = subprocess.Popen(["sudo", "-u", "postgres", "dropdb", "testdb"], stdout=subprocess.PIPE)
        process.communicate()

    @classmethod
    def setUpClass(cls):
        process = subprocess.Popen(["sudo", "-u", "postgres", "createdb", "testdb", "-O", "vagrant"],
                                   stdout=subprocess.PIPE)
        process.communicate()
        process = subprocess.Popen(["yoyo", "-c", "tests/yoyo.ini", "apply"], stdout=subprocess.PIPE)
        process.communicate()

    def setUp(self):
        super().setUp()
        self.db = momoko.Pool(self.good_dsn, ioloop=self.io_loop, max_size=1, auto_shrink=0)
        f = self.db.connect()
        self.io_loop.add_future(f, lambda x: None)

    def tearDown(self):
        super().tearDown()
        self.db.close()
        self.io_loop.stop()
