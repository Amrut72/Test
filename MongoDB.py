import pymongo

client = pymongo.MongoClient("mongodb+srv://root:Amrut2599@amrutop.yg9fncw.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

D = {'Name' : "Amrut", 'Email ID': 'Amrut@gmail,com'}
db1 = client['mongotest']
coll=db1['test']
coll.insert_one(D)