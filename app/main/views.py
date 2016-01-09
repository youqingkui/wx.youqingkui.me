#!/usr/bin/env python
#coding=utf-8

from datetime import datetime
from flask import render_template, session, redirect, url_for, request, current_app
import hashlib
from . import main
from .. import db

@main.route('/', methods=['GET', 'POST'])
def index():

    weixin_token = current_app.config['WEIXIN_TOKEN']
    query = request.args
    signature = query.get('signature', '')
    timestamp = query.get('timestamp', '')
    nonce = query.get('nonce', '')
    echostr = query.get('echostr', '')
    s = [weixin_token, timestamp, nonce]
    s.sort()
    print(s)
    s = ''.join(s)

    if(hashlib.sha1(s).hexdigest() == signature):
        return echostr


    return "ok"