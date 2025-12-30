import math

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
choice = input("Choose operation (ADD, SUB, MULT, DIV, MOD, SQRT, REM): ")

if choice == "ADD":
    print("The sum is:", n1 + n2)

elif choice == "SUB":
    print("The difference is:", n1 - n2)

elif choice == "MULT":
    print("The product is:", n1 * n2)

elif choice == "DIV":
    if n2 != 0:
        print("The quotient is:", n1 / n2)
    def get_number(prompt):
        while True:
            s = input(prompt).strip()
            try:
                return float(s)
            except ValueError:
                print("Invalid number, please try again.")

    def main():
        n1 = get_number("Enter the first number: ")
        n2 = get_number("Enter the second number: ")
        choice = input("Choose operation (ADD, SUB, MULT, DIV, MOD, SQRT, REM): ").strip().upper()

        if choice == "ADD":
            print("The sum is:", n1 + n2)
        elif choice == "SUB":
            print("The difference is:", n1 - n2)
        elif choice == "MULT":
            print("The product is:", n1 * n2)
        elif choice == "DIV":
            if n2 == 0:
                print("Error: Division by zero.")
            else:
                print("The quotient is:", n1 / n2)
        elif choice == "MOD":
            if n2 == 0:
                print("Error: Modulus by zero.")
            else:
                print("The modulus is:", n1 % n2)
        elif choice == "SQRT":
            if n1 >= 0:
                print("The square root of", n1, "is:", math.sqrt(n1))
            else:
                print("Cannot compute square root of negative number:", n1)
            if n2 >= 0:
                print("The square root of", n2, "is:", math.sqrt(n2))
            else:
                print("Cannot compute square root of negative number:", n2)
        elif choice == "REM":
            if n2 == 0:
                print("Error: Division by zero.")
            else:
                print("Integer division (floor) of", n1, "by", n2, "is:", n1 // n2)
        else:
            print("Invalid operation selected.")

    if __name__ == '__main__':
        main()
