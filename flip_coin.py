import random

def flip_coin():
    headCount = 0
    tailcount = 0
    headpercentage = 0
    tailpercentage = 0
    flips = int(input("Enter the number of flips"))
    for i in range(flips):
        # num=int(input("Enter 1 for Tail or 2 for Head"))
        num = random.randint(1, 2)
        if num == 1:
            print("Tail")
            tailcount = tailcount + 1
        else:
            print("Head")
            headCount = headCount + 1

    headpercentage = (headCount * 100) / flips
    tailpercentage = (tailcount * 100) / flips

    print("HeadPercentage is ", headpercentage)
    print("TailPercentage is ", tailpercentage)


flip_coin()
