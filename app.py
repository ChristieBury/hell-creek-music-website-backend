from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_heroku import Heroku

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://trefuhsszkbjrb:1e26aecec9858eb826dd29539d37ebd4ac7e73d730a59dcdd203b8cb58fadc05@ec2-54-147-209-121.compute-1.amazonaws.com:5432/d2ivsn4dmrek33"
heroku = Heroku(app)
db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'comic-books'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200))
    author = db.Column(db.String)

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return '<Title%r>' % self.title         

@app.route('/')
def home():
    return "<h1>Comics!</h1>"


if __name__ == '__main__':
    app.run(debug=True)

