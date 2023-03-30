def password():
    enteredPassword = input("what is the password?")

    if enteredPassword == "butterfly":
        print("ACCESS GRANTED")

    else:
        print("ACCESS DENIED")
    password()

password()