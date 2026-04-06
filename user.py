actual_username = "Harsh"
actual_password = "12345678"

username = input("Enter username: ")
password = input("Enter password: ")

if username == actual_username and password == actual_password:
    print("Login Successful")
else:
    print("Login Failed")
