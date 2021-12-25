import logging
from app import db
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text
from kafka import KafkaConsumer


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")
TOPIC_NAME = 'locations'
KAFKA_SERVER = 'localhost:9092'
kafka_consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER)

class LocationSinkService:
    @staticmethod
    def save():
        for message in kafka_consumer:
            location = message.value
            db.session.add(location)
            db.session.commit()





    



