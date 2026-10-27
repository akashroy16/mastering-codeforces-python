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
        a = [(int(data[idx+1+i]), i) for i in range(n)]
        b = [(int(data[idx+1+n+i]), i) for i in range(n)]
        c = [(int(data[idx+1+2*n+i]), i) for i in range(n)]
        idx += 1 + 3 * n
        
        a.sort(reverse=True)
        b.sort(reverse=True)
        c.sort(reverse=True)
        
        max_sum = 0
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if a[i][1] != b[j][1] and a[i][1] != c[k][1] and b[j][1] != c[k][1]:
                        max_sum = max(max_sum, a[i][0] + b[j][0] + c[k][0])
        out.append(str(max_sum))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
