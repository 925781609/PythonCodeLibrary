#!/usr/bin/python
# encoding: utf-8


from __future__ import absolute_import, unicode_literals
from .celery import app


@app.task
def display(content):
    print(content)
    return True
