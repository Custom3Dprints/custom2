class Factor:
    def __init__(self, num):
        self.num = num

    def FactorLis(self):
        divisorList = [x for x in list(range(1, self.num + 1)) if self.num % x == 0]
        return (divisorList)

    def midlis(self):
        divisorList =  Factor(self.num).FactorLis()
        factor = len(divisorList) / 2
        return f"     {divisorList[int(factor)]} * {divisorList[int(factor) - 1]} = {self.num}"

    def formatted_factors(self):
        divisorList =  Factor(self.num).FactorLis()
        if len(divisorList) % 2 == 0:
            for i in range(int(len(divisorList)/2)):
                print(divisorList[i], divisorList[-(i+1)])
        else:
            for i in range(int(len(divisorList)/2)+1):
                print(divisorList[i], divisorList[-(i+1)])

Factor(int(input("Enter a num: "))).formatted_factors()
