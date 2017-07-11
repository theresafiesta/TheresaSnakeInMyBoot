# generates cd keys: 4 letters - 3 numbers - 2 letters 2 numbers - 4 letters

import random

def generateKey():
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    key = ""
    # first set
    for i in range(0,4):
    
        key += str(random.choice(letters))
    key += "-"
    for i in range(0,3):
        key += str(random.choice(numbers))
    key += "-"
    for i in range(0,2):
        key += str(random.choice(letters))
    for i in range(0,2):
        key += str(random.choice(numbers))
    key += '-'
    for i in range(0,4):
        key += str(random.choice(letters))
    print(key)
    return None

ans = input("press any key to generate a key or type \'quit\' to stop: ")
while True:
    ans = str(ans)
    if(ans == 'quit') : break
    generateKey()
    ans = input()