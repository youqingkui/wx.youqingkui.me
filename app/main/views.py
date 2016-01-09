#!/usr/bin/env python
#coding=utf-8

from datetime import datetime
from flask import render_template, session, redirect, url_for, request, current_app
import hashlib
from . import main
from .. import db
from xml.etree import ElementTree

from app.service.receive_message import ReMsg

@main.before_app_request
def check_token():

    weixin_token = current_app.config['WEIXIN_TOKEN']
    query = request.args
    signature = query.get('signature', '')
    timestamp = query.get('timestamp', '')
    nonce = query.get('nonce', '')
    echostr = query.get('echostr', '')
    s = [weixin_token, timestamp, nonce]
    s.sort()
    s = ''.join(s)

    if not (hashlib.sha1(s).hexdigest() == signature):
        print(s)
        return "Error"



@main.route('/', methods=['GET', 'POST'])
def index():

    print(request.data)
    query = request.args
    echostr = query.get('echostr', '')
    re_xml = ElementTree.fromstring(request.data)
    MsgType = re_xml.getiterator('MsgType')[0].text
    if MsgType == 'text':
        ReMsg.re_text(re_xml)



    return echostr