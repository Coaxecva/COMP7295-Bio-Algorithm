#Quang Tran (qmtran@memphis.edu)
#comp 7295 bioinfo alogirthm

def bwt(s):
	"""Apply Burrows-Wheeler transform to input string."""
	table = sorted(s[i:] + s[:i] for i in range(len(s)))  # Table of rotations of string
	last_column = [row[-1:] for row in table]  # Last characters of each row
	#print(table)
	return ("".join(last_column),   table.index(s))# Convert list of characters into string

def ibwt(r, idx):
	"""Apply inverse Burrows-Wheeler transform."""
	table = [""] * len(r)  # Make empty table
	for j in range(len(r)):
		table = sorted(r[i] + table[i] for i in range(len(r)))  # Add a column of r
	#print(table)
	return table[idx]  # Get rid of trailing null character

seq = "BANANA"

transform, i = bwt(seq)

print(transform, i)

print(ibwt(transform,i))
