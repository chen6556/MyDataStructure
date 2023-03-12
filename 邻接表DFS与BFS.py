from node import AdjacencyNode
from structure import AdjacencyList
from util import util


def dfs(adjacency_list:AdjacencyList, start:int) -> list:
    
    def func(node:AdjacencyNode):
        nonlocal marks
        temp = node.next_node
        while temp:
            if temp.value not in marks:
                marks.append(temp.value)
                func(temp.value)
            temp = temp.next_node

    marks = [adjacency_list[start]]
    func(adjacency_list[start])
    return [node.value for node in marks]


def bfs(adjacency_list:AdjacencyList, start:int) -> list:
    temp1 = [adjacency_list[start]]
    marks = [adjacency_list[start]]
    while temp1:
        lay = list()
        for node in temp1:
            temp2 = node.next_node
            while temp2: 
                if temp2.value not in marks:
                    lay.append( temp2.value )
                    marks.append( temp2.value )
                temp2 = temp2.next_node
        temp1 = lay
    return [ node.value for node in marks]
    
if __name__ == "__main__":
    m = [[0,1,0,1,1,0,0,0],
         [1,0,1,0,1,0,0,0],
         [0,1,0,0,0,1,0,0],
         [1,0,0,0,0,0,2,0],
         [1,1,0,0,0,0,1,0],
         [0,0,1,0,0,0,0,0],
         [0,0,0,1,1,0,0,1],
         [0,0,0,0,0,0,1,0]]

    d = {0:AdjacencyNode('A'), 
         1:AdjacencyNode('B'),
         2:AdjacencyNode('C'),
         3:AdjacencyNode('D'),
         4:AdjacencyNode('E'),
         5:AdjacencyNode('F'),
         6:AdjacencyNode('G'),
         7:AdjacencyNode('H')}


    adjacency_list = AdjacencyList(list(d.values()))
    adjacency_list.build_from_adjacency_mat(m)
    adjacency_list.show()
    # util.show_mat(t.adjacencu_mat)
    print("DFS:", adjacency_list.dfs(0), sep=' ')
    # ['A', 'B', 'C', 'F', 'E', 'G', 'D', 'H']
    print("BFS:", adjacency_list.bfs(0), sep=' ')
    # ['A', 'B', 'D', 'E', 'C', 'G', 'F', 'H']