# Hi Lo Guessing game
print("Choose a number between 1 and 100")
print("After each guess, enter:")
print("0 - if I got it right")
print("-1 - if I guessed too high")
print("1 - if I guessed too low")
def take_guess(high, low, guesses):
	guess = (high + low) / 2
	keep_asking = 1
	while keep_asking == 1:
		print ("My guess is: " + str(guess)) 
		response = raw_input("enter a response: ")
		if str(response) == "0":
			print("I got it right")
			print("It took: " + str(guesses) + " guesses!")
			keep_asking == 0
		elif str(response) == "-1":
			print("I will guess lower")
			high = guess
			take_guess(high, low, guesses + 1)
			keep_asking == 0
		elif str(response) == "1":
			print("I will guess higher")
			low = guess
			take_guess(high, low, guesses + 1)
			keep_asking == 0
		else:
			print("Choose a number between 1 and 100")
			print("After each guess, enter:")
			print("0 - if I got it right")
			print("-1 - if I guessed too high")
			print("1 - if I guessed too low")
		print(" ")
		return("Your response was: " + str(response))
#def main():
	#high = 1000
	#low = 0
	#guesses = 1
	#while high > low:
		#response = return(take_guess(high, low))
		#if response == 0: 
			#high == 0 
		#elif response == -1:
			#high = guess - 1 
		#elif response == 1: 
			#high = guess + 1
	#if high == low:
		#print response
take_guess(1000, 0, 0)

			