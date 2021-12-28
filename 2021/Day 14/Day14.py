from collections import Counter

def process_template(line):
	line = line.rstrip()
	c = Counter()
	for i in range(len(line) - 1):
		c.update([line[i] + line[i + 1]])
	return c, line

def process_rule(line):
	line = line.rstrip().split()
	rule = [line[0], [line[0][0] + line[2], line[2] + line[0][1]]]
	return rule

def read_input():
	with open('input.txt') as file:
		data = file.readlines()
		pairs, template = process_template(data[0])
		rules = [process_rule(rule) for rule in data[2:]]
		rules = dict(rules)
		return pairs, rules, template

def count(pairs, template):
	cnt = Counter()
	for i in pairs:
		cnt[i[0]] += pairs[i]
	cnt.update(template[-1])
	return cnt

def do_step(pairs, rules):
	cnt = Counter()
	for i in pairs:
		for rule in rules[i]:
			cnt[rule] += pairs[i]
	return cnt

def run_steps(pairs, rules, num):
	for i in range(num):
		# print(f'Step {i}')
		pairs = do_step(pairs, rules)
	return pairs

def puzzle1():
	pairs, rules, template = read_input()
	
	pairs = run_steps(pairs, rules, 10)
	cnt = count(pairs, template)
	mc = cnt.most_common()
	print(mc)
	
	solution = mc[0][1] - mc[-1][1]
	
	print(f'Puzzle 1 solution: {solution}')

def puzzle2():
	pairs, rules, template = read_input()
	
	pairs = run_steps(pairs, rules, 40)
	cnt = count(pairs, template)
	mc = cnt.most_common()
	print(mc)
	
	solution = mc[0][1] - mc[-1][1]
	
	print(f'Puzzle 2 solution: {solution}')

puzzle1()
puzzle2()