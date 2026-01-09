correct_name = "shubham"
correct_pass = "shubham#1234"

while True:
    name = input("Enter your Name: ")
    passw = input("Enter the password: ")
    if name == correct_name and passw == correct_pass:
        print("You are in the right selection")
        print(f"You are logged in! Welcome, {name}.")
        break
    else:
        print("We are not recognizing you. Please try again...!")
