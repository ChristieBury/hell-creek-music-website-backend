from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_heroku import Heroku

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://osxnickyzjyjpi:2a8b9ac5075c647d0ddfa9cd165610b108d6a45e66b38cde28e14512d76059ff@ec2-52-86-73-86.compute-1.amazonaws.com:5432/ddljo5kimoedja"
heroku = Heroku(app)
db = SQLAlchemy(app)

class Comic(db.Model):
    __tablename__ = 'comic-books'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200))
    author = db.Column(db.String)
    image = db.Column(db.String)

    def __init__(self, title, author, image):
        self.title = title
        self.author = author
        self.image = image

    def __repr__(self):
        return f"Title{self.title}"         

@app.route('/')
def home():
    return "<h1>Comics!</h1>"

# @app.route('/comic-books/input', methods=['POST'])
# def comics_input():
#     if request.content_type == 'application/json':
#         post_data = request.get_json()
#         title = post_data.get('title')
#         author = post_data.get('author')
#         image = post_data.get('image')
#         reg = Comic(title, author, image)
#         db.session.add(reg)
#         db.session.commit()
#         return jsonify("Data Posted")
#     return jsonify('Did not post') 

# @app.route('/comic-books', methods = ['GET'])
# def return_comics():
#     all_comics = db.session.query(Comic.id, Comic.title, Comic.author, Comic.image).all()
#     return jsonify(all_comics)

# @app.route('/comic-books/<id>', methods = ['GET'])
# def return_single_comic(id):
#     one_comic = db.session.query(Comic.id, Comic.title, Comic.author, Comic.image).filter(Comic.id == id).first()
#     return jsonify(one_comic)

# @app.route('/delete/<id>', methods = ['DELETE'])
# def comic_delete(id):
#     if request.content_type == 'application/json':
#         record = db.session.query(Comic).get(id)
#         db.session.delete(record)
#         db.session.commit()
#         return jsonify('completed Comic deletion')
#     return jsonify('deletion failed')

# @app.route('/update_comic/<id>', methods = ['PUT'])
# def comic_update(id):
#     if request.content_type == 'application/json':
#         put_data = request.get_json()
#         title = put_data.get('title')
#         author = put_data.get('author')
#         image = put_data.get('image')
#         record = db.session.query(Comic).get(id)
#         record.title = title
#         record.author = author
#         record.image = image
#         db.session.commit()
#         return jsonify('Completed Comic Page Update')
#     return jsonify('Failed Update')
    
if __name__ == '__main__':
    app.run(debug=True)

