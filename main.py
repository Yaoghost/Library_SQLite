from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random
#-------------DATABASE----------------
db = SQLAlchemy()    # creating a 'database' basically
app = Flask(__name__)  # creating the app
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"  # naming the database
# initialize the app with the extension
db.init_app(app)
# creating table called book
class Book(db.Model):
    __tablename__ = 'books'  # Specify the table name

    id = db.Column(db.Integer, primary_key=True)    # necessary to have id when it comes to table
    title = db.Column(db.String(300), nullable=False)
    author = db.Column(db.String(300), nullable=False)
    rating = db.Column(db.Float, nullable=False)
with app.app_context():
    db.create_all()

all_books = []

@app.route('/')
def home():
    with app.app_context():
        all_books = db.session.query(Book).all()
    return render_template('homepage.html', all_books=all_books)

@app.route('/change', methods=['GET', 'POST'])
def change_rating():
    book_id = request.args.get('id')
    book = Book.query.get(book_id)

    if request.method == 'POST':
        new_rating = float(request.form['new_rating'])
        book.rating = new_rating
        db.session.commit()

    return redirect(url_for('home'))

@app.route('/delete')
def delete_book():
    book_id = request.args.get('id')
    book = Book.query.get(book_id)

    if book:
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return "Book not found", 404



@app.route("/add")
def add():
    return render_template('add.html')

@app.route('/edit')
def edit_rating():
    title = request.args.get('name')
    author = request.args.get('author')
    rating = request.args.get('rating')
    id = request.args.get('id')
    return render_template('edit_rating.html', title=title, author=author, rating=rating, id=id)

@app.route("/process_form", methods=['POST'])
def process_form():
    name = request.form['Book Name']
    author = request.form['Book Author']
    rating = request.form['Rating']
    new_book = {"name": name, "author": author, "rating": rating }
    with app.app_context():
        new_book = Book(title=name, author=author, rating=rating, id=random.randint(1,100000))
        db.session.add(new_book)
        db.session.commit()
    # all_books.append(new_book)
        # get data from database and fetch it basically return all objects of class Book
        all_books = db.session.query(Book).all()

    return render_template('homepage.html', all_books=all_books)



if __name__ == "__main__":
    app.run(debug=True)

