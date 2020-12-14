from api import API
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from json_encoder import JSONEncoderWithDateLikeSupport

db = SQLAlchemy()


def init_app():
    from config import get_config_by_current_environment

    app = Flask(__name__, instance_relative_config=False)
    app.json_encoder = JSONEncoderWithDateLikeSupport
    CORS(app)
    api = API(app)
    app.config.from_object(get_config_by_current_environment())

    db.init_app(app)

    with app.app_context():
        from resources.product import ProductResource

        api.add_resource(ProductResource, "/product")

        return app
