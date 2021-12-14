def process_line(line):
	line = line.rstrip().split('|')
	line = [sorted(line[0].split(), key = len), line[1].split()]
	return line

with open('input.txt') as file:
	lines = file.readlines()
	lines = [process_line(line) for line in lines]

def str_diff(a, b):
	for char in b:
		a = a.replace(char,'')
	return a

def get_decoder(decode_lst):
	decode_dict = {
		decode_lst[0] : 1,
		decode_lst[1] : 7,
		decode_lst[2] : 4,
		decode_lst[9] : 8
	}
	seg_a = str_diff(decode_lst[1], decode_lst[0])
	
	print(seg_a, decode_dict)
	return decode_dict

def puzzle1():
	count = 0
	for line in lines:
		for digit in line[1]:
			if len(digit) in [2, 3, 4, 7]:
				count += 1
	
	solution = count
	
	print(f'Puzzle 1 solution: {solution}')

def puzzle2():
	
	for line in lines:
		# print(line[0])
		decoder = get_decoder(line[0])
	
	solution = 0
	
	print(f'Puzzle 2 solution: {solution}')

puzzle1()
puzzle2()