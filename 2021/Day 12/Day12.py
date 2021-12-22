def process_line(line):
	line = line.rstrip()
	return line

with open('input.txt') as file:
	data = file.readlines()
	data = [process_line(line) for line in data]

# if large letter can go to any child cave
# small letter can only go to connected large letter or end


def puzzle1():
	
	
	
	solution = 0
	
	print(f'Puzzle 1 solution: {solution}')

def puzzle2():
	
	
	
	solution = 0
	
	print(f'Puzzle 2 solution: {solution}')

puzzle1()
puzzle2()