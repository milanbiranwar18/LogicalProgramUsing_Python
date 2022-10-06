# Program for larger number

def larger_num():
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))
    num3 = int(input("Enter third number"))
    if num1 > num2:
        print(num1, "is larger")
    elif num2 > num3:
        print(num2, "is larger")
    else:
        print(num3, "is larger")



larger_num()