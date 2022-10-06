#Program for prime number

def prime_num():
    first = int(input("Enter a number from where you wanna start to check that it's prime or not"))
    last = int(input("Enter a number till you wanna check that it's prime or not"))
    for i in range(first, last + 1):
        num = 0
        for j in range(2, i):
            if (i % j == 0):
                num = 1
                break
        if (num == 0):
            print(i)

prime_num()