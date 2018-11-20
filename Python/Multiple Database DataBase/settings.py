database = ""


def init():
    global database
    database = ""


def set_database(db):
    global database
    database = db


def get_database():
    return database
