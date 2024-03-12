from pymongo import MongoClient, DESCENDING

#Connecting to MongoDB
client = MongoClient("localhost", 27017)
db = client["users-db"]
users = db["users-collection"]


#Receives the Username and Email from user.py and insert them in the users-collection
def create_user(username: str, email: str):

    if check_exist(email) is None:
        data = {"id": new_id(), "username": username, "email": email}
        users.insert_one(data)
        return {'response': 'User Created Successufully', 'data': data, 'status': True}

    return {'response': 'Email Already in use', 'data': '', 'status': False}

#Finds the specified email in the collection if not, return None
def check_exist(email: str):
    user = users.find_one({'email': email})
    return user

#Gets the max ID from the collection plus one
def new_id():
    try:
        new_id = users.find().sort('id', DESCENDING).limit(1)
        new_id = new_id[0]['id'] + 1
        return new_id
    except:
        new_id = 1
        return new_id

def delete_user(email: str):
    user = users.find_one_and_delete({"email": email})
    return user

def get_users():
    all_users = []
    for user in users.find():
        all_users.append(user)

    return all_users


