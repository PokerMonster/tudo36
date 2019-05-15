import hashlib

from models.auth import User
from models.db import Session


def hashed(text):
    return hashlib.md5(text.encode('utf8')).hexdigest()


def authenticate(username, password):
    # session = Session()
    # user = session.query(User).filter_by(name=username).first()

    return User.get_password(username) == hashed(password)


def register(username, password):
    s = Session()
    s.add(User(name=username, password=hashed(password)))
    s.commit()