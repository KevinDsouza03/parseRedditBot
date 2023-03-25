#Create Functions:
import requests as rq
from bs4 import BeautifulSoup
import time

#Function can run on single time. Meaning, one run then compare, then compare etc.

def Reddit_parse(link,mem_spot):

    reqs = rq.post(link)
    reqs = rq.get(link)