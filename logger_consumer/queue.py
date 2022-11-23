import pika

from config import (
  QUEUE_URL,
  QUEUE_PORT,
  EXCHANGE,
  QUEUE,
)

class Queue:
  def __init__(self):
    self.host = QUEUE_URL
    self.port = QUEUE_PORT
    self.exchange = EXCHANGE
    self.queue = QUEUE

    self.queue_name = None
    self.channel = None

  def connect(self):
    connection = pika.BlockingConnection(
      pika.ConnectionParameters(
        host=self.host,
        port=self.port,
      )
    )
    channel = connection.channel()
    self.channel = channel

  def queue_bind(self):
    self.channel.exchange_declare(self.exchange, exchange_type='direct')
    result = self.channel.queue_declare(queue=self.queue)
    self.queue_name = result.method.queue
    self.channel.queue_bind(exchange=self.exchange, queue=self.queue_name)

  def set_channel_callback(self, callback):
    self.channel.basic_consume(
      queue=self.queue_name,
      auto_ack=True,
      on_message_callback=callback
    )
    return self.channel