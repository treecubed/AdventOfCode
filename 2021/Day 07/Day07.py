def process_line(line):
	line = list(map(int, line.rstrip().split(',')))
	return line

with open('input.txt') as file:
	crabs = file.readline()
	crabs = process_line(crabs)

def get_fuel_basic(start, pos):
	return abs(start - pos)

def get_fuel_advanced(start, pos):
	diff = abs(start - pos)
	fuel = int((diff * (diff + 1)) / 2)
	return fuel

def get_fuel_lists(lst, fuel_func):
	fuel_lists = []
	for i in range(min(lst), max(lst)):
		# print(i)
		fuel_list = [fuel_func(x, i) for x in lst]
		fuel_lists.append(fuel_list)
	return fuel_lists

def get_min_fuel(lst, fuel_function):
	min_fuel = float('inf')
	for fuel_list in get_fuel_lists(lst, fuel_function):
		fuel = sum(fuel_list)
		if fuel < min_fuel:
			min_fuel = fuel
	return min_fuel

def puzzle1():
	
	solution = get_min_fuel(crabs, get_fuel_basic)
	
	print(f'Puzzle 1 solution: {solution}')

def puzzle2():
	
	
	
	solution = get_min_fuel(crabs, get_fuel_advanced)
	
	print(f'Puzzle 2 solution: {solution}')

puzzle1()
puzzle2()