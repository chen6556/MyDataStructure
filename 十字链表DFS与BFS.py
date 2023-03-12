from node import OrthogonalNode, OrthogonalLink
from structure import OrthogonalList
from util import util

def build_from_mat(d:dict, m:list) -> list:
    orthogonal_links = list()
    shape = len(m)
    for i in range(shape):
        temp = d[i]
        for j in range(shape):
            if m[i][j] > 0 : 
                orthogonal_links.append(OrthogonalLink(d[i], d[j], m[i][j]))
                temp.tlink = orthogonal_links[-1]
                temp = temp.tlink
    for j in range(shape):
        temp = d[j]
        for i in range(shape):
            if m[i][j] > 0:
                for link in orthogonal_links:
                    if link.tnode is d[i] and link.hnode is d[j]:
                        temp.hlink = link
                        temp = temp.hlink
                        break
    return orthogonal_links

def dfs(nodes:list, start:int) -> list:
      
      def func(node:OrthogonalNode):
            nonlocal marks
            temp = node.tlink
            while temp:
                if temp.hnode not in marks:
                    marks.append(temp.hnode)
                    func(temp.hnode)
                temp = temp.tlink
      marks = [ nodes[start] ]
      func(nodes[start])
      return [ node.value for node in marks ]


def bfs(nodes:list, start:int) -> list:
    temp0 = [ nodes[start] ]
    marks = [ nodes[start] ]
    while temp0:
        lay = list()
        for node in temp0:
            temp1 = node.tlink
            while temp1:
                if temp1.hnode not in marks:
                    lay.append( temp1.hnode )
                    marks.append( temp1.hnode )
                temp1 = temp1.tlink
        temp0 = lay    
    return [ node.value for node in marks ]

if __name__ == "__main__":
    m = [[0,1,0,1,1,0,0,0],
          [1,0,1,0,1,0,0,0],
          [0,1,0,0,0,1,0,0],
          [1,0,0,0,0,0,1,0],
          [1,1,0,0,0,0,1,0],
          [0,0,1,0,0,0,0,0],
          [0,0,0,1,1,0,0,1],
          [0,0,0,0,0,0,1,0]]

    d = {0:OrthogonalNode('A'), 
         1:OrthogonalNode('B'),
         2:OrthogonalNode('C'),
         3:OrthogonalNode('D'),
         4:OrthogonalNode('E'),
         5:OrthogonalNode('F'),
         6:OrthogonalNode('G'),
         7:OrthogonalNode('H')}


    orthogonal_list = OrthogonalList(list(d.values()))
    orthogonal_list.build_from_mat(m)

    ls = build_from_mat(d, m)
    
    util.show_mat(orthogonal_list.adjacencu_mat)

    # print( dfs(list(d.values()), 0) )
    print("DFS:", orthogonal_list.dfs(0), sep=' ')
    # ['A', 'B', 'C', 'F', 'E', 'G', 'D', 'H']
    # print( bfs(list(d.values()), 0) )
    print("DFS:", orthogonal_list.bfs(0), sep=' ')
    # ['A', 'B', 'D', 'E', 'C', 'G', 'F', 'H']