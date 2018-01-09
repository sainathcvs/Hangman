import random
word_dict=['apple','maple','grape','paper']
def select_random_word():
	return random.choice(word_dict)

def check_if_letter_exists(input):
	index= sel_word.find(input)
	sel_word = sel_word.replace(input,'_',1)
	return index

sel_word = select_random_word()
print 'hidden word:',sel_word
display_word = '_'*len(sel_word)
display_word_list=list(display_word)
letters_left=len(sel_word)
while letters_left>0:
	input_letter = raw_input('Guess the letter(A-Z):').lower()
	print 'You chose the letter ',input_letter,
	index = check_if_letter_exists(input_letter)
	print index
	if index !=-1:
		display_word_list[index]=str(input_letter)
		letters_left-=1
		print '\nguessed word:',''.join(display_word_list)
		print 'letters left:',letters_left,
	print '\n'