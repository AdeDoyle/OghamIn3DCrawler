"""Reads excel file types"""

import xlrd


def readXL(file, sheet):
    datafile = xlrd.open_workbook(file)
    datasheet = datafile.sheet_by_name(sheet)
    return datasheet


# print(readXL("Ogham Data.xlsx", "Ogham Data"))
# print(readXL("Ogham Data.xlsx"))
