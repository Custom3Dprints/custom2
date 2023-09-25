def myfunc(n):
  return lambda a : a * n

# defines a
mydoubler = myfunc(2)
mytripler = myfunc(3)

# defines n
print(mydoubler(11)) # 2 * 11
print(mytripler(11)) # 3 * 11


# Example 2
(lambda x: x + 1)(2)


# Example 3
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('guido', 'van rossum'))