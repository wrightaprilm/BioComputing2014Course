#! /usr/bin/env python 	

import sys

## Functions have special types of comments called docstrings, which
## are declared with triple quotes: '''docstring'''
## These aren't just good form, they're very useful at the interpreter. Try:
## 
## >>> import expenditures_4
## >>> help(expenditures_4)
##
## >>> help(expenditures_4.print_exps)

def parse_file(infile):
	'''Open infile and return a list of lists. Each inner list is 
	a line split on commas.'''
	with open(infile) as f:
		line_list = [line.strip().split(',') for line in f]
	return line_list

def print_exps(infile):
	'''Call parse_file and print a summary of expenditures from infile.'''
	lines = parse_file(infile)
	for line in lines[1:]:
		print "Spent %s at %s" % (line[-1],line[0])

if __name__ == '__main__': 	# Read: "if I (__name__) am being executed from
	infile = sys.argv[1]	# the command line (__main__), do the below"
	print_exps(infile)
	
## This file is now a very nice piece of Python code.  It can be executed from
## the command line. It can be imported at the interpreter properly, and its
## functions can be accessed like this: expenditures_4.print_exps("homework.csv")
## Or the functions can be imported independently with, for instance: 
## "from expenditures_4 import parse_file".
