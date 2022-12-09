"""Seed file to make sample data for DB."""
from models import db, Pet, connect_db
from app import app

#Create all tables:
db.drop_all()
db.create_all()

#the data:
olive = Pet(name='Olive', species='lizard', age=1)
ticket = Pet(name='Ticket', species='dog', age=1, photo_url='https://images.unsplash.com/photo-1543466835-00a7907e9de1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1074&q=80')
moose = Pet(name='Moose', species='rat', age=1, photo_url='https://images.unsplash.com/photo-1584553421349-3557471bed79?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2046&q=80')
oreo = Pet(name='Oreo', species='cat', age=5, photo_url='https://images.unsplash.com/photo-1562009910-830d74050500?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1962&q=80')


db.session.add_all([olive, ticket, moose, oreo])

db.session.commit()