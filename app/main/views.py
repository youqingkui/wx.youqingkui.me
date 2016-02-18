#!/usr/bin/env python
#coding=utf-8

from flask import render_template, session, redirect, url_for, request, current_app
from . import main
from flask.ext.login import login_required



@main.route('/')
def index():
    return render_template('main/index.html')




