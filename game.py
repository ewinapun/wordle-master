#!/usr/bin/env python3

from word_list import *
from utils import *
import random

def welcome_message():
	print("\n**********************************************")
	print("*            Welcome to wordle               *")
	print("**********************************************\n")


if __name__ == '__main__':
	welcome_message()
	my_word_list = La.copy()
	correct = False
	count = 0
	updated_present = dict()
	# generate a true answer
	answer = random.choice(La)
	while not correct:
		count += 1
		print("--------------------", count, "/ 6 --------------------")
		while True:
			guess = input("Enter your guess: ")
			if len(guess) != len(answer):
				print("Your guess is not the right length")
			elif (guess not in La) and (guess not in Ta):
				print("Your guess is not a word")
			else:
				break
		rightSpot, present, absent = get_guess_feedback(guess, answer)
		for key in present:
			if key not in updated_present:
				# save new present letter and position it should not be
				updated_present[key] = present[key]
			else:
				if present[key] not in updated_present[key]:
					updated_present[key] += present[key]
		correct = (rightSpot == guess)
		my_word_list = update_word_list(my_word_list, rightSpot, updated_present, absent)
		if not correct:
			print("letters in right spot: " + rightSpot)
			print("letters in wrong spot: ", updated_present)
			print("letters not in answer: " + absent)
			print("%d possible answers: " % len(my_word_list), my_word_list)
		else:
			print("Congrats! " + answer + " is the right word!")
