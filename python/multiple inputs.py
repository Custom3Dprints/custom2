x = 0
Y = int(input("How many dates are you entering? "))
all_bdays = {
    'Julia': 'June 4, 2006',
    'Gigi': 'July 11, 2006', 
    'Marjorie': 'July 8, 2006',
}
while x < Y:
    class birthday:
        def get_bday(self):
            return self.name, self.month, self.day, self.year
        def __init__(self, name, month, day, year):
            self.name = name
            self.month = month
            self.day = day
            self.year = year

    n, m, d, y = input("Enter Name, month/day/year: ").split()
    v = birthday(n, m, d, y).get_bday()

    #monthdayyear
    mdy = "{M} {D}, {Y}".format(M = m.capitalize(), D = d, Y = y)
    #print(mdy)

    #adding to dict
    all_bdays[n.capitalize()] = mdy
    x += 1

print(f"\n{all_bdays}")    #prints whole dict

Question = input("Whose birthday do you want to know? ")
if Question in all_bdays:
    print(f"{all_bdays[n]}\nDON'T FORGET TO COPY AND PASTE DICT")
elif Question == "no" or "no one" or "nobody":
    print("DON'T FORGET TO COPY AND PASTE DICT")
else:
    print("dumdass you spelled something wrong again 🙄")
