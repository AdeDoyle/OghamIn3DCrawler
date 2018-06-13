"""Finds url beginning from entered url, combines it with href to make full hyperlink to new page"""

import re


def combinelink(url, ref):
    try:
        pattern = re.compile(r"\.[\w]*/")
        find = pattern.search(url)
        span = (find.span())
        endpat = span[1]
        urlstub = url[:endpat]
        newlink = urlstub + ref
        return newlink
    except AttributeError:
        return "Unable to find website."


# print(combinelink("https://ogham.celt.dias.ie/menu.php?lang=en&menuitem=30", "site.php?lang=en&site=Aglish"))
