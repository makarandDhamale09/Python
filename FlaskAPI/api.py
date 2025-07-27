from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'User (name = {self.username}, email = {self.email})'



class Users(Resource):
    def get(self):
        users = UserModel.query.all()
        return users
    
api.add_resource(Users, '/users')    

user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, help='Username of the user', required=True, help='Name cannot be blank')
user_args.add_argument('email', type=str, help='Email of the user', required=True, help='Email cannot be blank')


@app.route('/')
def home():
    return "<h1>Welcome to the API</h1><p>This is a simple Flask API.</p>"


if __name__ == '__main__':
    app.run(debug=True)