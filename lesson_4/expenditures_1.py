#! /usr/bin/env python 	

# Above is the shebang line - it tells Unix how to translate your script
# into machine language (1s and 0s), using python. I can't put other 
# comments onto that line

with open("homework.csv") as f:
	line_list = [line.strip().split(',') for line in f]
		
for line in line_list[1:]:
	print "Spent %s at %s" % (line[-1],line[0]) # print prints to the screen
	
## Now how do I execute it?
## Give yourself permission! "chmod u+x expenditures_1.py"
