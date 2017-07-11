# translates words into pig latin

def translate(word):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    if word[0] not in vowels and word[1] not in vowels and word[2] not in vowels:
        word = word[3:] + '-' + word[:3] + 'ay'
    elif word[0] not in vowels and word[1] not in vowels:
        word = word[2:] + '-' + word[0:2] + 'ay'
    elif word[0] not in vowels:
        word = word[1:] + '-' + word[0] + 'ay'
    else:
        word += '-' + 'say'
    print(word)
    return None


while True:
    word = input("Enter a word to translate: ")
    word = str(word)
    translate(word)