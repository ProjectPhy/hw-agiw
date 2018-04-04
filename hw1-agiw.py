import urllib.request
import json
from bs4 import BeautifulSoup
from tqdm import tqdm
import re

def readingfile():
    data = json.load(open('data.json'))
    return list(data)


def loadpage():
    listelements = readingfile()

    for elem in listelements:
        req = urllib.request.Request(elem)
        with urllib.request.urlopen(req) as response:
            the_page = response.read()

def get_headers_from_json():
    """
T  he function takes a json file with html_body and returns a list of headers.
It parses the headers, based on tags starting with 'h'.
It also parses urls and return them in a tuple: (headers, url)
"""
    data = json.loads(open('data.json').read())
    pattern = "h1" # | h2 | h3"
    # pattern = re.compile("^(?!.(href)).^h", re.IGNORECASE)
    headers_urls = []
    all_headers = []
    for x in tqdm(data):
        soup = BeautifulSoup(x[0], 'html.parser')
        html_headers = soup.find_all(re.compile(pattern))
        all_headers.append(html_headers)
        url = x[1]
        tuple_title_url = all_headers, url
        headers_urls.append(tuple_title_url)
        return headers_urls
