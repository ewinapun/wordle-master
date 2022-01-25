def get_guess_feedback(guess, answer):
	# return the feedback for a guess by checking the answer
	n = len(answer)
	assert len(guess) == len(answer), "guess is not the right length"
	rightSpot = ''
	present = dict()
	absent = ''
	for i in range(n):
		corrLetter = (guess[i]==answer[i])
		if corrLetter:
			rightSpot += guess[i]
		else:
			rightSpot += '_'
			if guess[i] not in answer:
				absent += guess[i]
			else:
				for j in range(n):
					if guess[i] == answer[j] and i != j:
						present[i] = guess[i]
	return rightSpot, present, absent

	

def update_word_list(my_word_list, rightSpot, present, absent):
	# update the list of possible words for answer
	indices = [];
	for ind, word in enumerate(my_word_list):
		flag_remove = False
		for i in range(len(absent)):
			if absent[i] in word:
				flag_remove = True
				break
		for key in present:
			for l, letter in enumerate(present[key]):
				if letter not in word or letter==word[key]:
					flag_remove = True
					break
		for i in range(len(rightSpot)):
			if (rightSpot[i] != '_') and (word[i] != rightSpot[i]):
				flag_remove = True
				break
		if flag_remove:
			indices.append(ind)
	for index in sorted(indices, reverse=True):
		my_word_list.pop(index)
	return my_word_list