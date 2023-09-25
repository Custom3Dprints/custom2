import random
def random_word():
    with open('Dict_words.txt', 'r') as file:
        line = file.readlines()
        words = [w.strip() for w in line]
        random_index = random.randint(0, len(words)-1)
    return words[random_index]

def get_guess():
    used_letters = []
    word = random_word()
    dash = ["-"]*len(word)
    print(f"You have 6 guesses left")
    for count in range(1,7):
        var = ("".join(dash))
        if var == word:
            return(f"\nYou guessed right!! the word was: {var}")
        else:
            print(var)
            letter = input("Enter best guess: ").upper()
            while letter in used_letters:
                letter = input("Enter another guess: ").upper()
            else:
                for i,l in enumerate(word):
                    if l == letter:
                        dash[i] = letter
                count += 1
                used_letters.append(letter)
                print(f"\nYou have {7-count} guesses left")
    return(var)

def play():
    guess = get_guess()
    print(guess)
    if "-" in guess:
        print("Better luck next time")
play()

while True:
    try_again = input("Would you like to play again (y/n)?")
    if try_again == "y":
        play()
    else:
        break

    
