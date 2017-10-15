"""
Author: Fernando Collado
Github: ForFer
"""

"""
Bellman-Ford algorithm implementation with adjacency and weight matrix
To see a more clear view of how the algorithm works, uncomment the prints
"""

def bellman_ford(graph, weights, start):

    #All vertices set to a weight of "inf"
    distance = [10e7 for _ in range(len(graph))]
    predecessor = [None for _ in range(len(graph))]

    distance[start] = 0 
    

    #print("Distance:", distance)
    for i in range(len(graph)-1):
        for j in range(len(weights)):
            for k in range(len(weights[j])):
                if weights[j][k]!=0:
                    w = weights[j][k]
                    #print("Edge:",j,k,"with weight:", w)
                    if distance[j] + w < distance[k]:
                        distance[k] = distance[j] + w
                        predecessor[k] = j
        #print("distance at iter ",i,distance)
        #print("predecessors", predecessor)

    for i in range(len(weights)):
        for k in range(len(weights)):
            w = weights[j][k]
            if distance[i] >= w + distance[k]:
                print("Error, graph contains a negative weight cycle")
    return distance, predecessor


  
def test():
    nodes =[
    [ 0,1,1,0,0 ],
    [ 0,0,1,1,1 ],
    [ 0,0,0,0,0 ],
    [ 0,1,1,0,0 ],
    [ 0,0,0,1,1 ]
    ]

    weights = [
    [ 0,-1,4,0,0 ],
    [ 0,0,3,2,2  ],
    [ 0,0,0,0,0  ],
    [ 0,1,5,0,0  ],
    [ 0,0,0,-3,0 ]
    ]
    
    
    a,b = bellman_ford(nodes, weights, 0)
    print(a,b)

if __name__=="__main__":
    test()
