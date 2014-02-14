#! /usr/bin/env python 	

import sys
			
infile = sys.argv[1] # Global variable - accessible anywhere in the script

## Variables within functions, like line_list, cannot be accessed outside
## of the function - they have what's called local "scope"

def parse_file(infile):
	with open(infile) as f:
		line_list = [line.strip().split(',') for line in f]
	return line_list

def print_exps(infile):
	lines = parse_file(infile)
	for line in lines[1:]:
		print "Spent %s at %s" % (line[-1],line[0])
		
print_exps(infile)
