from random import randint

rounds = input("How many rounds? ")

choice = []
compChoice = []

for x in range (0, rounds):
	roundNr = x + 1
	print "Make your choice for round ", roundNr
	roundChoice = raw_input()
	choice.append(roundChoice)
	print choice

	compNr = randint(1,3)
	compName = {1: "rock", 2: "paper", 3: "scissor"}
	compChoice.append(compName[compNr])
	print "this is the computer"
	print compChoice


	