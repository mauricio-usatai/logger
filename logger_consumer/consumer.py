from logger_consumer.database import Database
import json

def consumer(ch, method, properties, body):
  data = json.loads(body)

  db = Database()
  db.connect()
  db.create_table_if_not_exists(data['service_name'])
  db.insert(data)
  db.close()
