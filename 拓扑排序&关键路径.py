from node import AdjacencyNode
from structure import AOENetwork


def topological_sort(aoenet:AOENetwork) -> list:
    indegrees = [degree for degree in aoenet.indegree_list]
    sorted_nodes = list()
    length = len(aoenet)
    while len(sorted_nodes) < length:
        for i in range(length):
            if indegrees[i] == 0 and aoenet[i] not in sorted_nodes:
                sorted_nodes.append(aoenet[i])
                node = aoenet[i].next_node
                break
        while node:
            indegrees[ aoenet.node_list.index(node.value) ] -= 1
            node = node.next_node
    return [node.value for node in sorted_nodes]


if __name__ == "__main__":
    m0 = [[0,1,1, 1,0,0, 0,0,0, 0,0,0, 0,0,0], # 0
         [0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0], # 1
         [0,0,0, 0,0,1, 1,0,1, 1,0,0, 0,0,0], # 2
         [0,0,0, 0,0,0, 1,1,0, 1,0,0, 0,0,0], # 3
         [0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0], # 4
         [0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0], # 5
         [0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0], # 6
         [0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0], # 7
         [0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0], # 8
         [0,0,0, 0,0,0, 1,0,0, 0,1,0, 0,0,0], # 9
         [0,0,0, 0,0,0, 0,0,0, 0,0,1, 0,0,0], # 10
         [0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0], # 11
         [0,0,0, 1,0,0, 0,0,0, 0,0,0, 0,1,0], # 12
         [0,1,1, 0,0,0, 0,0,0, 0,0,0, 0,0,1], # 13
         [0,0,0, 0,1,0, 0,0,0, 0,0,0, 0,0,0]] # 14
    d0 = dict()
    for i in range(15):
        d0[i] = AdjacencyNode(i+1)
          
            #0  #1  #2  #3  #4  #5  #6  #7  #8
    m1 = [[ 0,  6,  4,  5, -1, -1, -1, -1, -1], # 0
          [-1,  0, -1, -1,  1, -1, -1, -1, -1], # 1
          [-1, -1,  0, -1,  1, -1, -1, -1, -1], # 2
          [-1, -1, -1,  0, -1,  2, -1, -1, -1], # 3
          [-1, -1, -1, -1,  0, -1,  7,  5, -1], # 4
          [-1, -1, -1, -1, -1,  0, -1,  4, -1], # 5
          [-1, -1, -1, -1, -1, -1,  0, -1,  2], # 6
          [-1, -1, -1, -1, -1, -1, -1,  0,  4], # 7
          [-1, -1, -1, -1, -1, -1, -1, -1,  0]] # 8
    d1 = dict()
    for i in range(9):
        d1[i] = AdjacencyNode(i+1)

    aoenet = AOENetwork(list(d1.values()))
    aoenet.build_from_adjacency_mat(m1)
    # print(aoenet.indegree_list)
    # aoenet.show()
    # print(topological_sort(aoenet))
    print( aoenet.topological_sort() ) 
    
    print( aoenet.critical_path() )
    print( aoenet.critical_path_weights)