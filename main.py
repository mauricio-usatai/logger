from logger_consumer import Queue, consumer

def main():
  queue = Queue()
  queue.connect()
  queue.queue_bind()
  channel = queue.set_channel_callback(consumer)
  channel.start_consuming()

if __name__ == '__main__':
  main()
