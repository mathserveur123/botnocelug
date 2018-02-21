import discord
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import logging
import re

var bot = new Discord.client

@client.event
async def on_ready():
    print("logged in as:")
    print(client.user.name)
    print("ID:")
    print(client.user.id)
    print("Ready to use !")


client.run("NDEzNDM4MDU1MTE5MzIzMTQ2.DWY0Pg.8-50NJXysjxQ07wURcUUjn11O4g")
