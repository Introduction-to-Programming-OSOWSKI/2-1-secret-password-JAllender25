def password(p):
    p = input("what is the password?")

    if p == "Knights19":
        print("ACCESS GRANTED")

    else:
        print("ACCESS DENIED")
    password()

password()