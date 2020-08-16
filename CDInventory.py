#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DMa, 2020-Aug-10, Added the dicRow1 line of code
# DMa, 2020-Aug-10, Added lstTbl.append(dicRow1)
# DMa, 2020-Aug-11, Added delID input command
# DMa, 2020-Aug-12, Added for loop in range(len(lstTbl))
# DMa, 2020-Aug-12, Added if lstTbl[i]['id'] == delID:
# DMa, 2020-Aug-13, Added del lstTbl[i]
# DMa, 2020-Aug-14, Added capability to allow user to write data into a .txt file

#------------------------------------------#

import json

# Declare Variables
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        break
    if strChoice == 'l':
       with open('strFileName', 'r') as file:
          lstTbl = json.load(file)
          lstTbl.append(lstTbl) 
          pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow1 = {'id': intID, 'title': strTitle, 'artist': strArtist}
        lstTbl.append(dicRow1)
    elif strChoice == 'i':
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(row['id'],row['title'], row['artist'], sep=',')   
        pass
    elif strChoice == 'd':
        delID = int(input("Please enter in the ID you want to delete: "))
        for i in range(len(lstTbl)):
            if lstTbl[i]['id'] == delID:
               del lstTbl[i]
               break
    elif strChoice == 's':
  	    with open('strFileName', 'w') as file:
             file.write(json.dumps(lstTbl))
    else:
       print('Please choose either l, a, i, d, s or x!')

