users = []

def create_user(username: str, email: str):

    last_id = len(users)+1 
    data = {"id": f"{last_id}", "username": f"{username}", "email": f"{email}"}
    response = str('Email already in use')
    if check_exists(email) is False:
        users.append(data)
        response = str('User created successfully')
    return response

def check_exists(email: str):

    all_emails = []
    for user in users:
        all_emails.append(user['email'])
    if email in all_emails:
        return True
    elif len(all_emails) == 0:
        return False
    return False

def delete_user(id: int):
    users.pop(id-1)