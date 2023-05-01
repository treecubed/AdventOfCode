import re

def preprocess(file_name):
	
	def process_line(line):
		line = re.split(',|-', line.rstrip())
		line = [(int(line[0]), int(line[1])),(int(line[2]), int(line[3]))]
		
		return line
	
	with open(file_name + '.txt') as file:
		file_data = file.readlines()
		file_data = [process_line(line) for line in file_data]
	
	return file_data

def contains(set1, set2):
	# Does set 1 contain set 2?
	return (set1[0] <= set2[0]) and (set1[1] >= set2[1])

def puzzle1():
	contained_pairs = 0
	
	for pair in data:
		if contains(pair[0], pair[1]) or contains(pair[1], pair[0]):
			contained_pairs += 1
	
	solution = contained_pairs
	
	print(f'Puzzle 1 solution: {solution}')

def overlaps(set1, set2):
	return (set1[0] <= set2[0] <= set1[1]) or (set1[0] <= set2[1] <= set1[1])

def puzzle2():
	overlapped_pairs = 0
	
	for pair in data:
		if overlaps(pair[0], pair[1]) or overlaps(pair[1], pair[0]):
			overlapped_pairs += 1
	
	
	solution = overlapped_pairs
	
	print(f'Puzzle 2 solution: {solution}')


# data = preprocess('example')
data = preprocess('input')
puzzle1()
puzzle2()