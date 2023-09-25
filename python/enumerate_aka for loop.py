"""     Ex: 1
# enumerate function
l1 = ["eat","sleep","repeat", 123]
s1 = "geek"
 
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
 
print ("Return type:",type(obj1))

# [(index #, 'value')]
print(list(enumerate(l1)))

#changes the index start #
# changing start index to 2 instead of 0
print(list(enumerate(s1,0)))
"""

"""     Ex: 2
days = { 'Mon', 'Tue', 'Wed','Thu'}
enum_days = enumerate(days)

print(enumerate(days))

# enumearte using loop
for enum_days in enumerate(days):
    print(enum_days)

for count,enum_days in enumerate(days,5):
   print(count,enum_days)

"""


my_l = ["apple", "pear", "oranges", "mango"]

for x, element in enumerate(my_l):
    #print(x, element)
    if x == 1:
        print(my_l[1])