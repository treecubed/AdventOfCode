def process_line(line):
	line = line.rstrip().split()
	return line[0], int(line[1])

with open('input.txt') as file:
	lines = file.readlines()
	lines = [process_line(line) for line in lines]

def puzzle1():
	pos, depth = 0, 0

	for i in range(len(lines)):
		direction = lines[i][0]
		distance = lines[i][1]
		match direction:
			case 'forward':
				pos += distance
			case 'up':
				depth -= distance
			case 'down':
				depth += distance

	solution = pos * depth

	print(f'Puzzle 1 solution: {solution}')

def puzzle2():
	pos, depth, aim = 0, 0, 0

	for i in range(len(lines)):
		direction = lines[i][0]
		distance = lines[i][1]
		match direction:
			case 'forward':
				pos += distance
				depth += aim * distance
			case 'up':
				aim -= distance
			case 'down':
				aim += distance

	solution = pos * depth

	print(f'Puzzle 2 solution: {solution}')

puzzle1()
puzzle2()