import time, random

class TrafficLight:
	# variables
	lights = ['green','yellow','red']
	g = '\033[32m'
	y = '\033[33m'
	r = '\033[31m'
	w = '\033[0m'
	colors = [g,y,r]
	lightOn = ''
	isLightOn = None
	
	# constructor
	def __init__(self):
		self.lightOn = str(self.lights[0])
		isTrafficComing = True		
		return None
		
	# methods
	def mainloop(self):
		while True:
			self.waitForLight()
		return None
	
	def greeting(self):
		self.colorPrint(self.colors, "___________________________________")
		self.colorPrint(self.colors,"Welcome to the Traffic Light System!")
		self.colorPrint(self.colors, "___________________________________\n\n")
		print(self.w)
		return None
		
	def colorPrint(self,colorset,text):
		colors = list(colorset)
		text = str(text)
		i = 0
		random.shuffle(colors)
		for char in text:
			if i < len(colors):
				print(colors[i] + char, end='')
				i += 1
				random.shuffle(colors)
			else:
				i = 0
				print(colors[i] + char, end='')
				random.shuffle(colors)
		print(self.w)
		return None
		
	def displayLight(self):
		text = self.lightOn + " light!"
		if self.lightOn == str(self.lights[0]):
			self.colorPrint([self.colors[0]], text)
		elif self.lightOn == str(self.lights[1]):
			self.colorPrint([self.colors[1]], text)
		elif self.lightOn == str(self.lights[2]):
			self.colorPrint([self.colors[2]], text)
		else:
			print('[*] error: displayLight() cannot get the current light!')
		print(end='')
		return None
		
	def changeLight(self):
		if self.lightOn == str(self.lights[0]):
			self.lightOn = str(self.lights[1])
		elif self.lightOn == str(self.lights[1]):
			self.lightOn = str(self.lights[2])
		elif self.lightOn == str(self.lights[2]):
			self.lightOn = str(self.lights[0])
		else:
			print('[*] error: changeLight() cannot get the current light!')
		return None
	
	def waitForLight(self):
		self.displayLight()
		if self.lightOn == str(self.lights[0]):
			time.sleep(4)
		elif self.lightOn == str(self.lights[1]):
			time.sleep(2)
		elif self.lightOn == str(self.lights[2]):
			time.sleep(6)
		else:
			print('[*] error: waitLight() cannot get the current light!')
		self.changeLight()
		return None

if __name__ == '__main__':
	test = TrafficLight()
	test.greeting()
	test.mainloop()
	
