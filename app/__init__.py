from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize components
    bootstrap.init_app(app)
    db.init_app(app)
    
    # Register bluprints
    from app.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)
    
    return app
