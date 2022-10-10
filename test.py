import bcrypt

passw = "123456789"

passw = passw.encode("utf-8")
salt = bcrypt.gensalt()
hashpass = bcrypt.hashpw(passw, salt)

#print(hashpass)

passwd = input()
passwd = passwd.encode("utf-8")
if bcrypt.checkpw(passwd, hashpass):
    print("Yes")
else:
    print("No")