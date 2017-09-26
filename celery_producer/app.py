#!/usr/bin/env python
# encoding: utf-8
from celery import Celery


app = Celery('celery_producer', include=['celery_producer.tasks'])

# 加载配置
app.config_from_object('celery_producer.config')


if __name__ == '__main__':
    app.start()
