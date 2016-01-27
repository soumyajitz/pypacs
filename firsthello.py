from sys import argv
# print "Hey"
script, first, second, third = argv
print "Hello World"
print "Hello again"
print "See ",100-25

cars = 100.0
print "There are",cars,"cars available"
eye_color = 'Blue'
print "Your eye color is:",eye_color
print round(1.745)

formatter = "%r %r %r %r"

print formatter %("one","two","three","four")

print "\n"

print "How old are you?\t"
#age = raw_input()
print "How tall are you?\t"
#height = raw_input()
#print "You are %r years old and your height is %r"%(age,height)


print "The Script name is: ",script
print "The first val is: ",first
print "The second val is: ",second
print "The third val is: ",third
prompt = '> '
comp = raw_input(prompt)
print "My comp name is:",comp
