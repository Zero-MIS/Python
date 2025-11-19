username=input("Masukkan username: ")
email=input("Masukkan email: ")
pw=input("Masukkan Password: ")
hasil={email : pw}

file=open(username + ".txt", mode='w',)
for key in hasil:
    user=key
    password=hasil[key]
    print(f"username: {username}", file=file)
    print(f"Email: {user}", file=file)
    print(f"password: {password}", file=file)
file.close()
print("Your account has been added!")
