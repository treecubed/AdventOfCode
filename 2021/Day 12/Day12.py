def process_line(line):
	line = line.rstrip().split('-')
	return line

with open('input.txt') as file:
	data = file.readlines()
	data = [process_line(line) for line in data]

# if large letter can go to any child cave
# small letter can only go to connected large letter or end

def get_valid_links(links, cave, dead_caves):
	valid_links = []
	for link in links:
		if link[0] == cave:
			if link[1] not in dead_caves:
				valid_links.append(link)
		if link[1] == cave:
			if link[0] not in dead_caves:
				valid_links.append([link[1],link[0]])
	return valid_links

def puzzle1():
	
	print(get_valid_links(data, 'start', []))
	
	solution = 0
	
	print(f'Puzzle 1 solution: {solution}')

def puzzle2():
	
	
	
	solution = 0
	
	print(f'Puzzle 2 solution: {solution}')

puzzle1()
puzzle2()