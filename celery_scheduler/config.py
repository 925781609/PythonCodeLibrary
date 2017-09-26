#!/usr/bin/python
# encoding: utf-8
import os
from datetime import timedelta
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CELERY_ENABLE_UTC = False  # ������UTC
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24  # ��������ʱЧʱ��
CELERYD_LOG_FILE = BASE_DIR + "/celery.log"  # log·��
CELERYBEAT_LOG_FILE = BASE_DIR + "/beat.log"   # beat log·��
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']  # ������ܵĸ�ʽ һ�����msgpack(��)��json(��ƽ̨)
CELERY_RESULT_SERIALIZER = 'json'  # ��ȡ��������ʽ
CELERY_TASK_SERIALIZER = 'msgpack'  # �������л������л�����msgpack


CONTENT = 'test'

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'celery_scheduler.tasks.display',  # ����
        'schedule': timedelta(seconds=5),  # ʱ��
        'args': ([CONTENT],)  # ������������list/tuple
    },
}
