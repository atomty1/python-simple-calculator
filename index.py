def calculator():
    print("Calculator")
    user_operation = input("1. + 2. - 3. * 4. /: ")
    if(user_operation == "1"):
        addition()
    elif(user_operation == "2"):
        subtraction()
    elif(user_operation == "3"):
        multiplication()
    elif(user_operation == "4"):
        division()

def addition():
    first_num = float(input("Enter the first number: "))
    second_num = float(input("Enter the second number: "))
    result = first_num + second_num
    print(f"{first_num} + {second_num} = {result}")

def subtraction():
    first_num = float(input("Enter the first number: "))
    second_num = float(input("Enter the second number: "))
    result = first_num - second_num
    print(f"{first_num} - {second_num} = {result}")

def multiplication():
    first_num = float(input("Enter the first number: "))
    second_num = float(input("Enter the second number: "))
    result = first_num * second_num
    print(f"{first_num} * {second_num} = {result}")

def division():
    first_num = float(input("Enter the first number: "))
    second_num = float(input("Enter the second number: "))
    result = first_num / second_num
    print(f"{first_num} / {second_num} = {result}")

calculator()