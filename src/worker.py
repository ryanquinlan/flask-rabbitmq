#!/usr/bin/env python

from config import config
from rabbitmq import rabbitmq

cfg = config().generate()

queue = cfg['RabbitMQ']['queue']
key = cfg['RabbitMQ']['routing_key']

rabbit = rabbitmq()
channel = rabbit.worker(queue, key)

def consume(ch, method, props, body):
    print(body.decode('utf-8'))
    ch.basic_ack(delivery_tag = method.delivery_tag)


channel.basic_consume(consume, queue=queue)
print("Started Test Worker...")
channel.start_consuming()
