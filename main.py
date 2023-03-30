def password():
    enteredPassword = input("what is the password?")

    if enteredPassword == "Knights19":
        print("ACCESS GRANTED")

    else:
        print("ACCESS DENIED")
    password()

password()