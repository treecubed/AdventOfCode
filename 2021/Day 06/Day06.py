def process_line(line):
	line = list(map(int, line.rstrip().split(',')))
	return line

with open('input.txt') as file:
	fishes = file.readline()
	fishes = process_line(fishes)

def sim_days(days):
	lst = fishes.copy()
	
	for i in range(days):
		print(f'Start day: {i}')
		births = []
		for idx, fish in enumerate(lst):
			if fish:
				lst[idx] -= 1
			else:
				lst[idx] = 6
				births.append(8)
		lst.extend(births)
		print(f'End day: {i}')
	return len(lst)

def new_sim_days(days):
	lst = fishes.copy()
	
	for i in range(days):
		print(f'Start day: {i}')
		lst = list(map(lambda x: x-1, lst))
		birth_count = lst.count(-1)
		births = [8] * birth_count
		lst = list(map(lambda x : 6 if (x == -1) else x, lst))
		lst.extend(births)
		print(f'End day: {i}')
	return len(lst)

def puzzle1():
	solution = sim_days(80)
	
	print(f'Puzzle 1 solution: {solution}')

def puzzle2():
	
	solution = new_sim_days(256)
	
	print(f'Puzzle 2 solution: {solution}')

puzzle1()
puzzle2()