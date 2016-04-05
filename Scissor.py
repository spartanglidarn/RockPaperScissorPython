class Scissor:
	def scissor(user, computer):
		#1 is equal to rock
		if computer == 1:
			print "the computer is the winner"
		#2 is equal to paper	
		elif computer == 2:
			print "the user is the winner"
		#3 is equal to scissor
		elif computer == 3:
			print "it's a draw"