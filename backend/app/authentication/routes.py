from app import app, db
from app.utils import *
from app.authentication.models import User
from app.authentication.routes import get_overview
from config import Config

from flask import request

def get_idx():
    return len(
        User
        .query
        .all()
    )

def add_user_to_db(username, email, password):
    user_idx = get_idx()
    new_user = User (
        username = username,
        email = email,
        password = password
        )
    new_user.set_password(password)
    new_user.create_new_account(
        user_idx,
        signup_bonus = Config.SIGNUP_BONUS
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

@app.route('/register', methods = ["GET", "POST"])
def register():
    message = request.get_json()
    email, username, password = message.values()['loginDetails']
    user_exists = db_query(User, 'username', username)[0]
    email_exists = db_query(User, 'email', email)[0]
    if user_exists:
        return gen_result_dictionary(
            success = False,
            message = "Username already taken. Please Try another username."
        )
    if email_exists:
        return gen_result_dictionary(
            success = False,
            message = "E-mail address already taken. Please Try another E-Mail address."
        )
    else:
        new_user = add_user_to_db(
            username, email, password
        )
    return gen_result_dictionary(
        success = True,
        message = "Account registered. Welcome {}".format(username), 
        result = get_overview(new_user)
    )