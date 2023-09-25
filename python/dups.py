#checks dups
def count_occurrences(word, character):
    sum = 0
    for char in word:
        if char == character:
            sum += 1
    return sum
#print(count_occurrences("banana", "a"))

#########################################################

a = [13, 44, 52, 1, 1, 2, 3, 5, 8, 13]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
lis = []
for i in a:
    for j in b:
        if i == j and i not in lis:
            lis.append(i)
lis.sort()
print(lis) #[1, 2, 3, 5, 8, 13]