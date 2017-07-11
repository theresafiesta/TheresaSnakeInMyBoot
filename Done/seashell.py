import os, sys

class SeaShell:
	# variables
	home = ''
	user = ''
	root = '/'
	path = ''
	dirContents = ''
	command = ''
	
	# bools
	hasArgs = None
	
	# color unicode
	color_white = '\033[0m'
	color_red = '\033[31m'
	color_blue = '\033[34m'
	color_purple = '\033[35m'
	
	# methods
	def __init__(self):
		self.user = os.getlogin()
		self.dirContents = os.listdir()
		return None
		
	def mainloop(self):
		print(self.color_blue+'======================================================'+self.color_purple)
		print('\tSea SHell ...zby-the-sea-shore!'+self.color_blue)
		print('======================================================'+self.color_white)
		print(self.color_blue+'[*] enter a command or \'quit\' to stop.\n\n\n'+self.color_white)
		while True:
			ans = input(self.color_purple+'==> '+self.color_white)
			ans = str(ans)
			self.grabCommand(ans)
		return None
		
	def debug(self, item):
		print(self.color_blue+'\t[*]debug log: ' + str(item)+self.color_white)
		return None
		
	def errMsg(self,msg):
		print(self.color_red + '[X_X] ' + str(msg) + self.color_white)
		return None
		
	def debugGrabbed(self, parts, command, path, args, numArgs):
		print('----------------------------')
		print('[*]parts: ' )
		self.debug(parts)
	
		print('[*] command: ')	
		self.debug(command)
		
		print('[*] path: ')
		self.debug(path)
	
		print('[*] arguments: ')
		self.debug(args)
		self.debug(numArgs)
		print('----------------------------')
	
		return None
		
	def printList(self, L):
		num = 0
		for item in L:
			print(str(item))
		return None
	
	def split(self, line):
		parts = []
		part = ''
		numItems = 0
		
		# break up the line into parts
		for item in list(line.split(' ')):
			parts.append(item)
			numItems += 1
		self.hasArgs = None
		
		# if there are arguments and/or a path or not
		if numItems > 1: self.hasArgs = True
		elif numItems == 1: self.hasArgs = False
		else: self.errMsg('Oops! split() might be broken...')
		
		return list(parts)
			
	def grabCommand(self, ans):
		parts = []
		command = ''
		path = []
		args = []
		numArgs = 0
		numPaths = 0
		
		parts = self.split(ans)	#pop off the command at the front of the list

		if self.hasArgs:
			command = parts.pop(0)	
			for item in parts:		# get all remaining arguments and/or a path
				args.append(item)
				numArgs += 1
				
				"""if (str(item)).startswith('/') or (str(item)).startswith('\\'):
					path.append(item)
					numPaths += 1
				else:		# otherwise it is an argument 
					args.append(item)
					numArgs += 1
			if numPaths == 0: path = 'none'
			elif numPaths == 1: path = str(path)
			elif numPaths == 2: source = str(path[0]); destination = str(path[1])
			elif numPaths > 2: self.errMsg('error: prolly too many paths!')"""
					
				
		elif not self.hasArgs:
			parts = [ans]
			command = ans
			args = 'none'
			numArgs = 0
			path = 'none'
			
		else:
			self.errMsg('Oops! grabCommand() might be broken @ hasArgs...')
		
		#self.debugGrabbed(parts, command, path, args, numArgs)		
						
		# grab the appropriate function
		if command == 'ls' : self.ls()
		elif command == 'who': self.who()
		elif command == 'cd': path = args.pop(0); path = str(path); self.cd(path)
		elif command == 'pwd': self.pwd()
		elif command == 'quit': sys.exit()
		else: self.errMsg('Oops! grabCommand() might be broken @ command conditional...')
		
		return None
					
	def ls(self):
		self.printList((os.listdir()))
		return None
		
	def who(self):
		print(str(os.getlogin()))
		return None
	
	def cd(self,path):
		try:
			os.chdir(path)
		except:
			self.errMsg('Oops! cd() might be broken...')
		return None
		
	def pwd(self):
		print(str(os.getcwd()))
		return None
		
if __name__ == '__main__':
	sh = SeaShell()
	sh.mainloop()
	print(sh.color_blue+'[*] exited the sea shell by the sea shore.'+sh.color_white)