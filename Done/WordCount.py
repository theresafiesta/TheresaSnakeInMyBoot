# gets a string from a text file and counts the number of words
import os
from debug import *
	
class WordCount:

	def count(self, sentence):
	    words = []
	    word = ''
	    punc = [' ',',','.','-','_',', ','!','(',')',';','\EOF']
	    isDone = False
	    
	    # loop and collect all the words in a list
	    while not isDone:
	        for char in sentence:
	            # if char is not punctuation (i.e., part of a word)
	            if char not in punc:
	                word += char
	                #if it is the last word of a line
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
	
	def grabLineFromFile(self,name):
	    sentence = ""
	    name = str(name)
	    filename = open(name,"r")
	    for line in filename.readlines():
	        sentence += line
	    filename.close()
	    return sentence
		
if __name__ == '__main__':		
	sentence = "how now brown cow sow now dow frow brow"
	test = WordCount()
	
	try:
		debug = debug()
		debug.rainbow('=============================')
		debug.title('   Testing WordCount.py!')
		debug.rainbow('=============================')
	except:
		print('[*] fyi: debug module is missing.\n\n')	
		print('=============================')
		print('   Testing WordCount.py!')
		print('=============================')
		
	test.count(sentence)