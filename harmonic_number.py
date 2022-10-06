# Program for harmonic number

def harmonic_num():
    num = 0
    n = int(input("Enter a number"))
    for x in range(1, n + 1):
        print(f'1/{x}')
        # print(1/x)
        num = num + (1 / x)
    print("Sum of Series upto terms", n, "is", num)


harmonic_num()
