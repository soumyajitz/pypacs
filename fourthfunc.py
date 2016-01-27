def print_two(*args):
	arg1,arg2 = args
	print "arg1 : %r, arg2 : %r" % (arg1,arg2)

print_two("Hello","World")

def add(a,b):
	return a+b;

a = add(2,3)
print a
