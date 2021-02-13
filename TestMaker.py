import random

class Question:
	def __init__(self,que,a,b,c,d,e,RC):
		self.que = que
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		self.e = e
		self.RC = RC
		self.raspunsCorect = [self.a,self.b,self.c,self.d,self.e][RC]
		
	def __str__(self):
		return '{}\n{}\n{}\n{}\n{}\n{}\n'.format(self.que,self.a,self.b,self.c,self.d,self.e)


Q1 = Question('\n1. Text for the Question 1\n','B. Example of text for answer option.','C. Example of text for answer option.','D. Example of text for answer option','E. Example of text for answer option.',0)
Q2 = Question('\n2. Text for the Question 2\n','A. Answer text','B. Answer text','C. Answer text','','',0)


qdb = [Q1,Q2]

while True:
	n = random.choice(qdb)
	print(n)
	userInput = input()
	if userInput == 'a':
		userInput = n.a
	elif userInput == 'b':
		userInput = n.b
	elif userInput == 'c':
		userInput = n.c
	elif userInput == 'd':
		userInput = n.d
	elif userInput == 'e':
		userInput = n.e
	if userInput == n.raspunsCorect:
		print('\n ------------------------------  Correct !  ------------------------------\n\n Next Question:')
	else:
		print('\n------------------------------  WRONG  ------------------------------\nThe correct answer is: ' + n.raspunsCorect + '\n---------------------------------------------------------------------\n\n Next Question:')
