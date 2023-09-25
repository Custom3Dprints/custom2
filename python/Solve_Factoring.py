import math
#DOESN"T WORK

prompt = "15x**2 - 23x + 4" #(input("Enter equation: ")) #x**2 + 48x - 1024
split_prompt = prompt.split()
print(split_prompt)
"""for char in split_prompt:
    if char == "x**2":
        print("x²")
    elif "x" in char:
        print(char)
    elif char == "+" or "-":
        print(char)"""


class Factor:
    def __init__(self, prompt_n):
        self.prompt_n = prompt_n

    def FactorLis(self):
        divisorList = [x for x in list(range(1, self.prompt_n + 1)) if self.prompt_n % x == 0]
        return divisorList

    def midlis(self):
        factor = len(Factorlis) / 2
        return f"     {Factorlis[int(factor)]} * {Factorlis[int(factor) - 1]} = {self.prompt_n}"

Promptnum = Factor(int(split_prompt[-1]))
Factorlis = Promptnum.FactorLis()

midlis = Promptnum.midlis()
print(Factorlis, "\n", midlis)

class Factoring:
    def __init__(self, lis):
        self.lis = lis
        self.n = -1
        self.i = 0

    def factoring(self):
        if len(self.lis) % 2 == 0:
            for index in range(int(len(self.lis) / 2)):
                subtract = self.lis[self.n] - self.lis[self.i]
                addition = self.lis[self.n] + self.lis[self.i]
                print(f"\n{self.lis[self.n]} - {self.lis[self.i]} = {subtract}")
                print(f"{self.lis[self.n]} + {self.lis[self.i]} = {addition}")
                self.i += 1
                self.n -= 1
                if subtract or addition == int(split_prompt[2][:2]):
                    print(int(split_prompt[2][:2]))
        else:
            if self.lis[0] != "x**2":
                print(self.lis[0][0])
                for var in self.lis:
                    if var != self.lis[0] or "+" or "-":
                        for num in self.lis[2]:
                            if num != "x":
                                print(int(num) / self.lis[0][0])
                        
            for index in range(int((len(self.lis)/ 2) + 1)):
                subtract = self.lis[self.n] - self.lis[self.i]
                addition = self.lis[self.n] + self.lis[self.i]
                if index == int(len(self.lis) / 2):
                    print(f"{self.lis[self.i]} ** 2")
                else:
                    print(f"\n{self.lis[self.n]} - {self.lis[self.i]} = {subtract}")
                    print(f"{self.lis[self.n]} + {self.lis[self.i]} = {addition}")
                    
                    promptx = (int(split_prompt[2][:2]))

                    if subtract == promptx or addition == promptx:
                        print ("yayayay")
                        break
                    self.i += 1
                    self.n -= 1

var = Factoring(Factorlis)
check = var.factoring()


