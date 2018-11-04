from bs4 import BeautifulSoup
from pathlib import Path
import os
import random
import requests
import shelve
import webbrowser


base_url = "https://doc.python.org/3/library/"


def main():
    with shelve.open(os.path.join(Path.home(), ".rplp", "links.db")) as shelf:
        links = shelf["links"]
        link = random.choice(links)
        webbrowser.open(base_url + link)


def get_links():
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, "html.parser")
    links = [x.get('href') for x in soup.find_all('ul')[1].find_all('a')]
    with shelve.open(os.path.join(Path.home(), ".rplp", "links.db")) as shelf:
        shelf["links"] = links
