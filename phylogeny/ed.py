
from rcviz import viz, callgraph

x = "AKSQ"
y = "DKLJ"

# D(x,y,i,j) computes the min number of insertions, deletions, substitutions
# to convert x[0..i] into y[0..j].
# @viz
def D(x,y,i,j):
	if j==-1:
		return i+1
	if i==-1:
		return j+1
	if x[i]==y[j]:
		return D(x,y,i-1,j-1)
	else:
		return min(1+D(x,y,i-1,j-1), 1+D(x,y,i-1,j), 1+D(x,y,i,j-1))

i, j = len(x)-1, len(y)-1
print(D(x,y,i,j))
# callgraph.render()