'''
This file defines what to do BEFORE & AFTER running any test cases:
'''

import os

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
    # print('Cleaning up environment...')
    # if os.path.exists(db_file):
    #     os.remove(db_file)
