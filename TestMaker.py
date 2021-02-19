### A local, inside python, without database or external actions, test maker that will let you introduce questions
### and answers to be used by yourself to practice for an exam (driving exam or any abc like quiz)
### It will ask you for an answer from a to e and provide the correct answer if you get it wrong.
### It's a single option answer.

import random

class Question:
	def __init__(self,que,a,b,c,d,e,CA):
		self.que = que
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		self.e = e
		self.CA = CA			### CA is used as index when you enter the data to point out towards the correct answer
		self.correctAnswer = [self.a,self.b,self.c,self.d,self.e][CA]     
		
	def __str__(self):					#### function used to return QUESTION with answers as a string
		return '{}\n{}\n{}\n{}\n{}\n{}\n'.format(self.que,self.a,self.b,self.c,self.d,self.e)

### When you enter questions if you leave an empty string at answers it will show only the answers entered. 
### Just remember to use last arguement as index that points out to the correct answer
### Replace the text and add more questions as the same format right below
Q1 = Question('\n1. Text for the Question 1\n','B. Text for answer option.','C. Text for answer option.','D. Text for answer option.','E. Text for answer option..',0)
Q2 = Question('\n2. Text for the Question 2\n','A. Text for answer option.','B. Text for answer option.','Text for answer option.','','',0)

### Each question from above should also be added to this list qdb. This list will be later used to randomize the order
qdb = [Q1,Q2]

while True:                       ### just an endless loop so you can stop whenever you want
	n = random.choice(qdb)	  ### this will randomize the order of the questions you will receive
	print(n)
	rawInput = input()
	userInput = rawInput.lower() 	### this kills the bug if you enter the letter for the answer in either capital letters or lower. It will work for both ways
	if userInput == 'a':		### this will let you answer with options like a, b, c, d, e instead of writting the whole answer
		userInput = n.a
	elif userInput == 'b':
		userInput = n.b
	elif userInput == 'c':
		userInput = n.c
	elif userInput == 'd':
		userInput = n.d
	elif userInput == 'e':
		userInput = n.e
	if userInput == n.correctAnswer:
		print('\n ------------------------------  Correct !  ------------------------------\n\n Next Question:')
	else:
		print('\n------------------------------  WRONG  ------------------------------\nThe correct answer is: ' + n.correctAnswer + '\n---------------------------------------------------------------------\n\n Next Question:')
