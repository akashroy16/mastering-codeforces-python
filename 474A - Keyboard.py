import sys

def solve():
    lines = sys.stdin.read().split()
    if not lines:
        return
    dir_ch = lines[0]
    s = lines[1]
    
    rows = ["qwertyuiop", "asdfghjkl;", "zxcvbnm,./"]
    shift = -1 if dir_ch == 'R' else 1
    
    res = []
    for ch in s:
        for r in rows:
            if ch in r:
                idx = r.index(ch)
                res.append(r[idx + shift])
                break
    print("".join(res))

if __name__ == '__main__':
    solve()
