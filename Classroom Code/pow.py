def raise_to_pow(base, pow):
        result = 1
        for i in range(pow): #i = 0-2
            result = result * base
        return result    
print(raise_to_pow(int(input("Enter base number: ")), int(input("Enter to what power: "))))