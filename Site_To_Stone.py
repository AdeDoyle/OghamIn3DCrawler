"""Takes list of single stone links and site links (output of Stone_Links).
   Finds the link to the stone where site link given."""

from Plain_Text import plaintext
from Stone_Links import stonelinks
from Combine_Link import combinelink


def sitetostone(url):
    mixedlist = stonelinks(url)
    fixedlist = []
    for link in mixedlist:
        if "stone.php?" in link:
            fixedlist.append(link)
        elif "site.php?" in link:
            sitehtml = plaintext(link)
            if "<script>window.location=" in sitehtml:
                sitelinkstart = sitehtml.find("<script>window.location=")
                linkstring = sitehtml[sitelinkstart:]
                sitelinkend = linkstring.find("</script>")
                linkstring = linkstring[25:sitelinkend-2]
                stonelink = combinelink(url, linkstring)
                fixedlist.append(stonelink)
            else:
                fixedlist.append("Problem Link: " + link)
    return fixedlist


# count = 0
# for item in sitetostone("https://ogham.celt.dias.ie/menu.php?lang=en&menuitem=30"):
#     count += 1
#     print(str(count) + ". " + item)
