Opperation_list = ["Addition", "Subtraction", "Multiplication", "Division"]

Opp_dict = {Opperation_list[0]: "Addition", "Subtraction": Opperation_list[1]}
print(Opp_dict[Opperation_list[0]])
print(Opp_dict["Subtraction"])


def Addition():
  num1 = float(input("Number one: "))
  num2 = float(input("Number two: "))
  result = num1 + num2
  print(result)
def Subtraction():
  num1 = float(input("Number one: "))
  num2 = float(input("Number two: "))
  result = num1 - num2
  print(result)
def Multiplication():
  num1 = float(input("Number one: "))
  num2 = float(input("Number two: "))
  result = num1 * num2
  print(result)
def Division():
  num1 = float(input("Number one: "))
  num2 = float(input("Number two: "))
  result = num1 / num2
  print(result)


while True:
  print(f"1. {Opperation_list[0]}")
  print(f"2. {Opperation_list[1]}")
  print(f"3. {Opperation_list[2]}")
  print(f"4. {Opperation_list[3]}")
  opperation_Question = input("What operation do you want to perform?: ")
  opp_list = [opp for opp in Opperation_list if opperation_Question in opp]
  print(opp_list)

  if len(opp_list) == 1:
    if opperation_Question in Opperation_list[0]:
      Addition()
    
    elif opperation_Question in Opperation_list[1]:
      Subtraction()
      
    elif opperation_Question in Opperation_list[2]:
      Multiplication()
      
    elif opperation_Question in Opperation_list[3]:
      Division()
    break
  
  elif len(opp_list) > 1:
    Join = ' or '.join(opp_list)
    opperation_Question = (f"Do you want to do {Join}? ")
    opperation_Question = opperation_Question.capitalize()
    print(opperation_Question)

    #if opperation_Question in Opperation_list:
      