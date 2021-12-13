def process_line(line):
	line = list(map(int, line.rstrip().split(',')))
	return line

with open('input.txt') as file:
	fishes = file.readline()
	fishes = process_line(fishes)

def sim_days(days):
	lst = fishes.copy()
	
	for i in range(days):
		# print(f'Start day: {i}')
		births = []
		for idx, fish in enumerate(lst):
			if fish:
				lst[idx] -= 1
			else:
				lst[idx] = 6
				births.append(8)
		lst.extend(births)
		# print(f'End day: {i}')
	return len(lst)

counts = {

}

def new_sim_days(days):
	lst = fishes.copy()
	for i in range(9):
		counts[i] = lst.count(i)
	for day in range(days):
		# print(f'Start day: {day}')
		for i in range(9):
			counts[i-1] = counts[i]
		counts[6] += counts[-1]
		counts[8] = counts[-1]
		counts[-1] = 0
		# print(f'End day: {day}')
	return sum(counts.values())

def puzzle1():
	solution = new_sim_days(80)
	
	print(f'Puzzle 1 solution: {solution}')

def puzzle2():
	
	solution = new_sim_days(256)
	
	print(f'Puzzle 2 solution: {solution}')

puzzle1()
puzzle2()