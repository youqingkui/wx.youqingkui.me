#!/usr/bin/env python
#coding=utf-8
from flask import  redirect, render_template, url_for, flash, request
from flask.ext.login import current_user, login_user

from . import auth
from .form import LoginForm
from ..model.users import User





@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)