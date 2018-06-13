"""Opens the web page entered and returns parsed HTML code."""

import requests
from bs4 import BeautifulSoup


def siteopen(url):
    web_source = url
    source_code = requests.get(web_source)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    return soup


# print(siteopen('https://ogham.celt.dias.ie/menu.php?lang=en&menuitem=30'))
