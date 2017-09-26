#!/usr/bin/env python
# encoding: utf-8
from kombu import Queue


# 使用RabbitMQ作为消息代理
BROKER_URL = 'amqp://guest:guest@localhost:5672/%2F'

# 把任务结果存在了Redis
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# 任务序列化和反序列化使用msgpack方案
CELERY_TASK_SERIALIZER = 'msgpack'

# 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON
CELERY_RESULT_SERIALIZER = 'json'

# 任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24

# 指定接受的内容类型
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']


# 定义任务队列
CELERY_QUEUES = (
    # 路由健以"task."开头的都进default队列
    Queue('default', routing_key='task.#'),
    # 路由健以"web."开头的都进web_tasks队列
    Queue('web_tasks', routing_key='web.#'),
)

# 默认交换机名字为 tasks
CELERY_DEFAULT_EXCHANGE = 'tasks'
# 默认交换类型是 topic
CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'

# 默认的路由键是task.default
CELERY_DEFAULT_ROUTING_KEY = 'task.default'

CELERY_ROUTES = {
    # app.add 的消息会进入web_tasks队列
    'celery_producer.tasks.add': {
        'queue': 'web_tasks',
        'routing_key': 'web.add'
    }
}
