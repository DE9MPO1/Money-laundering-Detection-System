import pymongo
import numpy as np
from pandas import Series,DataFrame

#Connecting with the database
client = pymongo.MongoClient()
db = client.MoneyLaundering

#Mapping CustomerId with Number
#Forming a tuple List
def mapCustomers():
    try:
        customerMap = {}
        tupleList = []
        transactions = db.bankingTransactions
        fromToTuple = transactions.find({},{'nameOrig':1,'nameDest':1,'_id':0})
        count = 0
        for transaction in fromToTuple:
            if transaction['nameOrig'] not in customerMap.keys():
                customerMap[transaction['nameOrig']] = count
                count += 1
            if transaction['nameDest'] not in customerMap.keys():
                customerMap[transaction['nameDest']] = count
                count += 1
            #print("%d -> %d" % (customerMap[transaction['nameOrig']], customerMap[transaction['nameDest']]))
            trans = (customerMap[transaction['nameOrig']],customerMap[transaction['nameDest']])
            try:
                tupleList.append(trans)
            except:
                tupleList = [trans]
        print(tupleList)
        return tupleList
    except:
        print("Error in Mapping !!")


class BucketContainer():
    def __init__(self):
        self.bucket = {}
        self.bucketCount = {}


def hashBasedBucketCount(tupleList):
    b = BucketContainer()
    for trans in tupleList:
        bucketIndex = ((trans[0]*10) + trans[1]) % 10
        try:
            if trans not in b.bucket:
                b.bucket[bucketIndex].append(trans)
        except:
            b.bucket[bucketIndex] = [trans]
    #print(b.bucket)
    for keys in b.bucket.keys():
        print(keys,b.bucket[keys])
        b.bucketCount[keys] = len(b.bucket[keys])
    for keys in b.bucketCount.keys():
        print(keys,b.bucketCount[keys])
    return b

def actualCount(tupleList):
    actualCount = {}
    for tuple in tupleList:
        if tuple not in actualCount.keys():
            actualCount[tuple] = 1
        else:
            actualCount[tuple] += 1
    for keys in actualCount.keys():
        print(keys,actualCount[keys])
    return actualCount

def filterOnActualCount(filteredBucketTuples,actualCount,minSupportCount):
    filteredActualCount = {}
    count = 0
    for keys in actualCount.keys():
        if actualCount[keys] > minSupportCount and keys in filteredBucketTuples.keys():
            filteredActualCount[keys] = actualCount[keys]
            count +=1
    print("Number of Transactions based on Actual Frequency : ",count)
    return filteredActualCount

def filterOnBucketCount(tupleList,bucketContainer,minSupportCount):
    itemSetCount = {}
    count = 0
    for tuple in tupleList:
        #Used List Comprehension
        key = [k for k, v in bucketContainer.bucket.items() if tuple in v]
        if(bucketContainer.bucketCount[key[0]] > minSupportCount):
            itemSetCount[tuple] = bucketContainer.bucketCount[key[0]]
            count += 1
    for keys in itemSetCount.keys():
        print(keys,itemSetCount[keys])
    print("Number of filtered Transactions : ",count)
    return itemSetCount

print("Tuple List")
tupleList = mapCustomers()
print("Total Number of Transactions : ",len(tupleList))

print("Actual Frequency of Transactions : ")
actualTransFreq = actualCount(tupleList)

print("Hash Based Bucket Count : ")
bucketContainer = hashBasedBucketCount(tupleList)

print("Filtered transactions(On Basis of Bucket Count) : ")
filteredBucketTuples = filterOnBucketCount(tupleList,bucketContainer,50)


print("Filtered Transactions(On Basis of actual Frequency) : ")
actualCount = filterOnActualCount(filteredBucketTuples,actualTransFreq,0)
print(actualCount)