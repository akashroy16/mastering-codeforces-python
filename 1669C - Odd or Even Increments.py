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
        a = [int(x) for x in data[idx+1:idx+1+n]]
        idx += 1 + n
        
        even_parity = a[0] % 2
        odd_parity = a[1] % 2
        possible = True
        for i in range(0, n, 2):
            if a[i] % 2 != even_parity:
                possible = False
                break
        for i in range(1, n, 2):
            if a[i] % 2 != odd_parity:
                possible = False
                break
        if possible:
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
