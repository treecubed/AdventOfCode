def preprocess(file_name):
	
	def process_line(line):
		line = line.split()
		return int(line[1]), int(line[3]), int(line[5])
	
	def process_stack(lines):
		index = {}
		stack = {}
		for line in reversed(lines):
			if index:
				for i in index:
					try:
						char = line[index[i]]
					except IndexError:
						char = ' '
					if char.isalpha():
						stack[i].append(char)
			else:
				for i in line.replace(' ', ''):
					index[int(i)] = line.index(i)
					stack[int(i)] = []
		return stack
	
	with open(file_name + '.txt') as file:
		file_data = [line.rstrip() for line in file.readlines()]
		split_index = file_data.index('')
		move_data = [process_line(line) for line in file_data[split_index + 1:]]
		stack_data = process_stack(file_data[:split_index])
	
	return move_data, stack_data

def do_move(move):
	for i in range(move[0]):
		stacks[move[2]].append(stacks[move[1]].pop())

def get_top_items():
	items = ''
	for stack in stacks.values():
		try:
			items += stack[-1]
		except IndexError:
			items += ' '
	return items
	
def do_new_move(move):
	stacks[move[2]] += stacks[move[1]][-move[0]:]
	stacks[move[1]] = stacks[move[1]][:-move[0]]
	
def puzzle1():
	for move in moves:
		do_move(move)
	
	solution = get_top_items()
	
	print(f'Puzzle 1 solution: {solution}')


def puzzle2():
	for move in moves:
		do_new_move(move)
	
	solution = get_top_items()
	
	print(f'Puzzle 2 solution: {solution}')


# moves, stacks = preprocess('example')
moves, stacks = preprocess('input')
puzzle1()
# moves, stacks = preprocess('example')
moves, stacks = preprocess('input')
puzzle2()