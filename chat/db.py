obj = {
    "user":"zkzk",
    "message":"lol",
    "servermessage":"ppp"
}


import json

def readDB(filename = "chat/db.json"):
    with open(filename , mode="r") as jsonFile:
        data = json.load(jsonFile)
        
    return data

def writeDB(obj ,filename = "chat/db.json" ):
    with open(filename , mode="r") as jsonFile:
        data = json.load(jsonFile)
        temp = data["database"]["msg"]
        temp.append(obj)

    with open(filename , mode="w") as jsonFile:
        json.dump(data , jsonFile)

# writeDB(obj=obj)


