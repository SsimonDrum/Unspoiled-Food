#!/usr/bin/python

import psycopg2
import logging

from domain.food_item import FoodItem

# Connect to your postgres DB
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="4drums",
    target_session_attrs="read-write"
)

class FoodItemInsertor():
  def __init__(
    self,
    level: int = logging.INFO,
    logger: logging.Logger = logging.getLogger(__name__),
    db_name: str = "postgres",
    db_user: str = "postgres",
    db_password: str = "4drums",
    db_host="localhost",
    db_port=5432
    ):
    self.conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    ),
    self.level = level
    self.logger = logger
    self.insert_food_item()

  def insert_food_item(self):
      query = """
          INSERT INTO food_items (name, category, calories)
          VALUES (%s, %s, %s)
      """
      with self.conn.cursor() as cursor:
          cursor.execute(query, (food_item.name, food_item.category, food_item.expiration_date))
      self.conn.commit()

  def close_connection(self):
      self.conn.close()
