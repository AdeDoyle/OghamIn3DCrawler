"""Goes to pages for each stone on the Ogham 3D website and collects data:
   Stone Place, Ogham Transcription, Roman Transcription, Translation, 3D View, Page Link
   Any stones' data on the site is added to a new .xls file"""

from xlwt import Workbook
from Ogham_DataMine import datamine
from Ogham_GO import deanogham


def SaveData(url):
    wb = Workbook()
    sheet = wb.add_sheet("New Ogham Data", cell_overwrite_ok=True)
    sheet.write(0, 0, "Stone ID")
    sheet.write(0, 1, "Ogham (Automatic Transcription)")
    sheet.write(0, 2, "Transcription")
    sheet.write(0, 3, "Transcription Amended?")
    sheet.write(0, 4, "Ogham (Assessed Transcription)")
    sheet.write(0, 5, "Usable?")
    sheet.write(0, 6, "Assessed?")
    sheet.write(0, 7, "Translation")
    sheet.write(0, 8, "Duplicate?")
    sheet.write(0, 9, "3D View?")
    sheet.write(0, 10, "URL")
    rownum = 0
    blankcols = [5]
    nocols = [3, 6, 8]
    oghamcols = [1, 4]
    for list in datamine(url):
        rownum += 1
        colnum = 0
        listnum = 0
        datalen = len(list) + len(blankcols) + len(nocols) + len(oghamcols)
        for i in range(0, datalen):
            if colnum in blankcols:
                sheet.write(rownum, colnum, "")
                colnum += 1
            elif colnum in nocols:
                sheet.write(rownum, colnum, "No")
                colnum += 1
            elif colnum in oghamcols:
                sheet.write(rownum, colnum, deanogham(list[1]))
                colnum += 1
            else:
                sheet.write(rownum, colnum, list[listnum])
                colnum += 1
                listnum += 1
    wb.save("New Ogham Data.xls")


SaveData("https://ogham.celt.dias.ie/menu.php?lang=en&menuitem=30")
