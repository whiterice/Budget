#Budget.py

#---------------
#| Initialize  |
#---------------


#Imports
import os
import csv

#Constants
sBankDir = 'C:\Documents and Settings\Scott\Desktop\Budget\Bank'
sCreditCardDir = 'C:\Documents and Settings\Scott\Desktop\Budget\Credit Card'

lCategories = ['Unknown', 'Food', 'Mortgage', 'Gas', 'House', 'Fun', 'PC Credit Card', 'Other Bills']

lAccounts = ['Bank Accont', 'Credit Card']

#Classes
class Expense:
    'Class for each expense'

    def __init__(sDate, rCost, lLocation, lCategory):

        self.sDate = sDate
        self.rCost = rCost
        self.lLocation = lLocation
        self.sCategory = sCategory


#---------------
#|   Program   |
#---------------

#Get files names in working directories
lBankFiles = []
lBankFiles = os.listdir(sBankDir)

lCreditCardFiles = []
lCreditCartdFiles = os.listdir(sCreditCardDir)

#Combines them into a list of lists
lFiles = [lBankFiles, lCreditCartdFiles]

#Removes all unwanted files from the lists
for lists in lFiles:
    for i in lists:
        if i.find('.csv') == -1:
            lists.remove(i)
        else:
            pass

#Print Files to Terminal
print 'The Following Files were Imported'
x=0
for lists in lFiles:
    print lAccounts[x], ':'
    x=x+1
    for i in lists:
        print i
    print '\n'            
    

