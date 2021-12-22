from colorama import Fore
from colorama import Style
import copy

def process_line(line):
	line = line.rstrip()
	return line

with open('input.txt') as file:
	data = file.readlines()
	data = [[int(x) for x in process_line(line)] for line in data]

def deep_count(lst, char):
	count = 0
	for item in lst:
		if isinstance(item, list):
			count += deep_count(item, char)
		elif item == char:
			count += 1
	return count

def read(lst, p):
	if(
		0 <= p[0] < len(lst) and
		0 <= p[1] < len(lst[0])
	):
		return lst[p[0]][p[1]]
	else:
		return False
	
def write(lst, p, val):
	if(
		0 <= p[0] < len(lst) and
		0 <= p[1] < len(lst[0])
	):
		lst[p[0]][p[1]] = val

def increment(lst, p, inc = 1):
	val = read(lst, p)
	write(lst, p, val + inc)

def output(lst, p):
	print(lst[p[0]][p[1]])

def can_flash(lst, p):
	return read(lst, p) > 9

def do_flash(lst, p):
	if read(lst, p) > 9:
		for i in range(-1, 2):
			for j in range(-1, 2):
				increment(lst, (p[0] + i, p[1] + j))
		write(lst, p, float('-inf'))
		return True

def reset_flash(lst, p):
	if read(lst, p) < 0:
		write(lst, p, 0)

def foreach(lst, func, **kwargs):
	ret = []
	for i in range(len(lst)):
		row_ret = []
		for j in range(len(lst[0])):
			row_ret.append(func(lst, (i,j), **kwargs))
		ret.append(row_ret)
	return ret

def do_step(lst):
	flashes = 0
	foreach(lst, increment)
	while deep_count(foreach(lst, can_flash), True) > 0:
		flashes += deep_count(foreach(lst, do_flash), True)
	foreach(lst, reset_flash)
	return flashes

def display(lst):
	disp = ''
	for i in range(len(lst)):
		for j in range(len(lst[i])):
			if lst[i][j] == 0:
				disp += Fore.LIGHTWHITE_EX + Style.BRIGHT
			disp += str(lst[i][j]) + Style.RESET_ALL
		disp += '\n'
	print(disp)

def puzzle1():
	lst = copy.deepcopy(data)
	flashes = 0
	for i in range(100):
		flashes += do_step(lst)
	
	solution = flashes
	
	print(f'Puzzle 1 solution: {solution}')

def puzzle2():
	lst = copy.deepcopy(data)
	solution = 0
	total_count = len(lst) * len(lst[0])
	for i in range(1000):
		flashes = do_step(lst)
		print(f'Step: {i + 1}')
		display(lst)
		if total_count == flashes:
			solution = i
			break
	
	print(f'Puzzle 2 solution: {solution}')

puzzle1()
puzzle2()