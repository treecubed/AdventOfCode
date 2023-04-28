def preprocess(file_name):
	
	def process_line(line):
		line = line.rstrip()
		return line
	
	with open(file_name + '.txt') as file:
		file_data = file.readlines()
		file_data = [process_line(line) for line in file_data]
	
	return file_data

def reduce(str1, str2):
	for char in str1:
		if str2.count(char):
			return char

def priority(char):
	val = ord(char)
	if val > 96:
		val -= 96
	else:
		val -= 38
	return val

def puzzle1():
	summation = 0
	
	for row in data:
		pos = int(len(row)/2)
		p1 = row[:pos]
		p2 = row[pos:]
		
		item = reduce(p1, p2)
		summation += priority(item)
	
	solution = summation
	
	print(f'Puzzle 1 solution: {solution}')

def badge(str1, str2, str3):
	for char in str1:
		if str2.count(char):
			if str3.count(char):
				return char

def puzzle2():
	summation = 0
	
	for i in range(0, len(data), 3):
		idx = i
		item = badge(data[idx], data[idx + 1], data[idx + 2])
		summation += priority(item)
	
	solution = summation
	
	print(f'Puzzle 2 solution: {solution}')


# data = preprocess('example')
data = preprocess('input')
puzzle1()
puzzle2()