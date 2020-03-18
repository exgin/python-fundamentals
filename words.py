def print_letters(word):
    """Accepts a word and prints each letter of it, returns uppercase"""

    for char in word:
        print(char.upper())


print_letters('hello')

print('--------------------------------------------')


def print_letters_with_e(word):
    """Accepts a word and prints each letter of it, only with e."""

    first_char = word[0]
    for char in word:
        if first_char == 'e' or first_char == 'E':
            print(char)
        else:
            print(f'{word} doesn\'t start with an e')


print_letters_with_e('Ello')


print('--------------------------------------------')


def print_upper_words(words, start_with):
    """Accpets a list of words & only prints the ones that start with {start_with}"""

    for word in words:
        first_char = word[0]
        if first_char == start_with:
            print(word)


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                  'y')
