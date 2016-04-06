import random #import random library 

#setting up the initial comp weight. The weight that will be guessed will be a random number betwee 1 and 99.
comp_weight = random.randrange(0,100) 

guessed = False; 

while not guessed:
	
	answer = input("Guess The Weight!")
	answer = int(answer)
	
	print(comp_weight)
	
	if (answer == comp_weight):
		print ("You got it, dude!")
		guessed = True
	elif (answer > comp_weight and answer < (comp_weight + 5)):
		print ("I'm so sorry, but you need to go slightly lower.")
	elif (answer <comp_weight and answer > (comp_weight - 5)):
		print ("I'm so sorry, but you need to go slightly higher.")
	elif (answer > comp_weight + 5 or answer < comp_weight - 5):
		print ("You're wayyy off, dude. Try again!")
