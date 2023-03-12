from node import OrthogonalNode
from structure import OrthogonalList
from util import util


def show(m):
    for row in m:
        for num in row:
            if num is None:
                print("{}".format(num), end=' ')
            else:
                print("{:4}".format(num), end=' ')
        print()


def prim(m:list) -> list:
    lowcost = [i for i in m[0]] # 保存相连顶点间边的权值;V0作为最小生成树的根开始遍历,权值为0;初始化为0行的权值
    adjvex = [0 for i in m[0]] # 保存相连顶点;V0作为第一个加入,初始化全部为V0
    ans = [[None for i in m] for j in m]
    for row in m[1:]:
        mincost = 9999
        k = 0
        for j in range(1, len(row)):
            if lowcost[j] != 0 and lowcost[j] < mincost:
                mincost = lowcost[j]
                k = j
                
        ans[adjvex[k]][k] = mincost
        lowcost[k] = 0 # 将当前顶点的权值设为0,表示此顶点已完成任务,进行下一个顶点的遍历

        # 邻接矩阵k行逐个遍历全部顶点
        for j in range(1, len(row)):
            if lowcost[j] != 0 and m[k][j] < lowcost[j]:
                lowcost[j] = m[k][j]
                adjvex[j] = k
    return ans


def kruskal(nodes:list, links:list) -> list:
    n, count = len(nodes), 0
    min_mat = [[0 for i in range((n))] for j in range(n)]
    node_tags = list(range(n)) 
    for link in sorted(links, key=lambda x: x.weight):
        tail_index = nodes.index(link.tnode)
        head_index = nodes.index(link.hnode)
        if node_tags[tail_index] != node_tags[head_index]:
            min_mat[tail_index][head_index] = link.weight
            count += 1
            # print(count)
            temp = node_tags[head_index]
            for index in range(n):
                if node_tags[index] == temp:
                    node_tags[index] = node_tags[tail_index]
        if count == n-1:
            break
    return min_mat

if __name__ == "__main__":
    m = [[   0,  10,9999,9999,9999,  11,9999,9999,9999],
         [  10,   0,  18,9999,9999,9999,  16,9999,  12],
         [9999,  18,   0,  22,9999,9999,9999,9999,   8],
         [9999,9999,  22,   0,  20,9999,9999,  16,  21],
         [9999,9999,9999,  20,   0,  26,9999,   7,9999],
         [  11,9999,9999,9999,  26,   0,  17,9999,9999],
         [9999,  16,9999,9999,9999,  17,   0,  19,9999],
         [9999,9999,9999,  16,   7,9999,  19,   0,9999],
         [9999,  12,   8,  21,9999,9999,9999,9999,   0]]

    mat = [ [ 0, 10,  0,  0,  0, 11,  0,  0,  0],
            [10,  0, 18,  0,  0,  0, 16,  0, 12],
            [ 0, 18,  0, 22,  0,  0,  0,  0,  8],
            [ 0,  0, 22,  0, 20,  0,  0, 16, 21],
            [ 0,  0,  0, 20,  0, 26,  0,  7,  0],
            [11,  0,  0,  0, 26,  0, 17,  0,  0],
            [ 0, 16,  0,  0,  0, 17,  0, 19,  0],
            [ 0,  0,  0, 16,  7,  0, 19,  0,  0],
            [ 0, 12,  8, 21,  0,  0,  0,  0,  0] ]

    
    show( prim(m) )

    nodes = [OrthogonalNode(chr(65+i)) for i in range(9)]

    orthogonal_list = OrthogonalList(nodes)
    orthogonal_list.build_from_mat(mat)
    # util.show_mat( orthogonal_list.adjacencu_mat )
    util.show_mat( kruskal(orthogonal_list.node_list, orthogonal_list.link_list) )
