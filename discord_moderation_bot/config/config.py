# File: discord_moderation_bot/config/config.py

import os

# Configuration for the Discord moderation bot

# Get the Discord bot token from the environment variables
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Prefix for bot commands
BOT_PREFIX = '!'

# Channels for logging moderation actions
MOD_LOG_CHANNEL = 'moderation_logs'

# Database configuration
DATABASE_NAME = 'moderation_logs.db'
DATABASE_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'database', DATABASE_NAME)