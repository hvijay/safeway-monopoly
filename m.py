#!/usr/bin/env python
import pprint

group_generators =	[
						('A', 500, 5),
						('B', 505, 5),
						('C', 510, 5),
						('D', 515, 5),
						('E', 521, 5),
						('F', 526, 5),
						('G', 531, 4),
						('H', 535, 4),
						('I', 539, 4),
						('J', 543, 4),
						('K', 547, 4),
						('L', 551, 4),
						('M', 555, 4),
						('N', 559, 4),
						('O', 563, 4),
						('P', 567, 4),
						('Q', 571, 4),
						('R', 575, 4), 
						('S', 579, 4),
						('T', 583, 4),
						('U', 587, 4),
						('V', 591, 4),
						('W', 595, 4),
						('X', 599, 4),
						('Y', 603, 4),
						('Z', 607, 4),

						('$', 611, 8),
						('?', 619, 8)
					]

groups = list() # groups that get a prize
valid = set() # all numbers in all groups to check validity of collected tickets

for t in group_generators:
	ltr, num, ln = t
	strs = set()
	for i in range(0, ln):
		s = "{0}{1}{2}".format(ltr, num + i, chr(ord('A') + i))
		strs.add(s)
	groups.append(strs)

valid = set([s for g in groups for s in g])
# pprint.pprint(groups)
# pprint.pprint(valid)

collected = 	[	
					"B509E", "A500A", "J546D", "$615E", 
					"C511B", "T584B", "P570D", "D516B", 
					"F526A", "L552B", "K548B", "C510A",
					"J546D", "A500A", "?620B", "$617G", 
					"L554D", "Q574D", "X599A", "A501B", 
					"?619A", "S580B", "I540B", "M557C", 
					"V591A", "R576B", "W596B", "K547A", 
					"Z609C", "H535A", "R576B", "V591A", 
					"$616F", "D516B", "N559A", "W598D", 
					"C511B", "T583A", "M555A", "Q571A", 
					"E523C", "M555A", "G534D", "W598D", 
					"?624F", "R577C", "Z609C", "C512C", 
					"N559A", "?624F", "W598D", "F530E", 
					"S580B", "?619A", "R576B", "$615E", 
					"Z610D", "P567A", "$612B", "F529D"
				]
				

for c in collected:
	if c not in valid:
		print "Invalid ticket: {0}".format(c)

for g in groups:
	for e in g:
		print "group {0}: {1} collected, {2} total".format(e[0][0], len(g & set(collected)), len(g))
		break

	if (g.issubset(collected)):
		print "WON: {0}".format(g)
