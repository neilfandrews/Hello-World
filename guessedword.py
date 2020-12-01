word = 'cat'
wrongguesses = 0
wrongletters = []
# Starting point
a = len(word)
guessedword = ('_' * a)

# Making a list of guessedword
listword = list(guessedword)
print("\nWelcome to Hangman\n")
print(f"Your word has {a} letters and you have 6 guesses:\n")
print(listword,'\n')

def playerguess():
    guess = input('\nPlease guess a letter: \n')
    guess = guess.lower()
    return guess

# Main Game Loop
while (guessedword.replace(" ","") != word) and (wrongguesses < 6):

    #print(listword,'\n')
    print("Incorrect Letters: ", wrongletters)
    # Guess Evaluation Loop
    guess = playerguess()
    for num in range(0,a):

        if word[num] == guess:
            print('\nGood guess!\n')
            listword[num] = guess

    guessedword = ''.join(listword)
    print(listword,'\n')
    if guessedword == word:
        print (f"Congratulations, you win! The word was {word}\n")

    if guess not in word:
        wrongguesses += 1
        wrongletters.append(guess)
        print(f"Incorrect guess - you have {6-wrongguesses} left\n")
        if wrongguesses == 6:
            print (f"Sorry, you lose - the word was: {word}\n")
