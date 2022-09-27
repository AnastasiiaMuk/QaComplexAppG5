import random


def random4digits():
    """Generate random 4 digits"""
    return str(random.randrange(1000, 9999, 1))


def random_username():
    """Generate random username"""
    return 'user' + random4digits()


def random_email():
    """Generate random email"""
    return random4digits() + '@gmail.com'


def random_password():
    """Generate random password"""
    return 'user' + random4digits() + random4digits()
