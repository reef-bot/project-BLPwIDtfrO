# main.py

import discord
from discord.ext import commands
from moderation_commands import ModerationCommands
from message_system import MessageSystem
from logging_feature import LoggingFeature
from profanity_filter import ProfanityFilter
from spam_detection import SpamDetection
from role_management import RoleManagement
from reporting_feature import ReportingFeature

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

moderation_commands = ModerationCommands()
message_system = MessageSystem()
logging_feature = LoggingFeature()
profanity_filter = ProfanityFilter()
spam_detection = SpamDetection()
role_management = RoleManagement()
reporting_feature = ReportingFeature()

@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}')

@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await moderation_commands.kick(ctx, member, reason)

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await moderation_commands.ban(ctx, member, reason)

@bot.command()
async def warn(ctx, member: discord.Member, *, reason=None):
    await moderation_commands.warn(ctx, member, reason)

@bot.event
async def on_message(message):
    await message_system.check_message(message)

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'An error occurred: {str(error)}')

bot.run('YOUR_DISCORD_BOT_TOKEN')