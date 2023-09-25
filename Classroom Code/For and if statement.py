Random_things = ["Apple", "pear", "oranges", "bananas", "pina", "Sage"]

search = input("what are you looking for? ")
found = [item for item in Random_things if search in item]
print(f"\nline 5\n{found}\n")

for var in Random_things:
  if search in var:
    print(var)

#these are the same except that line 5 will print all on 1 line and the other will print on new line each time

