import random
i = 0
n = 0
while i < 3:
    flips = []
    i += 1
    while n < 200:
        num = random.randint(1, 2)
        if num == 1:
            #print("Heads")
            flips.append("Heads")
        elif (num == 2):
            #print("Tails")
            flips.append("Tails")
        n += 1
    print(flips)
