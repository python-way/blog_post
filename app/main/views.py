from . import main
from flask_login import login_required

@main.route('/')
def index():
    return "<h1>Hello World!</h1>"


@main.route('/protected')
@login_required
def protected():
    return "<h1>This page is only for logged in users</h1>"
