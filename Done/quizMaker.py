import sys 

class quizMaker:
	# attributes
	quiz = {}		# {'answer' : [q1,a1,a2,a3,a4]], ...  ' ' : []}	
	userSel = []
	letters = ['a','b','c','d','e','f']
	score = 0.00
	numCorrect = 0
	numWrong = 0
	numOfQuestions = 0
	isCorrect = None
	quizLength = 0
	
	# unicode colors for text
	W = '\033[0m'  # white (normal)
	R  = '\033[31m' # red
	G  = '\033[32m' # green
	O  = '\033[33m' # orange
	B  = '\033[34m' # blue
	P  = '\033[35m' # purple

	# constructors
	def __init__(self, quiz):
		self.quiz = quiz
		num = 0
		for key in self.quiz.keys():
			self.quizLength += 1
		return None
	
	# methods
	def mainloop(self):
		print(self.P+'================================================'+self.B)
		print('\t\tQuiz Maker!')
		print(self.P+'================================================'+self.B)
		print('Take the super fun quiz and get a grade at the end!\n\n'+self.W)
		self.takeQuiz()
		self.askToSubmit()
		self.gradeQuiz()
		print('\nCongrats, you scored a %.2f on the quiz!' % (self.score))
		return None
		
	def debug(self, text, var):
		text = str(text)
		var = str(var)
		print(self.O+'[*_*]debug log: ' + text + '=>\t' + var + self.W)
		return None
	
	def err(self, text):
		print(self.R+'[X_X]error: ' + text + self.W)
		return None
	
	def selectAnswer(self, ans):
		self.userSel.append(ans) 
		return None
		
	def takeQuiz(self):
		qnum = 1
		numChoices = 0
		
		# display each question
		for key in self.quiz.keys():
			# display the question and answer choices
			numChoices = self.grabQuestion(qnum)
			# have user input their choice for current question
			while True:
				ans = input(self.P+'==> '+self.W)
				ans = str(ans)
				# if ans is a letter and is in range of indexes for choices, assign selected
				if ans in self.letters[:numChoices]: self.selectAnswer(ans); break
				else: self.err('invalid answer selected.')
			# housekeeping
			qnum += 1
		return None
		
	def printChoices(self, choices):
		letter = ''
		choice = ''
		i = 0
		
		# print the choices and their letters
		for item in choices:
			choice = str(item)
			letter = str(self.letters[i])
			print('\t' + letter + '.\t' + choice)
			i += 1
		return len(choices)
		
	def grabQuestion(self, qnum):
		num = 0
		question = ''
		choices = []
		numChoices = 0
		
		# print the question and its choices
		for val in self.quiz.values():
			num += 1
			if num == qnum: 
				question = str(val[0])
				choices = val[1:]
				break
		print(str(qnum) + '.  ' + question)
		numChoices = self.printChoices(choices)
				
		return numChoices
		
	def displayUserQuiz(self):
		question = ''
		ans = ''
		num = 0
		index = 0
		
		# show each question next to the answer the user entered
		for val in self.quiz.values():
			question = str(val[0])
			choices = val[1:]
			# get the value of the answer by applying letter index to choices
			index = self.letters.index(self.userSel[num])
			ans = choices[index]
			ans = str(ans)
			print(self.B+ str(num+1) + '.  ' + question + self.G + ' =>  ' + self.W + str(ans) )
			num += 1
		print()
		return None
		
	def grabSelectedAns(self,qnum):
		ans = ''
		index = 0
		choices = []
		num = 0
		
		for val in self.quiz.values():
			if num == qnum:
				choices = val[1:]
				# get the value of the answer by applying letter index to choices
				index = self.letters.index(self.userSel[num])
				ans = choices[index]
				ans = str(ans)
				break
			num+= 1
		return ans
		
	def grabCorrectAns(self,qnum):
		num = 0
		ans = ''
		
		for key in self.quiz.keys():
			if num == qnum:
				ans = str(key)
				break
			num += 1
		return ans
		
	def compareAns(self,qnum):
			ans = ''
			correct = ''
			
			# compare the user's answer against the quiz key(i.e., key is right ans)
			ans = self.grabSelectedAns(qnum)
			correct = self.grabCorrectAns(qnum)
			if ans == correct: 
				self.isCorrect = True
			elif ans != correct: 
				self.isCorrect = False
			else:
				self.isCorrect = None
				self.err('Oops! compareAns() might be broken...')
			return None
		
	def gradeQuiz(self):
		qnum = 0
		
		self.numCorrect = 0
		self.numWrong = 0
		self.isCorrect = None
		
		# check answers for correct values and record results
		for key in self.quiz.keys():
			self.compareAns(qnum)
			if self.isCorrect: self.numCorrect += 1
			elif not self.isCorrect: self.numWrong += 1
			elif self.isCorrect == None:
				numWrong += 1
				self.err('Oops! gradeQuiz() might be broken...')
			qnum += 1
		# calculate and display the score
		self.score = float(self.numCorrect / self.quizLength) * float(100)
		return None
	
	def changeAnswer(self, qnum):
		numChoices = 0
		
		# print the specified question and choices
		numChoices = self.grabQuestion(qnum)
		# have user input their choice for current question
		while True:
			ans = input(self.P+'==> '+self.W)
			ans = str(ans)
			# if ans is a letter and is in range of indexes for choices, assign selected
			if ans in self.letters[:numChoices]: self.selectAnswer(ans); break
			else: self.err('invalid answer selected.')
		return None
		
	def askToSubmit(self):
		print('Review Before Submission\n================================================')
		self.displayUserQuiz()
		while True:
			print('\n1. Submit\n2. Change an answer for a question')
			ans = input(self.P+ '==> '+ self.W)
			ans = int(ans)
			if ans == 1 : self.gradeQuiz(); break
			elif ans == 2 :
				qnum = input('enter question #: ')
				qnum = int(qnum)
				if qnum <= self.quizLength: self.changeAnswer(qnum)
				else: self.err('invalid question number entered.')
			else: self.err('invalid selection.')
		return None
				
			
# test for run at top-level else assumes import
if __name__ == '__main__':
	while True:
		quiz = {'blue' : ['what color is the sky?','green','blue','grey','yellow'],
		'5' : ['2 + 3 = ?','2','7','9','5']}
		testQuiz = quizMaker(quiz)
		testQuiz.mainloop()
		while True:
			print('take the quiz again? (y/n)')
			ans = input('==>')
			if ans == 'y' or ans == 'yes': break
			elif ans == 'no' or ans == 'n': sys.exit()
			else: continue
