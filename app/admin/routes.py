from app import db
from app.models import User
from flask import render_template, redirect, url_for, flash

from . import admin
from .forms import ContactForm


@admin.route('/')
def index():
    user_list = User.query.all()
    return render_template('admin/index.html', users = user_list)

@admin.route('/adduser', methods=['GET', 'POST'])
def add_user():
    form = ContactForm()
    if form.validate_on_submit():
        user = User()
        form.to_model(user)
        db.session.add(user)
        db.session.commit()
        flash('The user was added successfully.')
        return redirect(url_for('admin.index'))
    
    return render_template('admin/edit_contact.html', form=form)