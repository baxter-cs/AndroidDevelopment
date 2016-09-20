#!python2
# This script removes double spaces from any input text file.

# Here we open our input with the 'read' attribute
not_fixed = open('input file', 'r')
# And here we open our output with the 'write' attribute
fixed = open('output file', 'w')
# We initialize a buffer for holding processed lines
temp_fix = ""
for line in not_fixed:
    # replace() iterates over the current line from the input file
    temp_fix = line.replace("  ", " ")
    # Then we write the buffer to the output file
    fixed.write(temp_fix)