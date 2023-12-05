def preprocess(file_name):
	
	def process_line(line):
		line = line.rstrip()
		return line
	
	with open(file_name + '.txt') as file:
		file_data = file.readlines()
		file_data = [process_line(line) for line in file_data]
	
	return file_data

def sum_dir_sizes(threshold):
	total = 0
	for size in dir_sizes.values():
		if size <= threshold:
			total += size
	return total

def list_to_path(in_list):
	if len(in_list) <= 1:
		return '/'
	return in_list[0] + '/'.join(in_list[1:])

def puzzle1():
	open_dirs = []
	for line in data:
		# print(line)
		args = line.split()
		if args[0] == '$':
			if args[1] == 'cd':
				if args[2] == '..':
					open_dirs.pop()
				else:
					open_dirs.append(args[2])
					dir_sizes[list_to_path(open_dirs)] = 0
		elif args[0] == 'dir':
			pass
			# dir_sizes[args[1]] = 0
		elif args[0].isnumeric():
			for i in range(len(open_dirs)):
				dir_sizes[list_to_path(open_dirs[0:i+1])] += int(args[0])
		# print(open_dirs, dir_sizes)

	solution = sum_dir_sizes(100000)
	# print(dir_sizes)
	print(f'Puzzle 1 solution: {solution}')


def puzzle2():
	
	solution = 0
	
	total_space = 70000000
	target_space = 30000000
	free_space = total_space - dir_sizes['/']
	dir_sizes_list = list(dir_sizes.values())
	dir_sizes_list.sort()
	for size in dir_sizes_list:
		if free_space + size >= target_space:
			solution = size
			break
	
	print(f'Puzzle 2 solution: {solution}')


# data = preprocess('example')
data = preprocess('input')

dir_sizes = {'/': 0}

puzzle1()
puzzle2()