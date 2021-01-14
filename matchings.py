from igraph import *

#g = Graph.Full(6)
#g = Graph([(0,1), (1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (7,8)])
g = Graph.Full_Bipartite(3,5)
l = g.linegraph()
m = l.largest_independent_vertex_sets()
e = g.get_edgelist()
	
for i in range(len(m)):
    for j in range(len(m[i])):
        print("(", end='')
        print((e[m[i][j]][0] + 1), (e[m[i][j]][1] + 1), sep = ', ', end='')
        print(")", end=' ')
    print()
