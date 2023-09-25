def valid_file():
    try:
        file = open("periodicTable.txt", "r")
        return file
    except FileNotFoundError:
        return False

def Valid():
    file = valid_file()
    lines = file.readlines()
    line = [char.strip() for char in lines]
    print(line)
    strings = []
    numbers = []
    strchar = ''
    num = 0
    for i, a in enumerate(line):
        #print(a)
        for b in a:
            try:
                numbers.append(int(b))
            except ValueError:
                strchar += str(b)
            strings.append(strchar)
    print(strings)
    print(numbers)

def output():
    while valid_file() == False:
        valid_file()
    else:
        Valid()

output()