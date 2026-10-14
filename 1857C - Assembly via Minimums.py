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
        m = n * (n - 1) // 2
        b = [int(x) for x in data[idx+1:idx+1+m]]
        idx += 1 + m
        
        b.sort()
        a = []
        curr = 0
        for i in range(n - 1):
            a.append(b[curr])
            curr += (n - 1 - i)
        a.append(1000000000)
        out.append(" ".join(map(str, a)))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
