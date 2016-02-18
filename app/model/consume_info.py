#!/usr/bin/env python
#coding=utf-8

from app import db

class ConsumeInfo(db.Model):
    __tablename__ = 'consume_info'

    id = db.Column(db.Integer, primary_key=True)
    money = db.Column(db.Float, default=0.00)
    tag_name = db.Column(db.String(12), default='')
    note = db.Column(db.String(255), default='')
    add_time = db.Column(db.Integer, default=0, index=True)
    user_open_id = db.Column(db.String(255), default='')
    create_time = db.Column(db.Integer, default=0, index=True)
    content_xml = db.Column(db.Text, default=None)

    def __str__(self):
        return "ConsumeInfo => { \
id:%d, money:%0.2f, tag_name:'%s', note:'%s', add_time:%d,  \
user_open_id:'%s', create_time:%d, content_xml:'%s'}" % (
self.id, self.money, self.tag_name, self.note, self.add_time,
self.user_open_id, self.create_time, self.content_xml)

    __repr__ = __str__
