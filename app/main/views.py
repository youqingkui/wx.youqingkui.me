#!/usr/bin/env python
#coding=utf-8

from datetime import datetime
from flask import render_template, session, redirect, url_for, request, current_app
import hashlib
from . import main
from .. import db
from xml.etree import ElementTree

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
    ToUserName = re_xml.getiterator('ToUserName')[0].text
    FromUserName = re_xml.getiterator('FromUserName')[0].text
    CreateTime = re_xml.getiterator('CreateTime')[0].text
    MsgType = re_xml.getiterator('MsgType')[0].text
    Content = re_xml.getiterator('Content')[0].text
    MsgId = re_xml.getiterator('MsgId')[0].text

    print(ToUserName, FromUserName, CreateTime, MsgType, Content, MsgId)
    return echostr