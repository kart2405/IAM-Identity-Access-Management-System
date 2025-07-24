import logging
from datetime import datetime

logging.basicConfig(filename='activity.log', level=logging.INFO, format='%(asctime)s %(message)s')

class LoggingService:
    @staticmethod
    def log_event(user_id: int, action: str, details: str = ""):
        logging.info(f"user_id={user_id} action={action} details={details}") 