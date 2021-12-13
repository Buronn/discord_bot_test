import os

import discord
from discord.ext import commands
from discord.ext.commands import Context
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
intents = discord.Intents().all()
client = commands.Bot(command_prefix='.', intents=intents)
client.remove_command('help')
bot_token = os.getenv('BOT_TOKEN')

@client.command()
async def load(ctx: Context, *extension):
    if extension:
        try:
            client.load_extension(f'cogs.{extension[0]}')
            await ctx.send("Loaded Cog")
        except Exception as e:
            await ctx.send(f'Error: {e}')
    else:
        try:
            client.load_extension(f'cogs.commands')
            await ctx.send('Loaded commands')
        except Exception as e:
            await ctx.send(f'{e}')


@client.command()
async def unload(ctx: Context, *extension):
    if extension:
        try:
            client.unload_extension(f'cogs.{extension[0]}')
            await ctx.send("Unloaded Cog")
        except Exception as e:
            await ctx.send(f'Error: {e}')
    else:
        try:
            client.unload_extension(f'cogs.commands')
            await ctx.send('Unloaded commands')
        except Exception as e:
            await ctx.send(f'{e}')


@client.command()
async def reload(ctx: Context, *extension):
    if extension:
        try:
            client.unload_extension(f'cogs.{extension[0]}')
            client.load_extension(f'cogs.{extension[0]}')
            await ctx.send("Reloaded Cog")
        except Exception as e:
            await ctx.send(f'Error: {e}')
    else:
        try:
            client.reload_extension(f'cogs.commands')
            await ctx.send('Reloaded commands')
        except Exception as e:
            await ctx.send(f'{e}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[0:-3]}')

@client.event
async def on_ready():
    print('Bot is ready lol XD')

client.run(bot_token)
