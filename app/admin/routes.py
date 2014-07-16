from . import admin
from flask import render_template

@admin.route('/')
def index():
    return render_template('admin/index.html')

@admin.route('/adduser')
def add_user():
    return 'hello add'