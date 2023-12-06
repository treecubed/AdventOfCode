import re

symbols = ['*', '%', '$', '+', '#', '-', '&', '/', '=', '@']

def preprocess(file_name):
	
	def process_line(line):
		line = line.rstrip()
		return line
	
	with open(file_name + '.txt') as file:
		file_data = file.readlines()
		file_data = [process_line(line) for line in file_data]
	
	symbol_data = {}
	number_data = []
	for idy, line in enumerate(file_data):
		for idx, char in enumerate(line):
			if char in symbols:
				symbol_data[(idx, idy)] = char
		for match in re.finditer('[0-9]+', line):
			number_data.append({
				'value': int(match.group()),
				'start': match.start(),
				'end': match.end() - 1,
				'y': idy
				})
	
	return {'symbols': symbol_data, 'numbers': number_data}


def points_in_box(box_p1, box_p2):
	point_list = []
	for y in range(box_p1[1], box_p2[1]+1):
		for x in range(box_p1[0], box_p2[0]+1):
			point_list.append((x,y))
	return point_list

def puzzle1():
	part_numbers = []
	for num in data['numbers']:
		valid = 0
		points = points_in_box((num['start']-1,num['y']-1),(num['end']+1,num['y']+1))
		for p in points:
			if p in data['symbols']:
				valid = 1
		if valid:
			part_numbers.append(num['value'])
	solution = sum(part_numbers)
	
	print(f'Puzzle 1 solution: {solution}')


def puzzle2():
	gear = '*'
	gears = {}
	gear_ratios = []
	for num in data['numbers']:
		points = points_in_box((num['start']-1,num['y']-1),(num['end']+1,num['y']+1))
		for p in points:
			if p in data['symbols']:
				if data['symbols'][p] == gear:
					gears.setdefault(p, []).append(num['value'])
	for g in gears.values():
		if len(g) == 2:
			gear_ratios.append(g[0]*g[1])
	
	solution = sum(gear_ratios)
	
	print(f'Puzzle 2 solution: {solution}')


# data = preprocess('example')
data = preprocess('input')
puzzle1()
puzzle2()