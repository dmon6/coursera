#!/usr/bin/env python3.7

import re


def validate_user(username, minlen):
    """ Checks if the received username matches the required conditions"""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise TypeError("minlen must be at least 1")

    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username):
        return False
    if username[0].isalpha():
        return True
    return False


print(validate_user("blue.kale", 3))  # True
print(validate_user(".blue.kale", 3))  # Currently True, should be False
print(validate_user("red_quinoa", 4))  # True
print(validate_user("_red_quinoa", 4))  # Currently True, should be False
