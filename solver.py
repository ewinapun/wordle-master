#!/usr/bin/env python3

from word_list import *
from utils import *
import random

def welcome_message():
	nwords = len(La)
	print("\n**********************************************")
	print("*            Welcome to Wordle Bot           *")
	print("**********************************************\n")

def bestguess(my_word_list, rightSpot, dispInfo=False):
	# return the best guess from a shortlist of words that reduces the possible word list
	# best guess does not neccessarily have to be in my_word_list
	# sometimes it can maximize the chance of distinguishing very similar choices
	# e.g. "cupid" can be an excellent choice to tell apart "patch", "catch", "match", "hatch", "dutch"
	# input:
	# 	 my_word_list - possible word list from previous guess

	letter_freq, max_count_letters, min_count_letters = get_letter_freq(my_word_list, rightSpot)
	if dispInfo:
		print("Unknown letter distribution: ", letter_freq)
		print("min_count_letters", min_count_letters)
		print("max_count_letters", max_count_letters)
	shortlist = (La + Ta)
	if len(my_word_list) <= 3:
		# just flipping a coin if word list is short
		shortlist = my_word_list
	elif len(my_word_list) <= 8:
		# get shortlist from least frequently occured letters in my_word_list
		for i, key in enumerate(min_count_letters):
			temp_list = [word for word in shortlist if (key in word)]
			if len(temp_list) > 1:
				shortlist = temp_list
			else:
				break
			if i >= len(my_word_list)-1:
				break
	else:
		# get shortlist of words from most frequently occured letters in my_word_list
		for key in max_count_letters:
			temp_list = [word for word in shortlist if (key in word)]
			if len(temp_list) > 1:
				shortlist = temp_list
			else:
				break
	guess = random.choice(shortlist)
	if dispInfo:
		print("%d possible answers:  " % len(my_word_list), my_word_list)
		print("Best guess shortlist: ", shortlist)
		print("Chosen best guess is: ", guess)
	return guess

def get_letter_freq(my_word_list, rightSpot):
	# return the frequency of occurance per letter in words 
	# excluding the letter(s) in the right spot of answer 
	all_letter = []; 
	letter_freq = dict()
	# only pull out the remaining unknown letters
	for i, letter in enumerate(rightSpot):
		if letter == '_':
			all_letter += [word[i] for word in my_word_list]
	# get count per letter
	max_count_letters = dict()
	min_count_letters = dict()
	n = 0
	for letter in set(all_letter):
		letter_freq[letter] = all_letter.count(letter)
		# add the first n letter in max_count_letters
		if n < len(rightSpot):
			max_count_letters[letter] = letter_freq[letter]
			min_count_letters[letter] = letter_freq[letter]
		else:
			# keep track of which letters have the highest count
			if letter_freq[letter] > min(max_count_letters.values()):
				min_key = min(max_count_letters, key=max_count_letters.get)
				max_count_letters.pop(min_key)
				max_count_letters[letter] = letter_freq[letter]
			# keep track of which letters have the lowest count
			if letter_freq[letter] < max(min_count_letters.values()):
				max_key = max(min_count_letters, key=min_count_letters.get)
				min_count_letters.pop(max_key)
				min_count_letters[letter] = letter_freq[letter]
		n += 1
	max_count_letters = dict(sorted(max_count_letters.items(), key=lambda item: item[1], reverse=True))
	min_count_letters = dict(sorted(min_count_letters.items(), key=lambda item: item[1]))
	return letter_freq, max_count_letters, min_count_letters

def return_attempt_number(answer, initial_guess, dispInfo=False):
	# return the number of attempt the program took to get the right answer, given an initial guess
	my_word_list = La.copy()
	correct = False
	rightSpot = "_____"
	count = 0
	updated_present = dict()
	guess = initial_guess
	if dispInfo: print("The first guess is: ", guess)
	while not correct:
		count += 1
		rightSpot, present, absent = get_guess_feedback(guess, answer)
		if dispInfo: print("\n-----------", count, "/ 6 -----------")
		if dispInfo: print("letters in right spot: " + rightSpot)
		# if rightSpot_temp > rightSpot:
		# 	rightSpot = rightSpot_temp
		for key in present:
			if key not in updated_present:
				# save new present letter and position it should not be
				updated_present[key] = present[key]
			else:
				if present[key] not in updated_present[key]:
					updated_present[key] += present[key]
		correct = (rightSpot == guess)
		my_word_list = update_word_list(my_word_list, rightSpot, updated_present, absent)
		if correct:
			if dispInfo: print("I got %s in %d attempts!" % (answer, count))
		else:
			guess = bestguess(my_word_list, rightSpot, dispInfo=dispInfo)
		# 	print(updated_present)
		# 	print("letters not in answer: " + absent)
	return count


if __name__ == '__main__':
	welcome_message()
	initial_guess = "ariel" # subject to change
	while True:
		while True:
			# ask user for the word
			answer = input("\nWhat word are you asking me to solve?")
			# check input
			if len(answer) != len(La[0]):
				print("Your word is not the right length")
			elif (answer not in La):
				print("Your word is not in the list")
			else:
				break
		count = return_attempt_number(answer, initial_guess, dispInfo=True)
