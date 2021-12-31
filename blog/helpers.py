'''
Defines helper functions that helps model.py.
'''

import re


def in_database(model, obj):
    '''
    Checks to see if obj is in model's table.
    Returns true if obj is in model's table.
    '''
    return model.query.filter_by(id=obj.id).first() is obj


def is_username(string):
    '''
    Checks to see if a string meets the requirements of a username.
    Returns true if requirements are met.
    '''
    if len(string) > 32:
        return False
    regex = r'^[A-z]+[A-z0-9]{4,}$'
    return re.match(regex, string)


def is_email(string):
    '''
    Checks to see if a string meets the email requirements of RFC5322.
    Returns true if requirements are met.
    '''
    if len(string) > 320:
        return False
    regex = (r'([!#-\'*+/-9=?A-Z^-~-]+(\.[!#-\'*+/-9=?A-Z^-~-]+)*|\'"([]!#-[^-'
             r'~\t]|(\\[\t -~]))+")@([!#-\'*+/-9=?A-Z^-~-]+(\.[!#-\'*+/-9=?'
             r'A-Z^-~-]+)*|\[[\t -Z^-~]*])')

    return bool(re.match(regex, string))


def is_password(string):
    '''
    Checks to see if a string is >= 5 & <= 128, contains letters,
    contains numbers, and has at least 1 special character.
    Returns true if requirements are met.
    '''
    regex = r'[\s!\"#\$%&\'\(\)\*\+,-\./:;<=>\?@\[\]\^_`\{\|\}~]'
    if len(string) < 5 or len(string) > 128:
        return False
    if not bool(re.search(r'[A-z]', string)):
        return False
    if not bool(re.search(r'[0-9]', string)):
        return False
    return bool(re.search(regex, string))
