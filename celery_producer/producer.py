#!/usr/bin/env python
# encoding: utf-8

import time
import sys
sys.path.append('../')

from celery_producer.tasks import div


if __name__ == '__main__':
    r = div.delay(4, 0)
    # 从开始调celery，到celery执行结束会有一段延迟
    # 此时r.staus为PENDING态，延时一段时间后SUCCESS
    time.sleep(2)

    print(r)
    print(r.status)
    print(r.result)
    print(r.successful())
    print(r.backend)
