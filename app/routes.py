from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Shaquon'}
    posts = [
        {
            'author': {'username': 'Barbara'},
            'body': 'Beautiful day in Compton!'
        },
        {
            'author': {'username': 'Kelley'},
            'body': 'That Pulp Fiction movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)