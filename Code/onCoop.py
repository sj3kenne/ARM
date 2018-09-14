from xlrd import open_workbook

# Collect inputs
toReadFile = str(raw_input("File to read: "))
minSupport = int(raw_input("Support %: "))
minConfidence = int(raw_input("Support %: "))

rawSet = {}
transactions = 0
customers = []
# Read file
wb = open_workbook(toReadFile)

for sheet in wb.sheets():
    numRows = sheet.numrows
    numCols = sheet.ncols
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
#Changed from https://stackoverflow.com/questions/22169325/read-excel-file-in-python


oneItemList = []
# 1-item set
for customer in customers:
    if (100 * customers[customer]/transactions ) >= minSupport:
        oneL = []
        oneL.append(customer)
        oneItemList.append(oneL)

# candidate k-itemset, canSet
# (k-1)-itemset, kMinus1
def apriori_func (kminus1, k)
    length = k
    canSet = []
    for list1 in kMinus1:
        for list2 in kMinus1:
            count = 0
            c = []