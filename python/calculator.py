Opperation_list = ["+", "-", "*", "/", "**"]

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

# returnedCats = [cat for cat in Cat_lists if Cat_input in cat ]


while True:
  Join = "\n"+"  ,   ".join(Opperation_list)
  print(Join)
  """print(f"1. {Opperation_list[0]}")
  print(f"2. {Opperation_list[1]}")
  print(f"3. {Opperation_list[2]}")
  print(f"4. {Opperation_list[3]}")"""
  opperation_Question = input("What operation do you want to perform?: ")


  if opperation_Question not in Opperation_list:
    print("invalid input")
  else: 
    if opperation_Question in Opperation_list[0]:
      answer = Addition()
      print(answer)
    elif opperation_Question in Opperation_list[1]:
      Subtraction()
    elif opperation_Question in Opperation_list[2]:
      Multiplication()
    elif opperation_Question in Opperation_list[3]:
      Division()
    
    """Yes_no_list = ["YES", "Yes", "yes", "Y", "y", "NO", "No", "no", "N", "n"]
    Q = input("Do you want to do something else? ")
    if Q in Yes_no_list[0:4]:
      opperation_Question = input("What operation do you want to perform?: ")
      if opperation_Question in Opperation_list[0]:
        answer = Addition()
        print(answer)
      elif opperation_Question in Opperation_list[1]:
        Subtraction()
      elif opperation_Question in Opperation_list[2]:
        Multiplication()
      elif opperation_Question in Opperation_list[3]:
        Division()
    else:
      print(Yes_no_list[5:9])"""