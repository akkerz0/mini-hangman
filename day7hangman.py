import re, random 

wordlist = ["anwar", "pizza", "apple", "pear", "orange"] # Predefined wordlist
gameover = False # Used to check for win condition
live = 6

word = random.choice(wordlist)
wordsplitted = list(word)

letters_guessed = []
new_word = []

for _ in range(0, len(word)):
    new_word.append("_")

print(new_word)
print(f"Your word has {len(new_word)} letters.")
        
def lettercheck1(letterinput):
    global live; 
    letterfound = False
    for i, letter in enumerate(wordsplitted):
        if letterinput == letter:
            new_word[i] = letterinput
            letterfound = True
            print("\nYou guessed correctly!\n")
    if letterfound == False:
        print("You have guessed incorrectly.")
        live -= 1


while gameover == False:
    letterinput = input("\nInput a letter you would like to guess: ")
    letterinput = letterinput.lower()
    letters_guessed.append(letterinput)

    if letterinput in new_word:
        print("You have already guessed this letter, try again...")
    else:
        lettercheck1(letterinput)
        print(new_word)
        print(f"You have {live} lives remaining.")
        print(f"These are the letters you have already guessed: {(", ".join(letters_guessed))}")

    if live == 0:
        print("You have run out of lives. Game over.")
        gameover = True

    if wordsplitted == new_word:
        print("You have finished the word!")
        gameover = True








