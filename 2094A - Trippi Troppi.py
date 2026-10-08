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
        words = data[idx:idx+3]
        idx += 3
        ans = [word[0] for word in words]
        out.append("".join(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
