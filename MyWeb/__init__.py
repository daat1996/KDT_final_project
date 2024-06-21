from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
migrate=Migrate()

def create_app():
    app = Flask(__name__)
    print(f'__name__ : {__name__}')
    

    
    from .views import main_views
    
    app.register_blueprint(main_views.BP)
    
    
    return app