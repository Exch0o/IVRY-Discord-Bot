import discord
import discord, json
from discord.ext import commands
import random 
import asyncio
from asyncio import sleep
import requests
import json
import data 
from data import config

client = commands.Bot(command_prefix='.')
client.remove_command('help')
client.load_extension("lib.cogs.Help")
client.load_extension("lib.cogs.General Commands")
client.load_extension("lib.cogs.Fun Commands")
client.load_extension("lib.cogs.Music")
client.load_extension("lib.cogs.Admin Commands")
client.load_extension("lib.cogs.Events")

async def status():
    while True:
        await client.wait_until_ready()
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='for .Help'))
        await sleep(10)
        await client.change_presence(activity=discord.Game(name=f'on {len(client.guilds)} servers | .Help'))
        await sleep(10)
@client.event
async def on_ready():
    print(f'{client.user} has Awoken!')
client.loop.create_task(status())

@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Unknown Command Try .help') 

client.run(config.token)