# gets a string from a text file and counts the number of words
import os

def count(sentence):
    words = []
    word = ''
    punc = [' ',',','.','-','_',', ','!','(',')',';','\EOF']
    isDone = False
    # loop and collect all the words in a list
    while not isDone:
        for char in sentence:
            # if char is part of a word
            if char not in punc:
                word += char
                #if it is the last word
                if sentence.find(char) == (len(sentence) - 1):
                    sentence = ''
                    words.append(word)
                    isDone = True
                    break
            # if char is punctuation
            else:
                sentence = sentence[sentence.find(char)+1:]
                words.append(word)
                break
        word = ''
        if sentence == '' : break
        if isDone : break
    # get the count and print it
    count = 0
    for item in words:
        count += 1
    print(str(count) + " words total.")
    return None

def getSentence():
    sentence = ""
    filename = open("sentence.txt","r")
    for line in filename.readlines():
        sentence += line
    filename.close()
    print(sentence)
    return sentence
	
#sentence = getSentence()
sentence = "how now brown cow"
count(sentence)