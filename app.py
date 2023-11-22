from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Define the path to the database file within the Flask app directory
db_path = os.path.join(app.root_path, 'todo.db')

# Configure SQLAlchemy to use SQLite and set the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno}- {self.title}"

@app.route('/', methods =['GET','POST'])
def firstapp():
    if request.method =="POST":
        title  = request.form['title']
        desc  = request.form['desc']
        todo  = Todo(title  =title, desc = desc)
        db.session.add(todo)
        db.session.commit()
    alltodo =Todo.query.all()
    return render_template("index.html",alltodo=alltodo)
    

@app.route('/product')
def machine_learning():
   return render_template("product.html")


if __name__ == "__main__":
    # Function to create the database tables
    def create_database():
        with app.app_context():
            db.create_all()

    create_database()  # Call function to create database tables

    # Run the Flask app in debug mode
    app.run(debug=True)
