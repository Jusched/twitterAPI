users = [
    {
        "user_id": "6f9230a3-994d-43cc-8a8a-6b253cdb7fea",
        "email": "seba@betan.com",
        "first_name": "juan",
        "last_name": "betan",
        "birth_date": "2022-09-16",
        "password": "12345678"
    },
    {
        "user_id": "6f9230a3-994d-43cc-8a8a-6b253cdb7fea",
        "email": "asdadsad@adasdad.com",
        "first_name": "sdddd",
        "last_name": "string",
        "birth_date": "2022-09-16",
        "password": "stringst"
    }
]

x = input("Password. ")

for passw in range(len(users)):
    passw = users[passw]
    if passw["password"] == x:
        print(passw)
        break
    else:
        print("No user with this password. ")