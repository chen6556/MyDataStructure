def dfs(m:list, start:int) -> list:
    
    def func(i):
        nonlocal m, marks
        for j in range(shape):
            if m[i][j] > 0 and j not in marks:
                marks.append(j)
                func(j)
    
    shape = len(m)
    marks = [start]
    func(start)
    return marks


def bfs(m:list, start:int) -> list:
    shape = len(m)
    temp = [start]
    marks = [start]
    while temp:
        lay = list()
        for i in temp:
            for j in range(shape):
                if m[i][j] != 0 and j not in marks:
                    marks.append(j)
                    lay.append(j)
        temp = lay
    return marks

if __name__ == "__main__":
    m = [[0,1,0,1,1,0,0,0],
         [1,0,1,0,1,0,0,0],
         [0,1,0,0,0,1,0,0],
         [1,0,0,0,0,0,1,0],
         [1,1,0,0,0,0,1,0],
         [0,0,1,0,0,0,0,0],
         [0,0,0,1,1,0,0,1],
         [0,0,0,0,0,0,1,0]]

    d = {0:'A', 1:'B', 2:'C', 3:'D',
         4:'E', 5:'F', 6:'G', 7:'H'}
         
    print("DFS:", [d[i] for i in dfs(m, 0)], sep=' ')
    # ['A', 'B', 'C', 'F', 'E', 'G', 'D', 'H']
    print("BFS:", [d[i] for i in bfs(m ,0)], sep=' ')
    # ['A', 'B', 'D', 'E', 'C', 'G', 'F', 'H']