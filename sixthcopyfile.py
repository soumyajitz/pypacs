from sys import argv
from os.path import exists

script, fromfile, tofile = argv

print "Copying from %s to %s" %(fromfile,tofile)

infile = open(fromfile)
indata = infile.read()

print "The input file is %d bytes long" %len(indata)

print "Does the output file exist? %r" %exists(tofile)

outfile = open(tofile,'w')
outfile.write(indata)

print "Done"

outfile.close()
infile.close()