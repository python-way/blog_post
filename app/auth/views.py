from . import auth
from flask import render_template, request, flash, url_for, redirect
from ..models import User
from flask_login import login_user
from .forms import LoginForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Invalid username or password.')

    return render_template('auth/login.html', form=form)


@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"

@auth.route('/register')
def register():
    return "<h1>Register</h1>"
