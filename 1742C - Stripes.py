import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        grid = data[idx:idx+8]
        idx += 8
        
        found_red = False
        for row in grid:
            if row == "R" * 8:
                found_red = True
                break
        if found_red:
            out.append("R")
        else:
            out.append("B")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
