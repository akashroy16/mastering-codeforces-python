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
        k = int(data[idx+1])
        p = int(data[idx+2])
        idx += 3
        
        if abs(k) > n * p:
            out.append("-1")
        else:
            out.append(str((abs(k) + p - 1) // p))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
