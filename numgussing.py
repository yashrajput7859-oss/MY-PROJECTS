
e_shubh = "shubham"
i = 0
while i != e_shubh:
    i = int(input("Enter your guess: "))
    if i < e_shubh:
        print("Too low!")
    elif i > e_shubh:
        print("Too high!")
    else:
        print("Congratulations! You've guessed the number.")