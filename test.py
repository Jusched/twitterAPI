import bcrypt

passw = "123456789"

passw = passw.encode("utf-8")
salt = bcrypt.gensalt()
hashpass = bcrypt.hashpw(passw, salt)

print(hashpass)