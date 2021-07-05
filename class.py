#!/bin/python3.9


class main():
	def __init__(self):
		self.uppercase = 0
		self.lowercase = 0
		self.vowels = 0
		self.consonants = 0
		self.space = 0 
		self.string = ""
	
	def getstr(self):
		self.string = input("Enter the letter : ")
		
	def upper_case(self):
		for letter in self.string:
			if (letter.isupper()):
				self.uppercase += 1
				
	def lower_case(self):
		for letter in self.string:
			if (letter.islower()):
				self.lowercase += 1
				
	def vowvels(self):
		for letter in self.string:
			if (letter in ("A","a","E","e","I","i","O","o","U","u" )):
				self.vowels += 1			
				
	def consonant(self):
		for letter in self.string:
			if (letter in ("A","a","E","e","I","i","O","o","U","u" )):
				self.consonants += 1
				
	def spaces(self):
		for letter in self.string:
			if (letter == " "):
				self.space += 1
				
	def execute(self):
		self.upper_case()
		self.lower_case()
		self.vowvels()
		self.consonant()
		self.spaces()
		
	def display(self):
		print("The Given Strings Contains ")
		print("%d Uppercase Letters " %self.uppercase)
		print("%d Lowercase Letters " %self.lowercase)
		print("%d Vowels Letters " %self.vowels)
		print("%d Consonants Letters " %self.consonants)
		print("%d space Letters " %self.space)
		

r = main()
r.getstr()
r.execute()
r.display()

	
			
			
			
			
			
			
			


