'''
6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
'''

text = "X-DSPAM-Confidence:    0.8475"
# Extract characters from index 23 to the end
#num = text.find('0.8475')

# search for the marker
pos = text.find(':')
# extract relative to that marker
num = text[pos+1:]
num = num.lstrip()

num = float(num)
print(num)

'''
Slice From an Index
To extract a chunk of text starting from that index to the end of the string, use a colon : after the variable.
'''
# store index in a variable 
#output = text[num: ]) 

# convert str to floating point number
# num = float(num)



'''
You've actually just learned a reusable programming pattern:

1. Find where something starts.
2. Store the index.
3. Use the index in a slice.
4. Convert if necessary.
'''

