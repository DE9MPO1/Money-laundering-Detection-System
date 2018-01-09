import pymongo
import openpyxl





def LoadData(excelSheet,sheetName,numberOfRecords):

    print("Load Data")
    # Creating a new table in Mongo
    # containing Banking Transactions
    # First tuple is inserted this way to create the schema
    client = pymongo.MongoClient()
    db = client.MoneyLaundering

    try:
        db.bankingTransactions.remove()
        db.bankingTransactions.insert({
            "hour": 1,
            "type": "PAYMENT",
            "amount": 9839.64,
            "nameOrig": "C1231006815",
            "oldBalanceOrig": 170136.0,
            "newBalanceOrig": 160296.36,
            "nameDest": "M1979787155",
            "oldBalanceDest": 0.0,
            "newBalanceDest": 0.0,
            "isFraud": 0,
            "isFlaggedFraud": 0
        })
        print("Successfully Inserted the record")
    except:
        print("Insertion Unsuccessful!")


    wb = openpyxl.load_workbook(excelSheet)
    sheet = wb.get_sheet_by_name(sheetName)
    #row will contain individual rows of the excel sheet
    row = []
    #row list contains all the rows of excel sheet
    row_list = []
    #from 2nd to 1000th row
    for i in range(2,numberOfRecords):
        row = []
        #from 1st to 11th column
        for j in range(1,11):
            row.append(sheet.cell(row=i, column=j).value)
        row_list.append(row)


    #Defining the Schema with some default values
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
    #Keys List contains all the attributes of Dictionary Object

    #Bulk Data is a List of dictionary objects which will be inserted into MongoDB database as a JSON object.
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