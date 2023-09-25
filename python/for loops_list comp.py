names_Bday ={
"Marjorie":"July 8,2006",
"Dulce":"September 4,2005", 
"Julia":"June 2, 2006"
}
bday = []
def whoseBirthdayThisMonth(x):
    for n in names_Bday:
        if x in names_Bday[n]:
            bday.append(n)
    return bday

#print(whoseBirthdayThisMonth("July"))

# OR
names_Bday ={
"Marjorie":"July 8,2006",
"Dulce":"September 4,2005", 
"Julia":"June 2, 2006"
}

I = input("Enter DOB: ")
def whoseBirthdayThisMonth(x):
    a = [I for I in names_Bday if x in names_Bday[I]]
    return a
print(whoseBirthdayThisMonth(I))

# [cat for cat in Cat_lists if Cat_input in cat ]

even_num = [x + x for x in range(4)]
print(even_num)