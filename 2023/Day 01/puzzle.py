import re

match_str = '(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))'
num_dict = {
	'one': '1',
	'two': '2',
	'three': '3',
	'four': '4',
	'five': '5',
	'six': '6',
	'seven': '7',
	'eight': '8',
	'nine': '9'
}


def mapping(item):
	return num_dict.get(item, item)


def preprocess(file_name):
	def process_line(line):
		line = line.rstrip()
		line = ''.join(c for c in line if c.isdigit())
		return line
	
	with open(file_name + '.txt') as file:
		file_data = file.readlines()
		file_data = [process_line(line) for line in file_data]
	
	return file_data


def reprocess(file_name):
	def process_line(line):
		line = line.rstrip()
		match = re.findall(match_str, line)
		line = ''.join(list(map(mapping,match)))
		return line
	
	with open(file_name + '.txt') as file:
		file_data = file.readlines()
		file_data = [process_line(line) for line in file_data]
	
	return file_data


def puzzle1():
	values = []
	for line in data:
		values.append(int(f'{line[0]}{line[-1]}'))
	
	solution = sum(values)
	
	print(f'Puzzle 1 solution: {solution}')


def puzzle2():
	values = []
	for line in data2:
		values.append(int(f'{line[0]}{line[-1]}'))
	
	solution = sum(values)
	
	print(f'Puzzle 2 solution: {solution}')


# data = preprocess('example')
data = preprocess('input')
puzzle1()
data2 = reprocess('input')
puzzle2()
