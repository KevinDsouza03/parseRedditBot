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
#MTAxMjc3MjM2Mzc3NzA5MzcxMg.G3Y6pR.Zfxjr91X4kAz7spTheY6nxLNYd4TKrGHQWeahA Token
#https://discord.com/api/oauth2/authorize?client_id=921811125799125023&permissions=527744384064&scope=bot 
#from discreactbot import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
options = Options()
#options.add_argument('--headless')
path_to_extension = r'G:\5.1.1_0'
options.add_argument('--disable-gpu')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('load-extension=' + path_to_extension)


service = Service(executable_path="chromedriver")
driver = webdriver.Chrome(service=service, options=options)

intents = discord.Intents.all()
intents.members = True #New intents for discord bots. Can use this many times
bot = commands.Bot(command_prefix="$", intents=intents)
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def Start(ctx):
    
#will define commands here, but functions in other. 

bot.run('MTAxMjc3MjM2Mzc3NzA5MzcxMg.G3Y6pR.Zfxjr91X4kAz7spTheY6nxLNYd4TKrGHQWeahA')

