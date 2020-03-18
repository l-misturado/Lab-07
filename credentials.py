username = input("Hello! Please enter your first name: ")
password = input("Please enter your password: ")

if(username.lower() == "logan" and password == "badpassword"):
    print("Welcome to facebook!")
else:
    print("Wrong credentials, try again!")
