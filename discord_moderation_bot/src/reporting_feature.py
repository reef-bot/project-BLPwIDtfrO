# reporting_feature.py

import discord
from discord.ext import commands

class ReportingFeature(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='report', help='Report an issue to server admins')
    async def report(self, ctx, user: discord.User, *, issue: str):
        """Report an issue to server admins"""
        # Logic to send the report to server admins
        admin_channel = discord.utils.get(ctx.guild.text_channels, name='admin-channel')
        if admin_channel:
            await admin_channel.send(f'{ctx.author.mention} has reported {user.mention} for: {issue}')
            await ctx.send('Your report has been submitted successfully.')
        else:
            await ctx.send('Admin channel not found. Please contact a server admin directly.')

def setup(bot):
    bot.add_cog(ReportingFeature(bot))