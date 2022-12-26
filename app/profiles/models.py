from flask_login import UserMixin

from app import db, login_manager

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __init__(self, user, email):
        self.user = user
        self.email = email
    
    def __repr__(self):
        return f'<user {self.id}>'


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    birthdate = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    image = db.Column(db.String)

    def __init__(self, firstname, lastname, birthdate, user_id, img):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.user_id = user_id
        self.img = img

    def __repr__(self):
        return f'<profile {self.id}>'

@login_manager.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()
