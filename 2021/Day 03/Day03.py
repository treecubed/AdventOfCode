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

def count_bit(in_list, index, bit):
	count = 0
	for item in in_list:
		if item[index] == bit:
			count +=1
	return count

def trim_list(in_list, index, bit):
	ret_list = []
	for item in in_list:
		if item[index] == bit:
			ret_list.append(item)
	return ret_list

def puzzle2():
	new_lines = lines.copy()
	for i in range(len(lines[0])):
		if len(new_lines) > 1:
			if count_bit(new_lines, i, '1') >= count_bit(new_lines, i, '0'):
				new_lines = trim_list(new_lines, i, '1')
			else:
				new_lines = trim_list(new_lines, i, '0')
		else:
			break
	og_rating = int(new_lines[0], 2)

	new_lines = lines.copy()
	for i in range(len(lines[0])):
		if len(new_lines) > 1:
			if count_bit(new_lines, i, '0') <= count_bit(new_lines, i, '1'):
				new_lines = trim_list(new_lines, i, '0')
			else:
				new_lines = trim_list(new_lines, i, '1')
		else:
			break
	cs_rating = int(new_lines[0], 2)

	solution = og_rating * cs_rating

	print(f'Puzzle 2 solution: {solution}')

puzzle1()
puzzle2()