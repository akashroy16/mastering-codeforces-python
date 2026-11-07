import sys

MOD = 10**9 + 7

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
        idx += 2
        out.append(str(pow(n, k, MOD)))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
