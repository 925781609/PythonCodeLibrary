#!/usr/bin/env python
# encoding: utf-8
from kombu import Queue


# ʹ��RabbitMQ��Ϊ��Ϣ����
BROKER_URL = 'amqp://guest:guest@localhost:5672/%2F'

# ��������������Redis
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# �������л��ͷ����л�ʹ��msgpack����
CELERY_TASK_SERIALIZER = 'msgpack'

# ��ȡ������һ������Ҫ�󲻸ߣ�����ʹ���˿ɶ��Ը��õ�JSON
CELERY_RESULT_SERIALIZER = 'json'

# �������ʱ�䣬������ֱ��д86400��Ӧ����������magic���ֱ���������
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24

# ָ�����ܵ���������
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']


# �����������
CELERY_QUEUES = (
    # ·�ɽ���"task."��ͷ�Ķ���default����
    Queue('default', routing_key='task.#'),
    # ·�ɽ���"web."��ͷ�Ķ���web_tasks����
    Queue('web_tasks', routing_key='web.#'),
)

# Ĭ�Ͻ���������Ϊ tasks
CELERY_DEFAULT_EXCHANGE = 'tasks'
# Ĭ�Ͻ��������� topic
CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'

# Ĭ�ϵ�·�ɼ���task.default
CELERY_DEFAULT_ROUTING_KEY = 'task.default'

CELERY_ROUTES = {
    # app.add ����Ϣ�����web_tasks����
    'celery_producer.tasks.add': {
        'queue': 'web_tasks',
        'routing_key': 'web.add'
    }
}
