import os

import discord
from discord.ext import commands
from discord.ext.commands import Context
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = commands.Bot(command_prefix='.')


@client.command()
async def load(ctx: Context, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send("Loaded Cog")


@client.command()
async def unload(ctx: Context, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send("Unloaded Cog")


@client.command()
async def reload(ctx: Context, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send("Reloaded Cog")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[0:-3]}')

@client.event
async def on_ready():
    print('Bot is ready lol XD')

client.run('OTE4OTE0OTE5MjY3NzAwNzQ3.YbOMNQ.vWCeeOuoWNo0Je1fHQ1qQXgPLnE')
