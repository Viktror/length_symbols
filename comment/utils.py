def count_letters(word):
    vowels = 0
    consonants = 0
    for letter in word:
        if letter.isalpha():
            if letter.lower() in 'aeiouy':
                vowels += 1
            if letter.lower() in 'bcdfghjklmnpqrstvwxyz':
                consonants += 1

    return (vowels, consonants)
