#!/usr/bin/env python
# encoding: utf-8

from __future__ import absolute_import
from celery.utils.log import get_task_logger

from celery_producer.app import app


logger = get_task_logger(__name__)


# bind=True，将div变为绑定的方法，第一个参数传self，通过self可以获得任务的上下文
@app.task(bind=True)
def div(self, x, y):
    logger.info('Executing task id {0.id}, args:{0.args!r} kwargs:{0.kwargs!r}'
                .format(self.request))
    try:
        result = x / y
    except ZeroDivisionError as e:
        raise self.retry(exc=e, countdown=5, max_retries=3)
    return result
