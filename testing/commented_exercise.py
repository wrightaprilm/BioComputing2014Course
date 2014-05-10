master_list = ['a','p','r','i','l','5','1','2','9','4','0']

def keep_em_separated():
    try:
        type(master_list) is list
	print "Input passes check"
    except TypeError:
	"This isn't a list. Feed me a list!"

    alpha_list = []
    num_list = []
    for value in master_list:
        print value
        if value.isdigit():
#Forgetting the () on the isdigit is a big source of error in this type of filtration. Try removing these and see what occurs. A simple mistake like this is why we test!
            num_list.append(value)
        if value.isalpha():
            alpha_list.append(value)

    print num_list
    print alpha_list
 #   num_list = ['1','2','3','a']
#Try uncommenting the above line to see what happens if a letter got in our list
    for x in num_list:
        if x.isdigit() == False:
		print "This is not a digit. Check the above function."
		return
    return(num_list)
    

def sum_nums():
    sum = 0
    num_list = keep_em_separated()
    for x in num_list:
	x = int(x)
	sum += x
    print sum
    try: 
	int(sum) == True
	print "The sum is %i" % sum
    except TypeError:
	print "Your sum isn't a number. That seems odd."
    try:
        10 < sum < 15
    except ValueError:
        print "Sum is implausible"
    return(sum)
    

	

