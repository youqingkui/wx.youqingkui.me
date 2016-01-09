#!/usr/bin/env python
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from xml.etree import ElementTree

class ReMsg(object):

    @staticmethod
    def re_text(re_xml):
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

        print(ToUserName, FromUserName, CreateTime, MsgType, Content, MsgId)
