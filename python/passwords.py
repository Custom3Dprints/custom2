PW = {
    "gmail": "Marjoriemiddle12",
    "nike": "Marjorie12", 
    'fusion360': 'Marjorie12!', 
    'phone': '131181',
    'computer':'131181',
    'phone binary': '', 
    "Broward dual enrollment": 'Dulce12!'
    }

print(PW)

Question = input("What do you want to do with (Add or Find)? ")

if Question.capitalize() == "Find":
    key = PW.keys()
    print(f"Find a password from:\n    {', '.join(key)}")
    PW_i = input("What password are you looking for? ")
    if PW_i.lower() in key:
        print(f"\n Password = {PW[PW_i]}")
    else:
        print("else")
        lc = [v for v in PW if PW_i.lower() in v]
        lc = ("".join(lc))
        print(f"\n{PW_i.capitalize()} = {PW[lc]}")
elif Question.capitalize() == "Add":
    add_num = int(input("how many passwords do you want to add? "))
    x = 0
    while x < add_num:
        k,v = input("Enter Website Name and Password with 1 space inbetween: ").split()
        PW.update({k:v})
        x += 1
    print(PW)
else:
    print("something went wrong 😡😭😕")