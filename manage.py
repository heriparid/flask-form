from app import create_app
from flask_script import Manager
from flask import redirect, url_for

app = create_app('default')
manager = Manager(app)

@app.route('/')
def main_index():
    return redirect(url_for('admin.index'))

if __name__ == '__main__' :
    manager.run()