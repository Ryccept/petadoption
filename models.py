from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


default_img = 'https://media.istockphoto.com/id/931785704/vector/paw_print.jpg?s=612x612&w=0&k=20&c=CXBPHlf7XHdJiiOULJrI9nGZjVNAj7cqnkM_eDyDdCU='

#Models:

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(), nullable=False, unique=True)

    species = db.Column(db.String(), nullable=False)

    photo_url = db.Column(db.String(), nullable=True, default=default_img)

    age = db.Column(db.Integer, nullable=True)

    notes = db.Column(db.String(), nullable=True)

    available = db.Column(db.Boolean, nullable=False, default=True)
