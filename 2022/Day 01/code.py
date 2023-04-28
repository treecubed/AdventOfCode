def preprocess(file_name):
	
	def process_line(line):
		line = line.rstrip()
		return line
	
	with open(file_name + '.txt') as file:
		file_data = file.readlines()
		file_data = [process_line(line) for line in file_data]
	
	return file_data


def puzzle1():
	cals = []
	cal = 0
	for row in data:
		if row:
			cal += int(row)
		else:
			cals.append(cal)
			cal = 0
	max_cal = 0
	for row in cals:
		if row > max_cal:
			max_cal = row
	solution = max_cal
	
	print(f'Puzzle 1 solution: {solution}')


def puzzle2():
	cals = []
	cal = 0
	for row in data:
		if row:
			cal += int(row)
		else:
			cals.append(cal)
			cal = 0
	cals.sort(reverse = True)
	
	solution = cals[0] + cals[1] + cals[2]
	
	print(f'Puzzle 2 solution: {solution}')


# data = preprocess('example')
data = preprocess('input')
puzzle1()
puzzle2()