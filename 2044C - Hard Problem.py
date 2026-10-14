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
        m = int(data[idx])
        a = int(data[idx+1])
        b = int(data[idx+2])
        c = int(data[idx+3])
        idx += 4
        
        row1 = min(m, a)
        row2 = min(m, b)
        rem1 = m - row1
        rem2 = m - row2
        row1 += min(rem1, c)
        c -= min(rem1, c)
        row2 += min(rem2, c)
        
        out.append(str(row1 + row2))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
