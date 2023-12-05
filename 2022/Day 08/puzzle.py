def preprocess(file_name):
	
	def process_line(line):
		line = line.rstrip()
		return line
	
	with open(file_name + '.txt') as file:
		file_data = file.readlines()
		file_data = [process_line(line) for line in file_data]
	
	return file_data


def puzzle1():
	width = len(data[0])
	height = len(data)
	visible = [[0] * width] * height
	
	for y in range(height):
		north_max = -1
		south_max = -1
		for x in range(width):
			pass
		
		
	
	solution = 0
	
	print(f'Puzzle 1 solution: {solution}')


def puzzle2():
	
	
	
	solution = 0
	
	print(f'Puzzle 2 solution: {solution}')


data = preprocess('example')
# data = preprocess('input')
puzzle1()
puzzle2()