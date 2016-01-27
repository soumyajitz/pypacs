from sys import argv

script, filename = argv
txt = open(filename,'w')

print "The Filename is :%r" %filename
#print txt.read()
txt.write('New Line')
