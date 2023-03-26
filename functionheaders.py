#secret	cIxXuPvjqqOmlmrsM5E4dhR4-ZLJ2A
#personal use script
#0NMev7gCd_Lof_8ryVnRzA
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
import requests as rq
from bs4 import BeautifulSoup
import time
#Function can run on single time. Meaning, one run then compare, then compare etc.

class redditData:
    def __init__(self,SR,title,link):
        self.SR = SR
        self.title = title
        self.link = link



CLIENT_ID = '0NMev7gCd_Lof_8ryVnRzA'
SECRET_KEY = 'cIxXuPvjqqOmlmrsM5E4dhR4-ZLJ2A'
auth = rq.auth.HTTPBasicAuth(CLIENT_ID,SECRET_KEY) 
#logging into reddit api
data = {
    'grant_type' : 'password',
    'username' : 'blurzl',
    'password' : 'Bengal29'
}
headers = {'User-Agent' : 'ScraperKevinDAPI/0.0.1'}
res = rq.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth,data=data,headers=headers)

TOKEN = res.json()['access_token']
headers['Authorization'] = f'bearer {TOKEN}'
#essentially, logging in and getting access to API. this now lets us access every endpoint

def Reddit_parse(objectComparison):# add back memory spot for actual running. can make a class for reddit data, and then filter
    front = 'https://oauth.reddit.com/r/'
    end = '/new?limit=1'
    res = rq.get(front+objectComparison["SR"]+end,headers=headers)
    for post in res.json()['data']['children']:     #easier to do so in a array for json. can filter for returning to parser
        temp = {
            "title" :post['data']['title'],
            "link": ("https://www.reddit.com/" + post['data']['permalink'])
            } 
        #creating a temporary object compare.
        if (objectComparison["title"] == temp["title"]):
            return -1 #handle -1, do not print. go next?
        else:
            if (len(temp["title"]) > 255):
                pass
            else:
                objectComparison["title"] = temp["title"]
            if (len(temp["link"]) > 255):
                pass
            else:
                objectComparison["link"] = temp["link"] #uniqueness update
            return objectComparison
#data handling should be over.
    