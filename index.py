name =input("enter your Name")
passw = input("enter the password")
password = "shubham#1234"
while password != passw and name != "shubham":
    passw = input("Password not match please enter valid password:")
    name =input("name not match please enter your valid Name")
    if password == passw and name == "shubham":
        print ("you are in right selection")
        print("you are logged in welcome", name)
    else:
        print("we are not recognizing you try again...!")