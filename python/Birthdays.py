Birthdays = {}
with open("Birthdays.txt", "r") as file:
  line = file.readlines()
  bdays = [i.strip() for i in line]
  names = [n for i,n in enumerate(bdays) if i % 2 == 0]
  dates = [d for i, d in enumerate(bdays) if i % 2 != 0]
  for index in range(len(names)):
    name = names[index]
    Birthdays[name] = dates[index]

print(f"We know the birthdays of:")
[print(n) for n in names]

def Output():
  prompt = input("Who's name do you want to look up? ").capitalize()
  try:
    return Birthdays[prompt]
  except KeyError:
    return False

output = Output()
while output == False:
  try_again = input("Do you want to look up another birthday (y/n)? ")
  if try_again == "y":
    output = Output()
  else:
    break
else:
  print(output)
  while output != False: #re-prompts for another file
    try_again = input("Would you like to process another birthday (y/n)? ")
    if try_again == "y":
        output = Output() #calls function again
    else:
        break
