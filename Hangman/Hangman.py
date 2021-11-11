import random

tries = 8


def get_word():
    words = ['python', 'java', 'javascript', 'php']
    return random.choice(words).upper()


word = get_word()
word_letter = list(word)


def check(words, guesses, guess):
    global tries
    status = ''
    match = 0
    for letter in words:
        if letter in guesses:
            status += letter
        else:
            status += "*"

        if letter == guess:
            match += 1
    if match > 1:
        print('you have guessed ', match, 'letter truly "' + guess + '"' + '\'s')

    elif match == 1:
        print('you have guessed 1 letter truly')

    else:
        print('Entered input does not exist in the word ')
    return status


def main():
    global tries
    # print word_letter
    num_of_guess = 0
    guesses = []
    guessed = False
    test = '*' * len(word_letter)
    print('HANGMAN The game will be available soon. the word is \"', test, '\" and it has ', len(word_letter), )
    while not guessed:
        if tries == 0:
            print('You lost!')
            print(f'Word: {word}')

            break
        guess = input('please input your letter or word  ')
        guess = guess.upper()
        if len(guess) == 1 or len(guess) == len(word_letter):
            print(tries)

        elif len(guess) == len(word):
            guesses.append(guess)
            if guess == word:
                guessed = True

            else:
                num_of_guess += 1
        if guess in guesses:
            print('you already guessed ', guess)
            tries -= 1
            print(tries)
        elif len(guess) == len(word):
            guesses.append(guess)
            if guess == word:
                guessed = True

            else:
                print('You should enter only 1 letter or a word')
        elif len(guess) == 1:
            guesses.append(guess)
            result = check(word, guesses, guess)
            if '*' not in result:
                guessed = True
            else:
                print(result)
            if tries > 0 and '*' not in result:
                print('You survived! this word: ', word, ':) in ', num_of_guess, 'steps')
    else:
        print('you should enter only 1 letter or a word with length? ', len(word_letter), ' please enter again')


def start():
    choice = int(input("Hi! Type 1 to play the game, 2 to quit:").lower())
    if choice == 1:
        main()
    elif choice == 2:
        print("Exit")


start()
