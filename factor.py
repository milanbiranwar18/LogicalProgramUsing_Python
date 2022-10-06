def factors():
    num = int(input("Enter a number to check it's factor"))
    num1 = int(input("Enter range till which number you want factor"))
    for i in range(1, num1):
        if num % i == 0:
            print(i)

factors()
