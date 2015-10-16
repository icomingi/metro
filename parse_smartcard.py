# -*- coding: utf-8 -*-

import itertools
import codecs
import re

SPLITTER = "\xba\xc5\xcf\xdf"

def open_file(filename):
	result = []
	with open(filename) as f:
		#result = [l.strip().split(",") for l in f]
		#for i in range(size_limit):
		for l in f:
			l = l.strip().replace(SPLITTER, ",").split(",")
			#print l
			#l = l.split(",")
			#print l
			if l[-3] == '\xb5\xd8\xcc\xfa':
				result.append(l)
	return result[1:]

def parse_raw(l):
	result = []
	for k, g in itertools.groupby(sorted(l, key = lambda e: e[0]), lambda e: e[0]):
		#print list(g)
		subgroup = itertools.groupby(sorted(g, key = lambda e: e[-2]), lambda e: 1 if float(e[-2])>0 else 0)
		#This is the tricky part, turn grouper (iterator-like) object into a list or when I try to sort or iterate later, it becomes empty
		subgroup = [(kk, list(gg)) for kk, gg in subgroup]
		if len(subgroup) == 2:
			g1, g2 = subgroup
			l1 = sorted(g1[1], key = lambda e: e[2])
			l2 = sorted(g2[1], key = lambda e: e[2])
			if len(l1) == len(l2):
				for i in range(len(l1)):
					result.append(l1.pop(0)[:5] + l2.pop(0)[2:])
	return result

def split_line_station(s):
	return s.split(SPLITTER)

def generate_sample(infilename, outfilename, lines=10):
	with open(infilename) as infile:
		with open(outfilename, "w") as outfile:
			for i in range(lines):
				outfile.write(infile.readline())
	print "wrote to %s success!" % outfilename

def test_process():
	#source = ["03", "04", "05", "06", "07", "08", "30"]
	source = ["30"]
	for s in source:
		r = parse_raw(open_file("SPTCC-201504%s.csv" % s))
		with open("commuter_201504%s.txt" % s, "w") as f:
			commuters = guess_commuter(r)
			#for c in commuters:
			#	f.write(c+"\n")
			f.write("\n".join(commuters))
		print "wrote %s commuter success!" % s
		with open("trip_201504%s.txt" % s, 'w') as f:
			for e in r:
				f.write(",".join(e)+"\n")
		print "wrote %s trip success!" % s
	print "entire writing success!"

def get_min(s):
	h, m, s = s.split(":")
	return int(h)*60 + int(m)

def guess_commuter(l):
	result = []
	for k, g in itertools.groupby(l, lambda e: e[0]):
		key_info = [(set([e[4], e[-4]]), get_min(e[2]), get_min(e[5])) for e in g]
		#print key_info
		for c1, c2 in itertools.combinations(key_info, 2):
			if c1[0] == c2[0] and (c2[1] - c1[-1] >= 60*5 or c1[1] - c2[-1] >= 60*5):
				result.append(k)
				break
		continue
	return result

def test_guess_commuter():
	with open("result_sample.txt") as f:
		lines = [l.strip().split(",") for l in f]
	print guess_commuter(lines)[:10]

if __name__ == "__main__":
	#generate_sample("SPTCC-20150401.csv", "SPTCC_Sample.txt")
	test_process()
	#print open_file("SPTCC_Sample.txt")
	#test_guess_commuter()


