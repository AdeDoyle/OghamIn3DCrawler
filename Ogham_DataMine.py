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
                            changespot = namestring.find("    ")
                            namestring = namestring[:changespot] + " " + namestring[changespot + 4:]
                        if "  " in namestring:
                            changespot = namestring.find("  ")
                            namestring = namestring[:changespot] + " " + namestring[changespot + 2:]
                        if namestring[-2:] == "  ":
                            namestring = namestring[:-2]
                        if namestring[-1:] == " ":
                            namestring = namestring[:-1]
                        if namestring[-1:] == ".":
                            namestring = namestring[:-1]
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
                        transcend = searchstring.find("</div")
                        transcstring = searchstring[:transcend]
                        newstart = transcstring.find("div")
                        transcstring = transcstring[newstart:]
                        newstart = transcstring.find(">")
                        transcstring = transcstring[newstart + 1:]
                        if transcstring[0] == "\n":
                            transcstring = transcstring[1:]
                        if "<a href=" in transcstring:
                            transcstring = bleach.clean(transcstring, tags=[], strip=True)
                        if "<a id=" in transcstring:
                            refstart = transcstring.find("<a id=")
                            refend = (transcstring.find("</a>") + 4)
                            transcstring = transcstring[:refstart] + transcstring[refend:]
                        if '<br id="al">' in transcstring:
                            bridcount = transcstring.count('<br id="al">')
                            for i in range(0, bridcount):
                                refstart = transcstring.find('<br id="al">')
                                transcstring = transcstring[:refstart] + transcstring[refstart + 12:]
                        if '<br id="al2">' in transcstring:
                            bridcount = transcstring.count('<br id="al2">')
                            for i in range(0, bridcount):
                                refstart = transcstring.find('<br id="al2">')
                                transcstring = transcstring[:refstart] + transcstring[refstart + 13:]
                        if '<span class="linenumber">' in transcstring:
                            spinclasscount = transcstring.count('<span class="linenumber">')
                            for i in range(0, spinclasscount):
                                refstart = transcstring.find('<span class="linenumber">')
                                transcstring = transcstring[:refstart] + transcstring[refstart + 25:]
                        if "</span>" in transcstring:
                            linkcount = transcstring.count("/span")
                            for i in range(0, linkcount):
                                linkend = transcstring.find("</span>")
                                transcstring = transcstring[:linkend] + transcstring[linkend + 7:]
                        if "\xa0" in transcstring:
                            spacenum = transcstring.count("\xa0")
                            for i in range(0, spacenum):
                                spacepoint = transcstring.find("\xa0")
                                transcstring = transcstring[:spacepoint] + " " + transcstring[spacepoint + 1:]
                        if " ̣" in transcstring:
                            dotnum = transcstring.count(" ̣")
                            for i in range(0, dotnum):
                                dotplace = transcstring.find(" ̣")
                                transcstring = transcstring[:dotplace] + "." + transcstring[dotplace + 2:]
                        if "  " in transcstring:
                            spacescount = transcstring.count("  ")
                            for i in range(0, spacescount):
                                spaceplace = transcstring.find("  ")
                                transcstring = transcstring[:spaceplace] + " " + transcstring[spaceplace + 2:]
                        if transcstring[0] == " ":
                            transcstring = transcstring[1:]
                            try:
                                if transcstring[0] == " ":
                                    transcstring = transcstring[1:]
                            except IndexError:
                                pass
                        try:
                            if transcstring[-1] == " ":
                                transcstring = transcstring[:-1]
                        except IndexError:
                            pass
                        stonedata.append(transcstring)
                    """Get translation"""
                    """Get 3D obj file"""
        datalist.append(stonedata)
    return datalist


for list in datamine("https://ogham.celt.dias.ie/menu.php?lang=en&menuitem=30"):
    print(list)
