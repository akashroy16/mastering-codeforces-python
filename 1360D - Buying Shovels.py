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
        idx += 2
        
        ans = n
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                if i <= k:
                    ans = min(ans, n // i)
                if n // i <= k:
                    ans = min(ans, i)
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
