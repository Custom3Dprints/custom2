import math
from character_type_class import int_float
from squareroot_class import Factor
from squareroot_class import Squareroot
from fraction_simplifier_class import fraction
from fraction_simplifier_class import simplifier

a = int(input("Enter a: "))#float
b = int(input("Enter b: "))#float
c = int(input("Enter c: "))#float
denominator = 2 * a
InSqrt = (b**2) - (4 * a * c)

if InSqrt < 0:
  InSqrt = InSqrt * -1

formula = (f"\n{-b}±√{b}² {-4} * {a} * {c}\n    {2} * {a}")
print(formula)


char_type = (int_float(math.sqrt(InSqrt)).int_float()) #checks if number has perfect sqrt
factors = Factor(InSqrt).char_type_sqrt()
Sqrt_ans = Squareroot(factors, InSqrt).answer()
if char_type == "float":
  print((f"\n {-b}±√{b**2} + {-4 * a * c}\n    {denominator}"))
  print((f"\n  {-b}±√{InSqrt}\n    {denominator}"))
  if Sqrt_ans == None:
    print(f"a\n{-b} + √{factors[0]}  |  {-b} - √{factors[0]}\n    {denominator}    |     {denominator}")
  else:
    print(f"b\n{-b} {Sqrt_ans[5:]}  |  {-b} {Sqrt_ans[5:]}\n    {denominator}    |     {denominator}")
  
else:
  print((f"c\n {-b}±√{b**2}{-4 * a * c}\n    {denominator}"))
  print((f"d\n  {-b}±√{InSqrt}\n    {denominator}"))
  print(f"e\n{-b} + {Sqrt_ans[5:]}  |  {-b} - {Sqrt_ans[5:]}\n    {denominator}    |     {denominator}")
  positive = (f"{-b + int(Sqrt_ans[5:])}/{denominator}") #4/2
  negative = (f"{-b - int(Sqrt_ans[5:])}/{denominator}")

  pos_ans = fraction(positive).nums() #(4,2)
  pos_fraction = simplifier((pos_ans)[0], (pos_ans)[1]).simplify()

  neg_ans = fraction(negative).nums() #(4,2)
  neg_fraction = simplifier((neg_ans)[0], (neg_ans)[1]).simplify()

  print(f"\n{positive}\n ↓ \n{pos_fraction}")
  print(f"\n{negative}\n ↓ \n{neg_fraction}")
