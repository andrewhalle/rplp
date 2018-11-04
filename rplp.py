from bs4 import BeautifulSoup
import random
import requests
import webbrowser

base_url = "https://doc.python.org/3/library/"

def main():
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, "html.parser")
    links = [x.get('href') for x in soup.find_all('ul')[1].find_all('a')]
    link = random.choice(links)
    webbrowser.open(base_url + link)
