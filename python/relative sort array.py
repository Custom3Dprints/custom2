arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
array = []
arr1.sort()

"""
for arr2[0] in arr1:
    if arr2[0] == 2:
        array.append(arr2[0])
for arr2[1] in arr1:
    if arr2[1] == 1:
        array.append(arr2[1])
for arr2[2] in arr1:
    if arr2[2] == 4:
        array.append(arr2[2])
for arr2[3] in arr1:
    if arr2[3] == 3:
        array.append(arr2[3])
for arr2[4] in arr1:
    if arr2[4] == 9:
        array.append(arr2[4])
for arr2[5] in arr1:
    if arr2[5] == 6:
        array.append(arr2[5])
"""
for i in range(0, len(arr2)):
    for x in arr1:
        if x == arr2[i]:
            array.append(arr2[i])
            
def array_without_dups(x):
    return list(dict.fromkeys(x))
print(array_without_dups(array))

def array_without_dups(x):
    return list(dict.fromkeys(x))
print(array_without_dups(array))

arr1_after = [item for item in arr1 if item not in array]   #arr1_after = list(set(arr1) - set(array)) #arr1_after.sort()
array.extend(arr1_after)

print(array)