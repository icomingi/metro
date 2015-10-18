# -*- coding: utf-8 -*-
import json
import codecs
import itertools

def read_object_from_csv(filename):
	#line_2_entry = list_2_object(names)
	result = []
	with codecs.open(filename, "r", "utf-8") as f:
		for l in f:
			a, b, c = l.strip().replace(" ", "").split(",")
			result.append([a, int(b), int(c)])
	return result

def save_obj_2_json(obj, filename):
	with codecs.open(filename, "w", "utf-8") as f:
		json.dump(obj, f, ensure_ascii=False)

def read_object_from_json(filename):
	with codecs.open(filename, "r", "utf-8") as f:
		return json.loads(f.read())

def list_2_object(names):
	#assert len(l) == len(names)
	return lambda l: dict(zip(names, l))

def group_entry(l, names, start, end):
	line_2_entry = list_2_object(names)
	r = range(start, end+1)
	#print r
	result = [[] for i in r]
	#print len(result)
	for k, g in itertools.groupby(l, lambda e: e[1]):
		#print k
		if k in r:
			print k
			result[k-start].extend([line_2_entry(e) for e in g])
	return result

def check_sanity(l, d):
	keys = set(d.keys())
	# dirty_data = [e[0] for e in l if e[0] not in keys]
	# print '\n'.join(set(dirty_data))
	stations = set([e[0] for e in l])
	print "in keys not in csv"
	print '\n'.join(keys - stations)
	print "-"*20
	print "in csv not in keys"
	diff = list(stations - keys)
	print diff
	print '\n'.join(diff)

def test_group_entry():
	l = read_object_from_csv("Every5MinuteEnterForEachStation0401.csv")
	#sample = l
	#print sample
	r = group_entry(l, ["name", "minutegroup", "entry"], 53, 284)
	save_obj_2_json(r, "every5minute_entry0401.json")
	print "wrote success!"

def test_list_2_object():
	f = list_2_object(["name", "minutegroup", "entry"])
	print f
	print f(["a", "b", "c"])

def test_check_sanity():
	l = read_object_from_csv("Every5MinuteEnterForEachStation0401.csv")
	d = read_object_from_json("stations_by_name_with_alias.json")
	check_sanity(l, d)

if __name__ == "__main__":
	#test_group_entry()
	#test_list_2_object()
	test_check_sanity()