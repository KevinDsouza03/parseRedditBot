#personal use script
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
import json
#Function can run on single time. Meaning, one run then compare, then compare etc.


class redditData:
    def __init__(self,SR,title,link):
        self.SR = SR
        self.title = title
        self.link = link


def read_secrets(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        
    username = data.get('username')
    password = data.get('password')
    token = data.get('token')
    client_id = data.get('CLIENT_ID')
    secret_key = data.get('SECRET_KEY')
    
    return username, password, token, client_id, secret_key

secrets_filename = 'secrets.json'  # can also replace with path to JSON file
username, password, TOKEN, CLIENT_ID, SECRET_KEY = read_secrets(secrets_filename)


auth = rq.auth.HTTPBasicAuth(CLIENT_ID,SECRET_KEY) 
#logging into reddit api
data = {
    'grant_type': 'password',
    'username': username,
    'password': password
}

headers = {'User-Agent' : 'ScraperKevinDAPI/0.0.1'}
res = rq.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth,data=data,headers=headers)

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


def keyword_add(subreddit):
    pass