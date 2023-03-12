def build_next(t:int) -> list:
    left, right = -1, 0
    next_ls = [-1 for i in range(len(t))]
    while right < len(t)-1:
        if left == -1 or t[right] == t[left] :
            left += 1
            right += 1
            if t[right] == t[left]:
                next_ls[right] = next_ls[left]
            else:
                next_ls[right] = left
        else:
            left = next_ls[left]
    return next_ls


def kmp(s:str, t:str) -> int:
    index_s = index_t = 0
    next_ls = build_next(t)
    print(next_ls)
    while index_s < len(s) and index_t < len(t):
        if index_t == -1 or s[index_s] == t[index_t]:
            index_s += 1
            index_t += 1
        else:
            index_t = next_ls[index_t]
    
    if index_t >= len(t):
        return  index_s - len(t)
    else:
        return -1

if __name__ == "__main__":
    s = "aaabbbcccddd"
    t = "bbcc"

    print(kmp(s, t))