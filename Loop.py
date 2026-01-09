shubham = (3,6,9,12,15,18,21,24,27,30)
x =int(input("Enter a number to search in tuple: "))
i = 0
while i < len(shubham):
    if shubham[i]==x:
        print ("found at index", i)
        break
    i = i + 1

