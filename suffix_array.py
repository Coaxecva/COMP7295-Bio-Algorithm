seq = 'THECATISINTHEHAT'
query = 'HE'

# Problem1: find the first occurence of query in seq
#Problem2:  find occurences of query in seq

def  Search(SA, query):
	#print(m.start() for m in re.finditer(seq, query))
	l, r = 0, len(SA)-1
	while l <= r:
		mid = (l+r)//2
		#if SA[mid].startswith(query):
		if seq[SA[mid]:].startswith(query):
			return mid
		if query < seq[SA[mid]:]:
			r = mid  - 1
		else:
			l = mid + 1
	return -1

def BuildSA(seq):
	SA = []
	# print  out all suffixes
	for i in range(len(seq)):
		print(seq[i:])
		# srtore all suffixes into SA
		#SA.append(seq[i:])
		SA.append(i)
	# sort SA
	SA.sort(key=lambda k: seq[k:])
	return SA

def PrintSA(seq, SA):
	for i in range(len(SA)):
		print('%3d  %3d %s' % (i, SA[i], seq[SA[i]:]))

SA = BuildSA(seq)
PrintSA(seq, SA)
print(Search(SA, query) ) 
