# backend/src/app.py
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(debug=True)