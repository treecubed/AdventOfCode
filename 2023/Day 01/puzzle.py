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
		line = line.replace('one','1')
		line = line.replace('two','2')
		line = line.replace('three','3')
		line = line.replace('four','4')
		line = line.replace('five','5')
		line = line.replace('six','6')
		line = line.replace('seven','7')
		line = line.replace('eight','8')
		line = line.replace('nine','9')
		line = ''.join(c for c in line if c.isdigit())
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