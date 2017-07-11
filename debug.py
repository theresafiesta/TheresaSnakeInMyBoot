import random

class debug:

# unicode colors for text
	W = '\033[0m'  # white (normal)
	R  = '\033[31m' # red
	G  = '\033[32m' # green
	O  = '\033[33m' # orange
	B  = '\033[34m' # blue
	P  = '\033[35m' # purple
	T = '\033[36m' 	# teal
	
	def log(self, text, var):
		text = str(text)
		var = str(var)
		print(self.B+'[*_*] debug: ' + text + '=>   ' + var + self.W)
		return None
	
	def show(self, text):
		text = str(text)
		print(self.T+'[*_*] showing: ' + text + self.W)
		return None
		
	def info(self, text):
		print(self.T+'[^_-] info: ' + text + self.W)
		return None
		
	def success(self, text):
		print(self.G+'[^_^] success: ' + text + self.W)
		return None
	
	def warn(self, text):
		print(self.O+'[-_-] warning: ' + text + self.W)
		return None	
		
	def err(self, text):
		print(self.R+'[X_X] error: ' + text + self.W)
		return None
		
	# template for color combo prints of strings
	def colorPrint(self,text,array):
		colors = list(array)
		random.shuffle(colors)
		i = 0
		for char in text:
			if i < len(colors):
				print(colors[i] + char, end = '')
			else:
				i = 0
				print(colors[i] + char, end = '')
				random.shuffle(colors)
			i += 1
		print(self.W)
		return None
		
	def rainbow(self, text):
		rainbow = [self.R,self.O,self.G,self.T,self.B,self.P]
		self.colorPrint(text, rainbow)
		return None
	
	def citrus(self, text):
		citrus = [self.O,self.G]
		self.colorPrint(text, citrus)
		return None
	
	def americana(self, text):
		americana = [self.R,self.W,self.R,self.W,self.B]
		self.colorPrint(text, americana)
		return None
		
	def primary(self, text):
		primary = [self.R,self.O,self.B]
		self.colorPrint(text, primary)
		return None
			
	def clouds(self,text):
		clouds = [self.W,self.W,self.W, self.T, self.T]
		self.colorPrint(text, clouds)
		return None
	
	def beach(self,text):
		clouds = [self.O,self.O,self.T,self.T,self.T,self.O]
		self.colorPrint(text, clouds)
		return None
		
	def poison(self,text):
		poison = [self.G, self.P, self.G, self.P, self.G, self.P]
		self.colorPrint(text, poison)
		return None
	
	def mystery(self,text):
		rainbow = [self.R,self.O,self.G,self.T,self.B,self.P,self.R,self.O,self.G,self.T,self.B,self.P]
		mystery = []
		color = []
		for i in range(0,7):
			color = random.choice(rainbow)
			mystery.append(color)
		self.colorPrint(text, mystery)
		return None
	
	
if __name__ == '__main__':
	test = debug()
	# log schemes
	test.log('LOG!','itemname')
	test.show('SHOW!')
	test.info('INFO!')
	test.success('SUCCESS!')
	test.warn('WARN!')
	test.err('ERR!')
	# color scheme prints
	test.rainbow('RAINBOW city!')
	test.citrus('sweet and sour CITRUS fruit!')
	test.americana('fourth of july -esque! how very AMERICANA.')
	test.primary('oh yea its PRIMARY time!')
	test.clouds('what lovely weather have we on this CLOUDy day.')
	test.beach('lets play volleyball on the BEACH.')
	test.poison('are you POISONed? you had better drink a potion!')
	test.mystery('its an ipsum lorem kind of MYSTERY we have here!!')
