#!/usr/bin/python
# encoding: utf-8
import os
from datetime import timedelta
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CELERY_ENABLE_UTC = False  # 不是用UTC
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24  # 任务结果的时效时间
CELERYD_LOG_FILE = BASE_DIR + "/celery.log"  # log路径
CELERYBEAT_LOG_FILE = BASE_DIR + "/beat.log"   # beat log路径
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']  # 允许接受的格式 一般采用msgpack(快)和json(跨平台)
CELERY_RESULT_SERIALIZER = 'json'  # 读取任务结果格式
CELERY_TASK_SERIALIZER = 'msgpack'  # 任务序列化反序列化采用msgpack


CONTENT = 'test'

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'celery_scheduler.tasks.display',  # 任务
        'schedule': timedelta(seconds=5),  # 时间
        'args': ([CONTENT],)  # 参数，必须是list/tuple
    },
}
