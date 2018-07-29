# OghamIn3DCrawler
Collects data about Ogham Stones recorded on the [Ogham3D](https://ogham.celt.dias.ie) website: Site, Transcription, Suggested translation, Online 3D Model Available, URL.

Automatic transliteration of the Roman transcription is applied, and hence, an Ogham transcription is created.

An Excel file is created containing all the data above, and allowing fields for manual assessments of transcriptions to be recorded.

Further Excel files can be created containing the same data for new stones as they are added to the website.


## Files Included

1. Combine_Link.py - Creates URLs to new pages on [Ogham3D](https://ogham.celt.dias.ie/menu.php?lang=en&menuitem=30) by combining "https://ogham.celt.dias.ie" with hrefs for stones/sites.

2. Findrefs.py - Finds hrefs for all links on a given web page.

3. Ogham_DataMine.py - Mines Data from [Ogham3D](https://ogham.celt.dias.ie/menu.php?lang=en&menuitem=30): Site, Transcription, Translation, Online 3D Model Available, URL.

4. Ogham_GO.py - Transliterates from Roman Script to Orthodox Ogham.

5. Plain_Text.py - Opens a URL and returns HTML code for the web page as plain text.

6. Read_XL.py - Opens an Excel file type and sheet, and returns data from that sheet.

7. Save_OghamData.py - Mines Data from [Ogham3D](https://ogham.celt.dias.ie/menu.php?lang=en&menuitem=30) and creates an Excel file (Ogham Data.xls) containing this data.

8. Save_UpdateOghamData.py - Mines Data from [Ogham3D](https://ogham.celt.dias.ie/menu.php?lang=en&menuitem=30), compares data to that in Ogham Data.xls, and creates an Excel file (Ogham Update.xls) containing only data for stones which does not already appear in Ogham Data.xls.

9. Site_Open.py - Opens a URL and returns parsed HTML code for the web page.

10. Site_To_Stone.py - Takes the output of Stone_Links.py and returns a complete list of URLs for stones on [Ogham3D](https://ogham.celt.dias.ie/menu.php?lang=en&menuitem=30).

11. Stone_Links.py - Finds all links to sites and stones on [Ogham3D](https://ogham.celt.dias.ie/menu.php?lang=en&menuitem=30) and returns all URLs.

### Prerequisites

Python 3

Python Libraries: bleach, bs4, re, requests, xlrd, xlwt

### IDE Used

PyCharm

### Tested On

Windows 10

## Authors

* **Adrian Doyle** - [AdeDoyle](https://github.com/AdeDoyle)
