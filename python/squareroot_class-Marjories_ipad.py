import math
#from Prompt_class import prompt

class Factor: # returns list of factors
    def __init__(self, num):
        self.num = num
        self.factor_lis = []

    def char_type_sqrt(self):
        from character_type_class import int_float
        char_type = int_float(math.sqrt(self.num)).int_float() #checks if perfect sqrt

        if char_type == "int": #if perfect sqrt
            sqrt = int(math.sqrt(self.num))
            return sqrt 
        elif char_type == "float": #if not perfect sqrt
            factors = [number for number in list(range(1, self.num+1)) if self.num % number == 0]
            self.factor_lis.extend(factors)
            self.factor_lis.reverse()
            return self.factor_lis #retrun list of factors
        else:
            return "ERROR" #if shit hits the fan

class Squareroot: # returns simpliest form of sqrt from int
    def __init__(self, Sqrt, input):
        self.Sqrt = Sqrt
        self.input = input
    def answer(self):
        if type(self.Sqrt) == int:
            return(f"ans: {self.Sqrt}")
        else:
            for index, value in enumerate(self.Sqrt):
                if self.input % value**2 == 0 and value != 1:
                    return((f"ans: {value}√{int(self.input/value**2)}"))

                elif len(self.Sqrt) == 2:
                    #print(f"{self.input} = {round(math.sqrt(self.input), 2)}")
                    return (f"ans: √{self.input}")


InSqrt = 63+48
factors = Factor(InSqrt).char_type_sqrt()
print(factors)
Sqrt_ans = Squareroot(factors, InSqrt).answer()
#print(Sqrt_ans)
