import pika
from config import config

class rabbitmq(object):
    def __init__(self):
        self.cfg = config().generate()
        self.host = self.cfg['RabbitMQ']['host']
        self.port = self.cfg['RabbitMQ']['port']
        self.vhost = self.cfg['RabbitMQ']['vhost']
        self.username = self.cfg['RabbitMQ']['user']
        self.password = self.cfg['RabbitMQ']['pass']
        self.exchange = self.cfg['RabbitMQ']['exchange']
        self.exchange_type = self.cfg['RabbitMQ']['exchange_type']

        # Sets up the connection
        credentials = pika.PlainCredentials(self.username, self.password)
        parameters = pika.ConnectionParameters(credentials=credentials, host=self.host, virtual_host=self.vhost)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exchange, exchange_type=self.exchange_type)

    def send_message(self, message, routing_key):
        self.channel.basic_publish(exchange=self.exchange, routing_key=routing_key, body=message)

    def worker(self, queue, routing_key):
        self.channel.queue_declare(queue=queue, durable=True)
        self.channel.queue_bind(exchange=self.exchange, queue=queue, routing_key=routing_key)
        self.channel.basic_qos(prefetch_count=1)
        return self.channel

    def close(self):
        self.connection.close()
