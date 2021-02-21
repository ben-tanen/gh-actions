import os, requests
from bs4 import BeautifulSoup
import spotipy

req = requests.get("http://ben-tanen.com")

if req.status_code == 200:
    soup = BeautifulSoup(req.text, "html.parser")
    print(soup.prettify()[:200])