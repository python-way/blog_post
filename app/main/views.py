from . import main
from flask_login import login_required
from ..decorators import admin_required, permission_required
from ..models import Permission

@main.route('/')
def index():
    return "<h1>Hello World!</h1>"

@main.route('/protected')
@login_required
def protected():
    return "<h1>This page is only for logged in users</h1>"

@main.route('/admin')
@login_required
@admin_required
def for_admins_only():
    return "For administrators!"

@main.route('/moderate')
@login_required
@permission_required(Permission.MODERATE)
def for_moderators_only():
    return "For comment moderators!"
