import os

from flask import Flask

# Import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy as _BaseSQLAlchemy

class SQLAlchemy(_BaseSQLAlchemy):
    def apply_pool_defaults(self, app, options):
        super(SQLAlchemy, self).apply_pool_defaults(app, options)
        options["pool_pre_ping"] = True

# def create_app(test_config=None):
# create and configure the app
app = Flask(__name__, instance_relative_config=True)

from flask_cors import CORS
CORS(app)

app.config.from_object('config')

# print(app.config['SQLALCHEMY_DATABASE_URI'])


# ********************************************************************
# configuring db engine
from sqlalchemy import create_engine
from config import SQLALCHEMY_DATABASE_URI as db_config
engine  = create_engine(db_config)
# ********************************************************************


db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

# Import a module / component using its blueprint handler variable (mod_auth)
from .mod_data.controllers import mod_data as input_data_module
app.register_blueprint(input_data_module)


db.create_all()
