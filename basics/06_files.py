# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
# Skip everything that is NOT a DSPAM line.
# "not" keyword ask: "what am I KEEPING vs what am I SKIPPING?”
# Your loop is a filtering system.
    if line.startswith("X-DSPAM-Confidence:"):

''' 
Case B (if you remove not but keep structure)
if line.startswith(...):
    continue
print(line)
'''

'''
Now:

skip DSPAM lines
print everything else

So it feels reversed, but the logic is consistent.
'''        
        # break
        continue
    print(line)
print("Done)

============================


