# Standard Form
opperations = ["add", "sub"]
opp = input("add or sub? ")
x = int(input("Enter x: "))
y = int(input("Enter y: "))
equal = int(input("Enter =  "))
opp_dict = {"add": "+", "sub": "-"}
#   2x - y = -7
if opp not in opperations:
    print("Try again") 
"""elif y == 0:
    print(f"{x}x {opp_dict[opp]} y = {equal}")

    print(f"step1 = -y = {equal} - {x}x")"""