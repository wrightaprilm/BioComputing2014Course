#! /usr/bin/env python 	

import sys 	# import the module 'sys.' You can now access sys methods just
			# like you could access str and list methods
			
infile = sys.argv[1] 	# The argv method returns a list of commands at the 
						# command line. sys.argv[0] is the script, and sys.argv[1]
						# is the first argument variable (hence argv)

with open(infile) as f:
	line_list = [line.strip().split(',') for line in f]
		
for line in line_list[1:]:
	print "Spent %s at %s" % (line[-1],line[0]) # print prints to the screen
