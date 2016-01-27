from sys import argv

script,filename = argv

print "We are going to erase filename: " ,filename

#raw_input("?")

print "Opening file"
target = open(filename,'w')

print "Targetting the file....goodbye \n"
target.truncate()

print "Write first line \n"

line =raw_input("Enter the line:\n")
target.write(line)

target.close()