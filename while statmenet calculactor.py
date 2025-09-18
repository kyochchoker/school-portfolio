while True:
    try:
        x = int(input("Put your 1st number: "))
        y = int(input("Put your 2nd number: "))
        z = int(input("Put your 3rd number: "))


        operator = input("Choose what operator to use (+, -, * , /): ")
        if operator == '+':
            result = x + y + z
        elif operator == '-':
            result = x - y - z
        elif operator == '*':
            result = x * y * z
        elif operator == '/':
            if x == 0 or y == 0 or z == 0:
                print("You cannot divide a number with 0.")
                result = None
            else: 
             result = x / y / z
        else:
            print("INVALID OPERATOR")
            if operator == "":
             operator = input("Please input a operator: ")
            continue

        print(f"The result is {result}")
        break


    except ValueError:
        print("Invalid Numerical value.Try again.")