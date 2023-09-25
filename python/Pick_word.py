dict = {}
with open('nameslist.txt', 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        if line in dict:
            dict[line] += 1
        else:
            dict[line] = 1
        line = file.readline()
print(dict)