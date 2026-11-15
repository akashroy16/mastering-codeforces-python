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
        s = data[idx]
        idx += 1
        last = {'1': -1, '2': -1, '3': -1}
        ans = float('inf')
        for i, c in enumerate(s):
            last[c] = i
            mn = min(last.values())
            if mn != -1:
                ans = min(ans, i - mn + 1)
        out.append("0" if ans == float('inf') else str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
