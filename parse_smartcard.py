import itertools

def open_file(filename):
	with open(filename) as f:
		result = [l.strip().split(",") for l in f]
	return result[1:]

def parse_raw(l):
	result = []
	for k, g in itertools.groupby(sorted(l, key = lambda e: e[0]), lambda e: e[0]):
		subgroup = itertools.groupby(sorted(g, key = lambda e: e[-2]), lambda e: 1 if float(e[-2])>0 else 0)
		#This is the tricky part, turn grouper (iterator-like) object into a list or when I try to sort or iterate later, it becomes empty
		subgroup = [(kk, list(gg)) for kk, gg in subgroup]
		if len(subgroup) == 2:
			g1, g2 = subgroup
			l1 = sorted(g1[1], key = lambda e: e[2])
			l2 = sorted(g2[1], key = lambda e: e[2])
			if len(l1) == len(l2):
				for i in range(len(l1)):
					result.append(l1.pop(0)[:4] + l2.pop(0)[2:])
	return result

if __name__ == "__main__":
	r = parse_raw(open_file("smartcard.txt"))
	with open("result.txt", 'w') as f:
		f.write('\n'.join([','.join(l) for l in r]))



