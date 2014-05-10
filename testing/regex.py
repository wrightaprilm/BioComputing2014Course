import os
import re
def get_list():
    file_list = []
    for file in os.listdir('.'):
        if file.startswith('ExaML_result'):
            file_list.append(file)
    print file_list
    if not os.path.exists('./rooted/'):
        os.makedirs('./rooted/')
    return file_list


   
    
def root_tree(): 
    file_list = get_list()
    type(file_list)
    for file in file_list:
	f = open(file)
        for line in f: 
            line = line.replace('Mabuya_sloanii', '')
        outfile = open('./rooted/%s' % file, 'w')
        outfile.write(line)

root_tree()
            


	
