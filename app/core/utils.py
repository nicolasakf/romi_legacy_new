from flask_httpauth import HTTPBasicAuth
from app import db_lib as db

auth = HTTPBasicAuth()

USER = 'romi'
PWD = 'romi'


@auth.verify_password
def verify_password(username, password):
    user_list = db.get_user_list()
    try:
        pwd = user_list[username]
        if pwd != password:
            return False
        else:
            global USER_ID
            USER_ID = db.get_user_id(username)
            return True
    except KeyError:
        return False


def auth_user(user, passwd):
    out = False
    if(user == USER) and (passwd == PWD):
        out = True

    return out