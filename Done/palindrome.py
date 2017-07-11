# checks if a word is a palindrome

def checkPalindrome(word):
    reverse = ""
    for i in range(0, len(word)):
        if i == 0:
            reverse += word[len(word)-1]
        elif i == len(word):
            reverse += word[0]
        else:
            reverse += word[-i - 1]
    print(word +  " reversed is " + reverse)
    if reverse == word:
        print(word + ' IS a palindrome!!\n')
    else:
        print(word + ' is NOT a palindrome.\n')
    return None

while True:
    word = input("enter a word to check if it is a palindrome: ")
    word = str(word)
    checkPalindrome(word)
