#Improved Redge after more experience
import asyncio
import codecs
from http import client
from pydoc import describe
from tempfile import tempdir
from time import sleep
from itertools import chain
from socket import setdefaulttimeout

import discord
import os
import subprocess
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import time
token = 'MTAxMjc3MjM2Mzc3NzA5MzcxMg.G3Y6pR.Zfxjr91X4kAz7spTheY6nxLNYd4TKrGHQWeahA'
#https://discord.com/api/oauth2/authorize?client_id=921811125799125023&permissions=527744384064&scope=bot 
#from discreactbot import *


intents = discord.Intents.all()
intents.members = True #New intents for discord bots. Can use this many times
bot = commands.Bot(command_prefix="$", intents=intents)
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def Start(ctx):
    
#will define commands here, but functions in other. 

bot.run(token)

