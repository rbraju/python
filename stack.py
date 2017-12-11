#!/usr/bin/python

stack = [1, 2, 3, 4, 5];

print stack

# Push
print "\nPush 6 and 7"
stack.append(6)
stack.append(7)
print stack, "\n"

# Pop
print "Pop", stack.pop()
print "Pop", stack.pop()
print stack
