from xlrd import open_workbook

toReadFile = str(raw_input("File to read: "))
support = int(raw_input("Support %: "))
confidence = int(raw_input("Support %: "))

rawSet = {}
transactions = 0
customers = [
# Read file
wb = open_workbook('toReadFile')

for sheet in wb.sheets():
    numRows = sheets.numrows
    numCols = sheet.ncols

    #customers = [[]]

    row = []
    for row in range(1, numRows):
        values = []
        for col in range(numCols):
            value = (sheet.cell(row,col).value)
            try: 
                value = str(value)
                transactions += 1
            except ValueError:
                pass
            finally: 
                values.append(value)
        customers.append(values)
#From https://stackoverflow.com/questions/22169325/read-excel-file-in-python


oneItemList = []
# 1-item set
for key in rawSet:
    if (100 * supportOfEvent ) >= support:
        oneL = []
        oneL.append(key)

        



# Find itemsets of length n, frequency minSupport
itemsets = []
for each in rawSet:

