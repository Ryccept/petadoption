from flask import Flask, request, render_template, redirect, session, jsonify, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm


app=Flask(__name__)
app.app_context().push()


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] ='idk123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():
    """Shows home page - a list of all pets."""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)


@app.route('/pets/<int:pet_id>')
def pet_page(pet_id):
    """Shows detail about the selected pet."""
    pet = Pet.query.get_or_404(pet_id)

    return render_template('pet_profile.html', pet=pet)

@app.route('/pets/add', methods=['GET', 'POST'])
def add_pet():
    """Shows pet form to add; handles adding"""
    
    form = AddPetForm()

    if form.validate_on_submit():
        name=form.name.data
        species=form.species.data
        image_url=form.photo_url.data
        age=form.age.data
        available=form.available.data
        notes=form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=image_url, age=age, notes=notes, available=available)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('pet_add.html', form=form)


@app.route('/pets/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """Shows pet form to edit; handles editing"""


    current_pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=current_pet)

    if form.validate_on_submit():
        current_pet.name=form.name.data
        current_pet.species=form.species.data
        current_pet.photo_url=form.photo_url.data
        current_pet.age=form.age.data
        current_pet.notes=form.notes.data
        current_pet.available=form.available.data
        flash(f"{current_pet.name} has been updated!")
        db.session.commit()
        return redirect(f'/pets/{pet_id}')
    else:
        return render_template('pet_edit.html', form=form, pet=current_pet)