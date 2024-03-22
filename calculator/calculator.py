while True:
    print("Select an operation to perform: ")
    print("1. ADD ")
    print("2. SUBTRACT ")
    print("3. MULTIPLY ")
    print("4. DIVIDE ")
    print("5. SQUIRE ")
    print("6. EXIT ")

    operation = int(input())

    if operation == 1:
        num1 = int(input("First Number: "))
        num2 = int(input("Second Number: "))
        print("Result is " + str(num1 + num2))
    elif operation == 2:
        num1 = int(input("First Number: "))
        num2 = int(input("Second Number: "))
        print("Result is " + str(num1 - num2))
    elif operation == 3:
        num1 = int(input("First Number: "))
        num2 = int(input("Second Number: "))
        print("Result is " + str(num1 * num2))
    elif operation == 4:
        num1 = int(input("First Number: "))
        num2 = int(input("Second Number: "))
        print("Result is " + str(num1 / num2))
    elif operation == 5:
        num = int(input("Enter Number: "))
        print("Squire is " + str(num**2))
    elif operation == 6:
        break;
    else:
        print("Invalid Number")