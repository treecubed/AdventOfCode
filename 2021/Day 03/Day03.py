def process_line(line):
	line = line.rstrip()
	return line

with open('input.txt') as file:
	lines = file.readlines()
	lines = [process_line(line) for line in lines]

def puzzle1():
	bits = [[] for _ in range(len(lines[0]))]
	gamma_list = []
	epsilon_list = []

	for line in lines:
		for i in range(len(line)):
			bits[i].append(line[i])

	for bit in bits:
		count0 = bit.count('0')
		count1 = bit.count('1')
		if count1 > count0:
			gamma_list.append('1')
			epsilon_list.append('0')
		else:
			gamma_list.append('0')
			epsilon_list.append('1')

	gamma_bin = ''.join(gamma_list)
	epsilon_bin = ''.join(epsilon_list)

	gamma = int(gamma_bin, 2)
	epsilon = int(epsilon_bin, 2)

	solution = gamma * epsilon

	print(f'Puzzle 1 solution: {solution}')

def count_bit(list, bit):
	pass

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
# puzzle2()