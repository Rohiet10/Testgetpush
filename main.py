import pymongo
client = pymongo.MongoClient("mongodb+srv://Aarohiet:Aashi2022@cluster0.w2rx1.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d={"name":"sudhanshu",
   "emailid":"sidhanshu@ineuron.com",
"surname":"kumar"
}
db1=client['mongotest']
coll=db['test']
coll.insert_one(d)