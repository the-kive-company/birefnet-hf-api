from flask import Flask
from app.config import Config
import os

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Ensure instance folders exist
    for folder in [app.config['UPLOAD_FOLDER'], app.config['RESULTS_FOLDER']]:
        os.makedirs(folder, exist_ok=True)

    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)

    return app
