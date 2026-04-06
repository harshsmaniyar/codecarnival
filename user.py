correct_username = "Harsh"
correct_password = "12345678"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Login Failed")
