import string

# alphabet list
alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)
#print(alphabet_list)

#Input = list(input("what is your name? ").lower())
Input = input("Enter name: ").lower()
#list of the names
"""name_dict = [
	{
		"name": "Dulce",	
		"PW": "Harry"
	},
	{
		"name": "JUlia",
		"PW": "1234"
	},
	{
		"name": "marjorie",
		"PW": "Marjorie12"
	}
]"""

name_dict = ["marjoire", "julia", "dulce", "dan", "todd"]
print(name_dict)
print(Input[0])
"""for Input[0] in name_dict:
	print(f"\n{Input}\n")"""

#def whoseBirthdayThisMonth(name):
a = [v for v in name_dict if Input in v]
print(a)
print(",".join(a))
#print(whoseBirthdayThisMonth(Input))
