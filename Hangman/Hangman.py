import random
from my_list import my_list

def get_valid_word(my_list):
    word = random.choice(my_list)
    while '-' in word or ' ' in word:
        word = random.choice(my_list)

        return word.upper()
print('HANGMAN')
print('The game will be available soon')
my_list = ['Python', 'java', 'javascript']

a = 'python'
print ('Введите слово!')
b = str(input())
if b == a:
    print('Вы выжили!')
else:
    print('Вы погибли!')