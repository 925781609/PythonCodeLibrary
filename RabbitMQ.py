#!/usr/bin/env python
# encoding: utf-8


import pika


class RabbitMQ(object):

    def __init__(self, url, exchange, exchange_type, passive, durable, auto_delete):
        '''RabbitMQ初始化函数:
            1. RabbitMQ相关：
                url: amqp://user:password@localhost:5672/vhost
            2. 交换机配置相关：
                exchange: 交换机名字
                exchange_type: 交换机类型，可选项为direct/topic/fanout/headers
                passive: 如果设为True，同名交换机已经存, 再声明的话会返回声明成功，
                        如果为False, 同名交换机已经存在，再声明会报错
                durable: 为True表示RabbitMQ在崩溃或重启之后，会重新建立队列或交换机
                auto_delete: 当所有的Q都不再使用交换机的时候，删除交换机
        '''
        parameters = pika.URLParameters(url)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange, exchange_type, passive, durable, auto_delete)
        self.exchange = exchange
        self.auto_delete = auto_delete

    def publish(self, content_type, deliver_mode, confirm_delivery, routing_key, msg):
        '''RabbitMQ发布消息函数：
            content_type: 消息内容的类型，可以是text/plain或者application/json
            deliver_mode: 2表示让消息持久化，重启RabbitMQ之后也不会丢失
            confirm_delivery: 是否支持消息确认
            routing_key: direct模式下，根据routing_key, 将消息传给对应的Q
            msg: 要传递的msg
        '''
        properties = pika.BasicProperties(content_type=content_type, delivery_mode=deliver_mode)

        if confirm_delivery:
            self.channel.confirm_delivery()
            deliveried = self.channel.basic_publish(self.exchange, routing_key, msg, properties=properties)
            if deliveried:
                print('Message published was confirmed')
            else:
                print('Message published could not be confirmed')
        else:
            self.channel.basic_publish(self.exchange, routing_key, msg, properties=properties)

        self.connection.close()

    def consume(self, queue, routing_key, callback):
        '''RabbitMQ消费消息函数：
            queue：队列名
            routing_key: 要与发布者的routing_key一致
            callback：收到消息的回调函数, 例如：
                    def callback(channel, method, properties, body):
                        channel.basic_ack(delivery_tag=method.delivery_tag)
                        print(body)
        '''
        self.channel.queue_declare(queue, self.auto_delete)
        self.channel.queue_bind(queue, self.exchange, routing_key)
        self.channel.basic_consume(callback, queue)

        try:
            self.channel.start_consuming()
        except KeyboardInterrupt:
            self.channel.stop_consuming()

        self.connection.close()


if __name__ == '__main__':
    import multiprocessing
    import time

    def callback(channel, method, properties, body):
        channel.basic_ack(delivery_tag=method.delivery_tag)
        print(body)
    url = 'amqp://guest:guest@localhost:5672/%2F'
    exchange = 'tmp_exchange'
    exchange_type = 'direct'
    passive = False
    durable = True
    auto_delete = False
    queue = 'tmp_queue'
    routing_key = 'tmp_routing_key'
    delivery_mode = 2
    content_type = 'text/plain'
    confirm_delivery = True
    msg = 'Hello world!'

    rabbit_mq_1 = RabbitMQ(url, exchange, exchange_type, passive, durable, auto_delete)
    rabbit_mq_2 = RabbitMQ(url, exchange, exchange_type, passive, durable, auto_delete)

    p1 = multiprocessing.Process(target=rabbit_mq_1.consume, args=(queue, routing_key, callback))
    p2 = multiprocessing.Process(target=rabbit_mq_2.publish, args=(content_type, delivery_mode, confirm_delivery, routing_key, msg))

    p1.start()
    time.sleep(2)
    p2.start()
