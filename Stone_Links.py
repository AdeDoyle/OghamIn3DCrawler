"""Finds all hyperlinks on ogham "browse" directory page.
   Separates links to stone pages from links to site pages.
   Goes to site pages and collects stone links from there also.
   Outputs links to all stones on the site."""

from Findrefs import findrefs
from Combine_Link import combinelink


def stonelinks(url):
    stonecount = 0
    sitecount = 0
    stone_links = []
    site_links = []
    allsites = []
    multistonesites = []
    onestonesites = []
    sitemark = "site.php?"
    stonemark = "stone.php?"
    """Gets links to all stone sites"""
    for ref in findrefs(url):
        if ref[:9] == sitemark:
            si_link = combinelink(url, ref)
            site_links.append(si_link)
    """Gets the names of sites, as they appear in links, of all sites on the ogham "browse" directory page"""
    for link in site_links:
        sitename = link[49:]
        allsites.append(sitename)
    """Gets the names of sites, as they appear in links, with more than one stone"""
    for link in site_links:
        for ref in findrefs(link):
            if ref[:10] == stonemark:
                for sitename in allsites:
                    if sitename in ref:
                        if sitename not in multistonesites:
                            multistonesites.append(sitename)
    """Gets the names of sites, as they appear in links, with one stone"""
    for sitename in allsites:
        if sitename not in multistonesites:
            onestonesites.append(sitename)
    """Gets links to each individual stone. Counts stones and sites."""
    """Gets links to stones from multi-stone sites"""
    multistonelinks = []
    for link in site_links:
        for ref in findrefs(link):
            if ref[:10] == stonemark:
                st_link = combinelink(url, ref)
                if st_link not in stone_links:
                    stonecount += 1
                    stone_links.append(st_link)
                    multistonelinks.append(st_link)
    """Gets links to stones from one-stone sites"""
    onestonelinks = []
    for ref in findrefs(url):
        if ref[:9] == sitemark:
            for onestonesite in onestonesites:
                if onestonesite in ref:
                    st_link = combinelink(url, ref)
                    if st_link not in stone_links:
                        stonecount += 1
                        stone_links.append(st_link)
                        onestonelinks.append(st_link)
    """Counts numbers of stones and sites, and prints results"""
    onestonelinkcount = 0
    for link in onestonelinks:
        onestonelinkcount += 1
    onestonesitecount = 0
    for site in onestonesites:
        onestonesitecount += 1
    multistonelinkcount = 0
    for link in multistonelinks:
        multistonelinkcount += 1
    multistonesitecount = 0
    for site in multistonesites:
        multistonesitecount += 1
    for site in allsites:
        sitecount += 1
    # print(str(sitecount) + " Sites")
    # print(str(multistonesitecount) + " Multi-stone sites")
    # print(str(onestonesitecount) + " One-stone sites")
    # print(str(stonecount) + " Stones")
    # print(str(multistonelinkcount) + " Multi-stone site stones")
    # print(str(onestonelinkcount) + " One-stone site stones")
    return stone_links


# stonelist = stonelinks('https://ogham.celt.dias.ie/menu.php?lang=en&menuitem=30')
# outcount = 0
# for stonelink in stonelist:
#     outcount += 1
#     print(str(outcount) + ". " + stonelink)
