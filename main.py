from flask import Flask, render_template
from database import *

app = Flask(__name__)


@app.route('/')
def home_page():
    cars = get_cars()
    blogs = get_blogs()
    return render_template('index.html', cars=cars, blogs=blogs)


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/blog')
def blog_page():
    blogs = get_blogs()
    return render_template('blog.html', blogs=blogs)


@app.route('/car')
def car_page():
    cars = get_cars()
    return render_template('car.html', cars=cars)


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
