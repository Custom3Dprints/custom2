plays = []
def True_iput():
    value = False
    while value == False:
        try:
            play = int(input(f"Enter a number 1-9: "))
            if play in range(1, 10) and play not in plays:
                plays.append(play)
                value = True
                return play
            else:
                value = False
        except ValueError:
            value = False


print(True_iput())