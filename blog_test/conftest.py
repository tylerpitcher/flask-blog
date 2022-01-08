'''
This file defines what to do BEFORE & AFTER running any test cases:
'''

import os
import pytest
import time
import threading
from werkzeug.serving import make_server
from blog.__main__ import app

db_file = os.getcwd() + '/db.sqlite'


def pytest_sessionstart():
    '''
    Delete database file if existed. So testing can start fresh.
    '''
    print('Setting up environment...')
    if os.path.exists(db_file):
        os.remove(db_file)


def pytest_sessionfinish():
    '''
    Delete database file after tests.
    '''
    print('Cleaning up environment...')
    if os.path.exists(db_file):
        os.remove(db_file)


base_url = 'http://127.0.0.1:{}'.format(8081)


class ServerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        # import necessary routes
        self.srv = make_server('127.0.0.1', 8081, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        print('running')
        self.srv.serve_forever()

    def shutdown(self):
        self.srv.shutdown()


@pytest.fixture(scope="session", autouse=True)
def server():
    # create a live server for testing
    # with a temporary file as database
    server = ServerThread()
    server.start()
    time.sleep(5)
    yield
    server.shutdown()
    time.sleep(2)
