import os

QUEUE_URL = os.environ.get('QUEUE_URL', '127.0.0.1')
QUEUE_PORT = int(os.environ.get('QUEUE_PORT', 5672))
DATABASE_URL = os.environ.get('DATABASE_URL', '127.0.0.1')
DATABASE_PORT = int(os.environ.get('DATABASE_PORT', 3306))
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')

EXCHANGE = os.environ.get('EXCHANGE')
QUEUE = os.environ.get('QUEUE')
DATABASE = os.environ.get('DATABASE')