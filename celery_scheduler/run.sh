#!/bin/bash

#pip install "celery[librabbitmq, redis, msgpack]"

cd ..
#启动任务调度器(celery beat)
celery beat -A celery_scheduler &
sleep 10s

#启动celery worker
celery -A celery_scheduler worker -l info
