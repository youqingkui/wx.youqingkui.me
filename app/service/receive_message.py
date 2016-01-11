#!/usr/bin/env python
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
from xml.etree import ElementTree
from app.model.consume_info import ConsumeInfo
from app import db

class ReMsg(object):

    @staticmethod
    def re_text(re_xml, xml_info):
        """接收解析文本消息"""

        ToUserName = re_xml.getiterator('ToUserName')[0].text
        FromUserName = re_xml.getiterator('FromUserName')[0].text
        CreateTime = re_xml.getiterator('CreateTime')[0].text
        Content = re_xml.getiterator('Content')[0].text
        MsgId = re_xml.getiterator('MsgId')[0].text
        MsgType = re_xml.getiterator('MsgType')[0].text

        content_arr = Content.split()
        if len(content_arr) >= 2 and (float(content_arr[1]) > 0):
            print(u"[Tag] :%s  [Money] :%s" %(content_arr[0].encode('utf8'), content_arr[1]))
            ci = ConsumeInfo()
            ci.money = content_arr[1]
            ci.add_time = int(time.time())
            ci.create_time = CreateTime
            ci.content_xml = xml_info
            ci.note = content_arr[2] if len(content_arr) >=3 else ''
            ci.tag_name = content_arr[0]
            db.session.add(ci)
            db.session.commit()

        print(ToUserName, FromUserName, CreateTime, MsgType, Content, MsgId)
