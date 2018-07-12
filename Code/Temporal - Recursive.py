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


# Find itemsets of length n, frequency minSupport
# itemsets = []
# for each in rawSet:

class JourneyObj:
    def __init__(self):
        self.events = []
        self.support = 1
    def increaseSupport(self):
        self.support += 1
    def getJourney(self):
        return self.events
    def getSupport(self):
        return self.support

    #pass

currentJourneys = oneItemList

# My Way
def myTry(allCustomers, k):
    length = k
    
    possibleItems = {}
    for journey in allCustomers:
        currJourney = JourneyObj()
        addEventToJourney(journey, possibleItems, currJourney, 0, k)
    finalItemList = isSupportEnough(possibleItems)
    return finalItemList


def isSupportEnough(possibleItems):
    kItemList = []
    for journeys in possibleItems:
        if (100 * journeys.getSupport/transactions ) >= minSupport:
            kItemList.append(journeys)
    return kItemList

def addEventToJourney(journey, possibleItems, currJourney, count, length):
    event = journey[count]
    if (event in oneItemList) and (event not in currJourney) and (count < length):
        currJourney.events.append(event)
        count += 1
        if count < length:
            addEventToJourney(journey, possibleItems, currJourney, count, length)
    elif (count >= length):
        pass
        #This needs to take into account that a possible journey is collected, and put it into possibleItems.
        #It then needs to start on the next journey, (possibly starting from the same event), but not REDO 
        #the journey it just completed.
    else:
        count += 1
        addEventToJourney(journey, possibleItems, currJourney, count, length)
    
            newJourney = event
            newJourney.append(itemToAdd)
            if possibleItems[newJourney]:
                possibleItems[newJourney].increaseSupport()
            else:
                newJourneyObj = JourneyObj()
                newJourneyObj.events = [newJourney]
                possibleItems[newJourney] = newJourneyObj
    return possibleItems


# # Apriori
# def aprioriMethod(k):
#     length = k
#     Ck = []
#     for 

# # Frequent Itemset
# def freqItemSets():
#     k = 2
#     constructList = []
#     outputList = []
#     for item in oneItemList:
#         constructList.append(item)
#     while constructList != []:
