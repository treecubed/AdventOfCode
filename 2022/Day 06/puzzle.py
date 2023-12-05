def preprocess(file_name):
	
	with open(file_name + '.txt') as file:
		file_data = file.readlines()
		file_data = file_data[0].rstrip()
	
	return file_data

def check_sequence(seq, length):
	if len(set(seq)) == length:
		return True
	return False

def puzzle1():
	solution = 0
	for i in range(len(data) - 3):
		if check_sequence(data[i:i + 4], 4):
			solution = i + 4
			break
	
	print(f'Puzzle 1 solution: {solution}')


def puzzle2():
	solution = 0
	for i in range(len(data) - 13):
		if check_sequence(data[i:i + 14], 14):
			solution = i + 14
			break
	
	print(f'Puzzle 2 solution: {solution}')


# data = preprocess('example')
data = preprocess('input')
puzzle1()
puzzle2()