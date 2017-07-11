# counts the vowels in a word

def countVowels(word):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    num = 0
    for char in word:
        if char in vowels:
            num += 1
    print(word + ' has ' + str(num) + ' vowels.')
    return None
    
while True:
    word = input("enter a word to count the number of vowels it has: ")
    word = str(word)
    countVowels(word)