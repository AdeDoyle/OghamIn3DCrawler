"""Goes to pages for each stone on the Ogham 3D website and collects data:
   Stone Place, Roman Transcription, Translation, 3D View, Page Link
   Opens current Ogham Data file and compares contents
   Any new stones' data on the site is added to a new .xls file"""

from ReadXL import readXL
from xlwt import Workbook
from Ogham_DataMine import datamine


def updateData(url):
    newdata = []
    xlfile = []
    datasheet = readXL("Ogham Data.xlsx", "Ogham Data")
    rownum = datasheet.nrows
    for i in range(1, rownum):
        transcheck = "{0}".format(datasheet.cell(i, 2).value)
        xlfile.append(transcheck)
    for list in datamine(url):
        if list[1] not in xlfile:
            newdata.append(list)
    return newdata


def updateSaveData(url):
    wb = Workbook()
    sheet = wb.add_sheet("Ogham Data")
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
    blankcols = [1, 4, 5]
    nocols = [3, 6, 8]
    for list in updateData(url):
        rownum += 1
        colnum = 0
        listnum = 0
        datalen = len(list) + len(blankcols) + len(nocols)
        for i in range(0, datalen):
            if colnum in blankcols:
                sheet.write(rownum, colnum, "")
                colnum += 1
            elif colnum in nocols:
                sheet.write(rownum, colnum, "No")
                colnum += 1
            else:
                sheet.write(rownum, colnum, list[listnum])
                colnum += 1
                listnum += 1
    wb.save("Ogham Update.xls")


# itemcount = 0
# for item in updateData("https://ogham.celt.dias.ie/menu.php?lang=en&menuitem=30"):
#     itemcount += 1
#     print(str(itemcount) + ". ")
#     print(item)

updateSaveData("https://ogham.celt.dias.ie/menu.php?lang=en&menuitem=30")
