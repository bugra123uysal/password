while True:
    
    password = input("Please enter a password between 5 and 10 characters: ")

    if password == 'cancel':
        break
    
    elif not password:
        print("Do not leave it blank.")

    elif len(password) > 10 or len(password) < 5:
        print("Please create a password between 5 and 10 characters.")

    else:
        print("Password successfully created.")
