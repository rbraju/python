#!/usr/bin/python

# Strings and string operations
str = "Bank of America"

print "\n" + str + "\n" + '-' * 50

# Print 8th character in the string
print "8th character        : ", str[8]

# Print characters from index 5 to 6
print "5th & 6th index      : ", str[5:7]

# Print first 9 characters
print "First 9 characters   : ", str[:9]

# Print characters from 8th index to end
print "8th character to end : ", str[8:]

# Print last 7 characters
print "Last 7 characters    : ", str[-7:]


# Word split - Converts into list
words = str.split(' ')
print "Words                : ", words
print "Total words          : ", len(words)

print '-' * 50
# Concatenation
print str + ", San Jose.\n"
