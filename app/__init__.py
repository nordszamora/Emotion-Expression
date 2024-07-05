from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['TESTING'] = True

    app.config.from_object('app.config.Config')
    db.init_app(app)

    with app.app_context():
         db.create_all()
    
    migrate.init_app(app, db)

    from app.routes import blueprint
    app.register_blueprint(blueprint)

    return app
