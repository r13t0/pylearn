https://www.py4e.com/lectures3/Pythonlearn-06-Strings.pdf


🧠 The “split vs find” decision rule


≠====================
🔵 Use split() when:
======================__
The data is separated by a clear delimiter
label : value

text = "X-DSPAM-Confidence:    0.8475"

parts = text.split(':')
num = float(parts[1])

print(num)

==============================
🟡 Use find() + slicing when:
=========≠=====================

You need a position inside a messy or unstructured string

Or when:
there is no clean separator
you need partial extraction
you need offsets from a marker

pos = text.find(':')
num = text[pos+1:]
num = num.lstrip()

_===========
Slice From an Index
============

To extract a chunk of text starting from that index to the end of the string, use a colon : after the variable.

text = "Error: 404"
num = 7

# Slice from index 7 to the end
value = text[num:]

print(value)  # Output: 404


