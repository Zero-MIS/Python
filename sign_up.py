login_or_signup = input("Login or Sign Up?: ")
if login_or_signup == str("login"):

    if login_or_signup.islower():
        username = input("username: ")
        pw = input("password: ")

        try:
            akun = open(username + ".txt")
            isi_akun = akun.read()
            akun.close()
            print("login berhasil!")
        except:
            print("Akun tidak terdaftar!")

elif login_or_signup == str("sign up"):

    if login_or_signup.islower():
        username = input("Masukkan username: ")
        email = input("Masukkan email: ")
        pw = input("Masukkan Password: ")
        required_email = "@gmail.com"
        hasil = {email: pw}

        if required_email in email:
            file = open(
                username + ".txt",
                mode="w",
            )
            for key in hasil:
                user = key
                password = hasil[key]
                print(f"username: {username}", file=file)
                print(f"Email: {user}", file=file)
                print(f"password: {password}", file=file)
            file.close()
            print("Your account has been added!")
        else:
            print("Invalid email!")
    else:
        print("please type in lowercase")
else:
    print("please type in lowercase")
