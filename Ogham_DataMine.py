"""Goes to pages for each stone on the Ogham 3D website and collects data:
   Transcription, Translation, 3D File/Link, Image"""

from Site_To_Stone import sitetostone
from Plain_Text import plaintext
from Findrefs import findrefs
from Combine_Link import combinelink
import bleach


def datamine(url):
    datalist = []
    for link in sitetostone(url):
        stonedata = []
        """Gets stone's description link"""
        if "description" in plaintext(link):
            for desclink in findrefs(link):
                if "description" in desclink:
                    descrlink = combinelink(url, desclink)
                    stonehtml = plaintext(descrlink)
                    """Get stone's name/placename"""
                    if "h1" in stonehtml:
                        namestart = stonehtml.find("h1")
                        nameend = stonehtml.find("</h1")
                        namestring = stonehtml[namestart:nameend]
                        if "CIIC" in namestring:
                            newstart = namestring.find("CIIC")
                            namestring = namestring[newstart:]
                            newstart = namestring.find(". ")
                            namestring = namestring[newstart + 2:]
                        else:
                            newstart = namestring.find(">")
                            namestring = namestring[newstart + 1:]
                        """Removes extraneous spaces, lines and html code"""
                        if "\n" in namestring:
                            newlinecount = namestring.count("\n")
                            for i in range(0, newlinecount):
                                changespot = namestring.find("\n")
                                namestring = namestring[:changespot] + " " + namestring[changespot + 1:]
                        if "  " in namestring:
                            spacecount = namestring.count("  ")
                            for i in range(0, spacecount):
                                changespot = namestring.find("  ")
                                namestring = namestring[:changespot] + " " + namestring[changespot + 2:]
                        if "            " in namestring:
                            changespot = namestring.find("            ")
                            namestring = namestring[:changespot] + " " + namestring[changespot + 12:]
                        if "           " in namestring:
                            changespot = namestring.find("           ")
                            namestring = namestring[:changespot] + " " + namestring[changespot + 11:]
                        if "         " in namestring:
                            changespot = namestring.find("         ")
                            namestring = namestring[:changespot] + " " + namestring[changespot + 9:]
                        if "       " in namestring:
                            changespot = namestring.find("       ")
                            namestring = namestring[:changespot]
                        if "    " in namestring:
                            spacescount = namestring.count("    ")
                            for i in range(0, spacescount):
                                changespot = namestring.find("    ")
                                namestring = namestring[:changespot] + " " + namestring[changespot + 4:]
                        if "  " in namestring:
                            spacescount = namestring.count("  ")
                            for i in range(0, spacescount):
                                spaceplace = namestring.find("  ")
                                namestring = namestring[:spaceplace] + " " + namestring[spaceplace + 2:]
                        if "  " in namestring:
                            spacescount = namestring.count("  ")
                            for i in range(0, spacescount):
                                spaceplace = namestring.find("  ")
                                namestring = namestring[:spaceplace] + " " + namestring[spaceplace + 2:]
                        namestring = namestring.strip(" .")
                        if '<span class="italic">' in namestring:
                            changespot = namestring.find('<span class="italic">')
                            namestring = namestring[:changespot] + namestring[changespot + 21:]
                        if '</span>' in namestring:
                            changespot = namestring.find('</span>')
                            namestring = namestring[:changespot] + namestring[changespot + 7:]
                        if namestring[0] == " ":
                            namestring = namestring[1:]
                        if " ," in namestring:
                            changespot = namestring.find(" ,")
                            namestring = namestring[:changespot] + namestring[changespot + 1:]
                        if " )" in namestring:
                            changespot = namestring.find(" )")
                            namestring = namestring[:changespot] + namestring[changespot + 1:]
                        stonedata.append(namestring)
                    """Gets transcription. Removes white space at start and end, and html code"""
                    if "Transcription" in stonehtml:
                        transcstart = stonehtml.find("Transcription")
                        searchstring = stonehtml[transcstart + 14:]
                        newstart = searchstring.find("Transcription")
                        searchstring = searchstring[newstart:]
                        transcend = searchstring.find("Translation")
                        transcstring = searchstring[:transcend]
                        transcstring = bleach.clean(transcstring, tags=['br'], strip=True)
                        transcstring = transcstring[13:]
                        transcstring = transcstring.strip()
                        if transcstring == "":
                            transcstring = "No Transcription Available"
                        if "<br>" in transcstring:
                            linenum = transcstring.count("<br>")
                            for i in range(0, linenum):
                                linepoint = transcstring.find("<br>")
                                transcstring = transcstring[:linepoint] + " " + transcstring[linepoint + 4:]
                        if "\xa0" in transcstring:
                            spacenum = transcstring.count("\xa0")
                            for i in range(0, spacenum):
                                spacepoint = transcstring.find("\xa0")
                                transcstring = transcstring[:spacepoint] + " " + transcstring[spacepoint + 1:]
                        if "&lt;" in transcstring:
                            tagnum = transcstring.count("&lt;")
                            for i in range(0, tagnum):
                                tagpoint = transcstring.find("&lt;")
                                transcstring = transcstring[:tagpoint] + "<" + transcstring[tagpoint + 4:]
                        if "&gt;" in transcstring:
                            tagnum = transcstring.count("&gt;")
                            for i in range(0, tagnum):
                                tagpoint = transcstring.find("&gt;")
                                transcstring = transcstring[:tagpoint] + ">" + transcstring[tagpoint + 4:]
                        if " ̣" in transcstring:
                            dotnum = transcstring.count(" ̣")
                            for i in range(0, dotnum):
                                dotplace = transcstring.find(" ̣")
                                transcstring = transcstring[:dotplace] + "." + transcstring[dotplace + 2:]
                        if "    " in transcstring:
                            spacescount = transcstring.count("    ")
                            for i in range(0, spacescount):
                                spaceplace = transcstring.find("    ")
                                transcstring = transcstring[:spaceplace] + " " + transcstring[spaceplace + 4:]
                        if "   " in transcstring:
                            spacescount = transcstring.count("   ")
                            for i in range(0, spacescount):
                                spaceplace = transcstring.find("   ")
                                transcstring = transcstring[:spaceplace] + " " + transcstring[spaceplace + 3:]
                        if "  " in transcstring:
                            spacescount = transcstring.count("  ")
                            for i in range(0, spacescount):
                                spaceplace = transcstring.find("  ")
                                transcstring = transcstring[:spaceplace] + " " + transcstring[spaceplace + 2:]
                        stonedata.append(transcstring)
                    """Gets translation, if available. Removes whitespace and html code."""
                    if "Translation" in stonehtml:
                        transtart = stonehtml.find("Translation")
                        searchstring = stonehtml[transtart + 11:]
                        newstart = searchstring.find("Translation")
                        searchstring = searchstring[newstart:]
                        transend = searchstring.find("Commentary")
                        transtring = searchstring[:transend]
                        transtring = bleach.clean(transtring, tags=[], strip=True)
                        transtring = transtring[11:]
                        transtring = transtring.strip()
                        if "''" in transtring:
                            quotemarkcount = transtring.count("''")
                            for i in range(0, quotemarkcount):
                                quotemarkplace = transtring.find("''")
                                transtring = transtring[:quotemarkplace] + "'" + transtring[quotemarkplace + 2:]
                        if "  " in transtring:
                            spacescount = transtring.count("  ")
                            for i in range(0, spacescount):
                                spaceplace = transtring.find("  ")
                                transtring = transtring[:spaceplace] + " " + transtring[spaceplace + 2:]
                        if transtring == "":
                            transtring = "No Translation Available"
                        stonedata.append(transtring)
                    """Finds if 3D View is available on the website."""
                    if "3D View" in stonehtml:
                        threedstring = "Yes"
                    else:
                        threedstring = "No"
                    stonedata.append(threedstring)
                    stonedata.append(descrlink)
        datalist.append(stonedata)
    return datalist


# for list in datamine("https://ogham.celt.dias.ie/menu.php?lang=en&menuitem=30"):
#     print(list)
