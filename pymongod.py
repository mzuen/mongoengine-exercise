from pymongo import MongoClient, WriteConcern


# client = MongoClient(host="mongodb://localhost:27017/")

client = MongoClient(
    "mongodb+srv://jpy:FK23sChtUnKCVY8y@pymongodb.xoete.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)

db = client.pymongo

print("LIST OF COLLECTION:", db.list_collection_names())
User = db.user


jamie = {"name": "jamie", "age": 25}
jason = {"name": "jason", "age": 19}

User.insert_one(jamie).inserted_id
User.insert_one(jason).inserted_id


molly = {"name": "molly", "age": 14}
kathy = {"name": "kathy", "age": 21}

res = User.insert_many([molly, jamie, kathy, jason])
res.inserted_ids

for user in User.find():
    print(user)
