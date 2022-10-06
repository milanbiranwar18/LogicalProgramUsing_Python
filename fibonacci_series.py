# Program for fibonacci series
def fibonacci_series():
    num = int(input("Enter a number to calculate fibonacci series"))
    a = 0
    b = 1
    for i in range(1, num):
            c = a + b
            print(c)
            a = b
            b = c


fibonacci_series()