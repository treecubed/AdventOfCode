def process_line(line):
	line = line.rstrip()
	return line

with open('example.txt') as file:
	data = file.readlines()
	data = [process_line(line) for line in data]

test = {(0, 0): {'cost': 0, 'parent': (0, 0)}}

def puzzle1():
	
	print(data)
	
	solution = 0
	
	print(f'Puzzle 1 solution: {solution}')

def puzzle2():
	
	
	
	solution = 0
	
	print(f'Puzzle 2 solution: {solution}')

puzzle1()
puzzle2()