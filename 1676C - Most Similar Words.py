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
        m = int(data[idx + 1])
        idx += 2
        words = data[idx : idx + n]
        idx += n
        ans = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                cost = sum(abs(ord(words[i][k]) - ord(words[j][k])) for k in range(m))
                if cost < ans:
                    ans = cost
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
