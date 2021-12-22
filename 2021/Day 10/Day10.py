import math

def process_line(line):
	line = line.rstrip()
	return line

with open('input.txt') as file:
	data = file.readlines()
	data = [process_line(line) for line in data]

open_symbols = ['(', '[', '{', '<']
close_symbols = [')', ']', '}', '>']
syn_score = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
ac_score = {')' : 1, ']' : 2, '}' : 3, '>' : 4}

def check_line(line):
	lst = []
	for char in line:
		if char in open_symbols:
			lst.append(char)
		elif char in close_symbols:
			char_id = close_symbols.index(char)
			val = lst.pop()
			try:
				val_id = open_symbols.index(val)
			except ValueError:
				val_id = -1
			if val_id != char_id:
				return True, char
	return False, lst

def auto_complete(line):
	ret = ''
	while len(line) != 0:
		val = line.pop()
		val_id = open_symbols.index(val)
		ret += close_symbols[val_id]
	return ret

def get_ac_score(ac_ret):
	score = 0
	for char in ac_ret:
		score *= 5
		score += ac_score[char]
	return score

def puzzle1():
	lst = []
	
	for line in data:
		ret = check_line(line)
		if ret[0]:
			lst.append(syn_score[ret[1]])
	solution = sum(lst)
	
	print(f'Puzzle 1 solution: {solution}')

def puzzle2():
	lst = []
	
	for line in data:
		ret = check_line(line)
		if not ret[0]:
			ac_ret = auto_complete(ret[1])
			lst.append(get_ac_score(ac_ret))
	lst = sorted(lst)
	mid_idx = math.floor(len(lst)/2)
	solution = lst[mid_idx]
	
	print(f'Puzzle 2 solution: {solution}')

puzzle1()
puzzle2()