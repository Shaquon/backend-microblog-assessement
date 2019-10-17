from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello World. I'm a program made by Shaquon Kelley"