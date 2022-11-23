import sqlalchemy as db
import warnings
from sqlalchemy import exc as sa_exc

from sqlalchemy.orm import sessionmaker

from logger_consumer.model import Log

from config import (
  DATABASE_URL,
  DATABASE_PORT,
  DATABASE_USER,
  DATABASE_PASSWORD,
  DATABASE,
)

class Database:
  def __init__(self):
    self.db = DATABASE
    self.url = DATABASE_URL
    self.port = DATABASE_PORT

    self.user = DATABASE_USER
    self.password = DATABASE_PASSWORD

    self.engine = None

  def connect(self):
    self.engine = db.create_engine(
      f'mysql://{self.user}:{self.password}@{self.url}:{self.port}/{self.db}'
    )

  def create_table_if_not_exists(self, service_name):
    LogModel = self.get_log_model(service_name)
    LogModel.__table__.create(bind=self.engine, checkfirst=True)

  def insert(self, data):
    LogModel = self.get_log_model(data['service_name'])
    del data['service_name']
    Session = sessionmaker(bind=self.engine)
    with Session() as session:
      session.add(LogModel(**data))
      session.commit()
  
  def close(self):
    self.engine.dispose()

  def get_log_model(self, service_name):
    with warnings.catch_warnings():
      warnings.simplefilter("ignore", category=sa_exc.SAWarning)
      class_name = f'Log_{service_name}'
      Model = type(class_name, (Log,), {
        '__tablename__': service_name
      })
    return Model

