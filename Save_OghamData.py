from xlwt import Workbook
from Ogham_DataMine import datamine


def SaveData(url):
    wb = Workbook()
    sheet = wb.add_sheet("Ogham Data")
    sheet.write(0, 0, "Stone ID")
    sheet.write(0, 1, "Transcription")
    sheet.write(0, 2, "Translation")
    sheet.write(0, 3, "3D View")
    sheet.write(0, 4, "URL")
    rownum = 0
    for list in datamine(url):
        rownum += 1
        colnum = 0
        for item in list:
            sheet.write(rownum, colnum, item)
            colnum += 1
    wb.save("Ogham Data.xls")


SaveData("https://ogham.celt.dias.ie/menu.php?lang=en&menuitem=30")
