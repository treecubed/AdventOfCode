def preprocess(file_name):
	
	def process_line(line):
		line = line.rstrip()
		return line
	
	with open(file_name + '.txt') as file:
		file_data = file.readlines()
		file_data = [process_line(line) for line in file_data]
	
	return file_data

score1 = {
	'A X' : 4,
	'A Y' : 8,
	'A Z' : 3,
	'B X' : 1,
	'B Y' : 5,
	'B Z' : 9,
	'C X' : 7,
	'C Y' : 2,
	'C Z' : 6,
}

score2 = {
	'A X': 3,
	'A Y': 4,
	'A Z': 8,
	'B X': 1,
	'B Y': 5,
	'B Z': 9,
	'C X': 2,
	'C Y': 6,
	'C Z': 7,
}

def puzzle1():
	
	points = 0
	for row in data:
		points += score1[row]
	
	solution = points
	
	print(f'Puzzle 1 solution: {solution}')


def puzzle2():
	
	points = 0
	for row in data:
		points += score2[row]
	
	solution = points
	
	print(f'Puzzle 2 solution: {solution}')


# data = preprocess('example')
data = preprocess('input')
puzzle1()
puzzle2()