import os


def get_uid():
    return os.environ['HOSTNAME']
