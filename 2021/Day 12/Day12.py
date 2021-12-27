def process_line(line):
	line = line.rstrip().split('-')
	return line

with open('input.txt') as file:
	data = file.readlines()
	data = [process_line(line) for line in data]

# if large letter can go to any child cave
# small letter can only go to connected large letter or end

def can_revisit(path):
	for cave in set(path):
		match cave:
			case 'start', 'end':
				continue
			case _ if cave.islower():
				if path.count(cave) > 1:
					return False
	return True

def cave_valid(path, cave, part_2):
	if part_2:
		if can_revisit(path):
			if cave != 'start' and cave != 'end':
				return True
	return cave.lower() not in path

def get_sub_paths(links, path, part_2):
	sub_paths = []
	if not path: return []
	for link in links:
		for i in range(2):
			if link[i] == path[-1]:
				if cave_valid(path, link[i-1], part_2):
					lst = path.copy()
					lst.append(link[i-1])
					sub_paths.append(lst)
	return sub_paths

def get_paths(links, part_2):
	paths = [['start']]
	for path in paths:
		sub_paths = get_sub_paths(links, path, part_2)
		if sub_paths:
			paths.extend(sub_paths)
	
	pruned_paths = []
	for path in paths:
		if path[-1] == 'end':
			pruned_paths.append(path)
	
	return pruned_paths

def display(paths):
	for path in sorted(paths):
		print(','.join(path))

def puzzle1():
	
	paths = get_paths(data, False)
	
	# display(paths)
	
	solution = len(paths)
	
	print(f'Puzzle 1 solution: {solution}')

def puzzle2():
	
	paths = get_paths(data, True)
	
	# display(paths)
	
	solution = len(paths)
	
	print(f'Puzzle 2 solution: {solution}')

puzzle1()
puzzle2()