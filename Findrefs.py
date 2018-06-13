"""Finds the href for each link on a page"""

from Site_Open import siteopen


def findrefs(url):
    reflist = []
    html = siteopen(url)
    """Gets all links on page and adds them to reflist"""
    for link in html.findAll('a', href=True):
        ref = link.get('href')
        reflist.append(ref)
    return reflist


# checklist = findrefs('https://ogham.celt.dias.ie/menu.php?lang=en&menuitem=30')
# count = 0
# for item in checklist:
#     count += 1
#     print(str(count) + ": " + item)
