"""Opens the web page entered and returns plain HTML code."""

import requests


def plaintext(url):
    web_source = url
    source_code = requests.get(web_source)
    plain_text = source_code.text
    return plain_text


# print(plaintext('https://ogham.celt.dias.ie/site.php?lang=en&site=Trinity_College_Dublin'))
