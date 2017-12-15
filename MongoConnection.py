import pymongo
import openpyxl
client = pymongo.MongoClient()
db = client.test
url = "www.manishjathan.com"
name = "Manish Jathan"
site = db.sites.find_one()
if site['url'] != url and site['name'] != name:
    db.sites.insert({"url" : url,"name" : name})
else:
    print(url)
    print(name)
    print("Record already Present")

#Creating a new table in Mongo
#containing Banking Transactions
#First tuple is inserted this way to create the schema
db = client.MoneyLaundering
try:
    db.bankingTransactions.remove()
    db.bankingTransactions.insert({
            "hour":1,
            "type":"PAYMENT",
            "amount":9839.64,
            "nameOrig":"C1231006815",
            "oldBalanceOrig":170136.0,
            "newBalanceOrig":160296.36,
            "nameDest": "M1979787155",
            "oldBalanceDest":0.0,
            "newBalanceDest":0.0,
            "isFraud":0,
            "isFlaggedFraud":0
    })
    print("Successfully Inserted the record")
except:
    print("Insertion Unsuccessful!")

#Read the CSV files and
#create a list of dictionary
#insert into mongo database

import fileinput
wb = openpyxl.load_workbook('Book1.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
row = []
row_list = []
for i in range(2,50):
    row = []
    for j in range(1,11):
        row.append(sheet.cell(row=i, column=j).value)
    row_list.append(row)


document = {
            "hour":0,
            "type":"",
            "amount":0.0,
            "nameOrig":"",
            "oldBalanceOrig":0.0,
            "newBalanceOrig":0.0,
            "nameDest": "",
            "oldBalanceDest":0.0,
            "newBalanceDest":0.0,
            "isFraud":0,
            "isFlaggedFraud":0
            }
keys = []
for key in document.keys():
    keys.append(key)

bulkData = []
for row in row_list:
    index = 0
    for col in row:
            document[keys[index]] = col
            index +=1
    #Creatinga a shallow copy of the dictionary document
    bulkData.append(document.copy())

#Inserting bulk Data
db.bankingTransactions.insert(bulkData)