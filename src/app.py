from flask import Flask

from src.routers.store import store


def create_app():
    app = Flask(__name__)
    
    app.config["ENV"] = "development"
    app.config["DEBUG"] = True
    
    app.register_blueprint(store)
    
    return app
    