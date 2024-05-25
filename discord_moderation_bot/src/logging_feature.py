# logging_feature.py

import logging
import asyncio

class LoggingFeature:
    def __init__(self, log_file):
        self.log_file = log_file
        logging.basicConfig(filename=log_file, level=logging.INFO)

    async def log_moderation_action(self, action, user_id, moderator_id):
        try:
            logging.info(f"Moderation Action: {action} - User ID: {user_id} - Moderator ID: {moderator_id}")
        except Exception as e:
            logging.error(f"Error logging moderation action: {e}")

    async def log_profanity_filter(self, message, user_id):
        try:
            logging.warning(f"Profanity Filter Triggered: Message - {message} - User ID: {user_id}")
        except Exception as e:
            logging.error(f"Error logging profanity filter: {e}")

    async def log_spam_detection(self, message, user_id):
        try:
            logging.warning(f"Spam Detection Triggered: Message - {message} - User ID: {user_id}")
        except Exception as e:
            logging.error(f"Error logging spam detection: {e}")