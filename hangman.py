import random

def replay():  
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Hangman')


# a given list of words
word_list = ['develop','hungry','beach','tree']


while True:   

    random.shuffle(word_list)
    word_to_guess = list(word_list[0])

    print(word_to_guess)
    n = len(word_to_guess)

    # empty list of length of word_to_guess is taken
    display = []
    display.extend(word_to_guess)

    # already guessed letters
    guessed_letters = []
    guessed_letters.extend(display)
    
    # Add _ in display for each letter in word_to_guess
    for i in range(n):
        display[i] = '_'
        
    print(' '.join(display))
    print()
    
    count = 0
    
    while count < len(word_to_guess):

        guess = input("Please enter a letter: ")
        guess = guess.lower()
        print(count)

        for i in range(n):
            if word_to_guess[i] == guess and guess in guessed_letters:
                display[i] = guess
                count += 1

                guessed_letters.remove(guess)
        
        if guess not in display:
            print('Sorry, wrong guess')

        print(' '.join(display))
        print()
    
    print('Well done! You have guessed the word!')

    if not replay():
        break
