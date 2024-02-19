def print_upper_words(words, letters):
    """Accepts a list of words and set of letters and prints each word
    that starts with any of the letters within the set"""

    for word in words:
        for letter in letters:
            if word.startswith(letter):
                print(word)

print_upper_words(
    ['hello', 'world', 'everyone', 'Elephant'],
    {'w', 'E'}
)