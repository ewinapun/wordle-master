#!/usr/bin/env python3

# this script aims to explore which initial guess is best to return the best performance

from word_list import *
from utils import *
from solver import *
import random
from tqdm import tqdm
nwords = len(La)

class Guesses():
	
	def __init__(self, initguess, attempt_num):
		self.initguess = initguess
		self.attempt_num = attempt_num
		self.attempt_freq = dict()
		self.tricky_words = []
		self.success_rate = 0
		self.avg_attempt  = 0

	def perf_summary(self):
		# get result performance summary
		self.get_attempt_count()
		self.get_tricky_words()
		self.get_success_rate()
		self.get_average_num_attempt();

	def get_attempt_count(self):
		for ind in set(self.attempt_num):
			self.attempt_freq[ind] = (self.attempt_num.count(ind) / nwords * 100)

	def get_tricky_words(self):
		# words that need more than 6 attempts
		self.tricky_words += [La[i] for i, count in enumerate(self.attempt_num) if count > 6]

	def get_success_rate(self):
		# define success as less than six attempts
		self.success_rate = (1 - len(self.tricky_words) / nwords) * 100

	def get_average_num_attempt(self):
		for key in self.attempt_freq:
			self.avg_attempt += int(key) * self.attempt_freq[key] / 100

	def print_perf(self):
		# print summary
		print('\n-------------------------------')
		print("For", self.initguess, "as the initial guess, here's the wordle solver performance.")
		self.print_distribution()
		self.print_tricky_words()
		self.print_rate()
		self.print_average_num_attempt()

	def print_distribution(self):
		print('\nAttempts distribution (%):')
		print('-------------------------------')
		for key in self.attempt_freq:
			print('\t', key, " - %8.2f" % self.attempt_freq[key])

	def print_tricky_words(self):
		print("Here are some words that need more than 6 attempts:\n", self.tricky_words)

	def print_rate(self):
		print("Sucessful rate:%8.2f" % self.success_rate, "%")
		
	def print_average_num_attempt(self):
		print("Average number of attempts: %8.2f" % self.avg_attempt)


if __name__ == '__main__':
	welcome_message()
	print("I'm designed to return the minimum number of attempts, given your initial guess, on a list of common 5-letter English words.")
	# ask user for their initial guess
	i = 0
	glist = []
	exit = False
	while i < 3:
		while not exit:
			initguess = input("\nWhat's your initial guess? No clue? Try arise or ariel: (type q to quit)\n")
			# check input
			if initguess == 'q':
				exit = True
				break
			elif (initguess not in La) and (initguess not in Ta):
				print("Your word is not in the list")
			elif len(initguess) != len(La[0]):
				print("Your word is not the right length")
			else:
				break
		if initguess != 'q':
			attempt_num = []
			# loop for all word in word list
			for wi in tqdm(range(nwords)):
				# print("%d " %wi, end='', flush=True)
				answer = La[wi]
				count = return_attempt_number(answer, initguess.lower())
				attempt_num.append(count)
			glist.append(Guesses(initguess, attempt_num))
			i += 1
		else:
			break
	print("\nInit guess \t success \t avg attempt")
	print("----------------------------------------------")
	for obj in glist:
	# print summary across all initial guess
		obj.perf_summary()
		# glist[i].print_perf()
		print("%s\t%8.2f\t%8.2f"%(obj.initguess, obj.success_rate, obj.avg_attempt))
	import pdb;pdb.set_trace()

