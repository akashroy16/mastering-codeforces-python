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
        n = int(data[idx])
        x = int(data[idx+1])
        a = [int(v) for v in data[idx+2:idx+2+n]]
        idx += 2 + n
        
        odds = sum(1 for v in a if v % 2 != 0)
        evens = n - odds
        
        possible = False
        for o in range(1, min(odds, x) + 1, 2):
            e = x - o
            if 0 <= e <= evens:
                possible = True
                break
        if possible:
            out.append("Yes")
        else:
            out.append("No")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
