from util import util


def dijkstra(mat:list, start:int) -> dict and list:
    passed = [start] # 已遍历的点
    nopassed = [i for i in range(len(mat)) if i != start] # 未遍历的点
    weights = [i for i in mat[start]]
    # 错误写法: weights = mat[start]
    ways = dict()
    for i in range(len(mat)):
        ways[i] = [start]
    while nopassed:
        idx = nopassed[0]
        for i in nopassed:
            if 0 < weights[i] < weights[idx]:
                idx = i
        passed.append(idx)
        nopassed.remove(idx)
        
        for i in nopassed:
            if weights[idx] + mat[idx][i] < weights[i]:
                weights[i] = weights[idx] + mat[idx][i]
                ways[i] = ways[idx] + [idx]
    for i in range(len(mat)):
        ways[i].append(i)
    return weights, ways


def floyd(mat:list) -> dict and list:
    length = len(mat)
    weights = [[i for i in j] for j in mat]
    ways = [[i if 0<weights[j][i]<9999 else -1 for i in range(length)] for j in range(length)]
    util.show_mat(ways)
    for n in range(length):
        for i in range(length):
            for j in range(length):
                if weights[i][j] > weights[i][n] + weights[n][j]:
                    weights[i][j] = weights[i][n] + weights[n][j]
                    ways[i][j] = ways[i][n]
    return weights, ways


def serach(ways:list, start:int, end:int) -> list:
    ans = [start]
    temp = ways[start][end]
    while temp != -1:
        ans.append(temp)
        temp = ways[temp][end]
    return ans


if __name__ == "__main__":
          # 0   # 1  # 2  # 3  # 4  # 5  # 6  # 7  # 8
    m = [[   0,  10,9999,9999,9999,  11,9999,9999,9999], # 0
         [  10,   0,  18,9999,9999,9999,  16,9999,  12], # 1
         [9999,  18,   0,  22,9999,9999,9999,9999,   8], # 2
         [9999,9999,  22,   0,  20,9999,9999,  16,  21], # 3
         [9999,9999,9999,  20,   0,  26,9999,   7,9999], # 4
         [  11,9999,9999,9999,  26,   0,  17,9999,9999], # 5
         [9999,  16,9999,9999,9999,  17,   0,  19,9999], # 6
         [9999,9999,9999,  16,   7,9999,  19,   0,9999], # 7
         [9999,  12,   8,  21,9999,9999,9999,9999,   0]] # 8

    weights, ways = dijkstra(m, 0)
    print(ways)
    
    weights, ways = floyd(m)
    util.show_mat(ways)
    print(serach(ways, 5, 8))