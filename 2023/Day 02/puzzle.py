def preprocess(file_name):
	
	def process_line(line):
		line = line.rstrip()
		line = [l.split() for l in line.replace(':',',').replace(';',',').split(',')]
		item = {
			'game': int(line.pop(0)[1]),
			'red': 0,
			'green': 0,
			'blue': 0
		}
		for l in line:
			i = int(l[0])
			if i > item[l[1]]:
				item[l[1]] = i
		return item
	
	with open(file_name + '.txt') as file:
		file_data = file.readlines()
		file_data = [process_line(line) for line in file_data]
	
	return file_data


def puzzle1():
	real_contents = {'red': 12, 'green': 13, 'blue': 14}
	valid_games = []
	for item in data:
		valid = 1
		for content in real_contents:
			if item[content] > real_contents[content]:
				valid = 0
		if valid: valid_games.append(item['game'])
	
	print(valid_games)
	solution = sum(valid_games)
	
	print(f'Puzzle 1 solution: {solution}')


def puzzle2():
	powers = []
	for item in data:
		powers.append(item['red'] * item['green'] * item['blue'])
	
	solution = sum(powers)
	
	print(f'Puzzle 2 solution: {solution}')


# data = preprocess('example')
data = preprocess('input')
puzzle1()
puzzle2()