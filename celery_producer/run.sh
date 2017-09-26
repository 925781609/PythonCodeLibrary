#!/bin/bash

#pip install "celery[librabbitmq, redis, msgpack]"

cd ..
# 启动worker，等着被调用
celery -A celery_producer.app worker -Q web_tasks -l info --logfile=celery_producer/celery2.log & 
sleep 30s
cd -

# 将任务发给worker 去执行
python producer.py



