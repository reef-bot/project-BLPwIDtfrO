# role_management.py

import discord

class RoleManagement:
    def __init__(self, bot):
        self.bot = bot

    async def assign_role(self, user, role_name):
        role = discord.utils.get(user.guild.roles, name=role_name)
        if role is not None:
            await user.add_roles(role)
        else:
            print(f"Role {role_name} not found in the server.")

    async def remove_role(self, user, role_name):
        role = discord.utils.get(user.guild.roles, name=role_name)
        if role is not None:
            await user.remove_roles(role)
        else:
            print(f"Role {role_name} not found in the server.")

    async def list_roles(self, guild):
        roles = guild.roles
        role_list = [role.name for role in roles]
        return role_list

    async def create_role(self, guild, role_name):
        try:
            await guild.create_role(name=role_name)
            print(f"Role {role_name} created successfully.")
        except discord.Forbidden:
            print("Bot does not have permission to create roles.")
        except discord.HTTPException:
            print("An error occurred while creating the role.")