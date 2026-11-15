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
        c = data[idx + 1]
        idx += 2
        possible = False
        for i, char in enumerate(s):
            if char == c and i % 2 == 0:
                possible = True
                break
        out.append("YES" if possible else "NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
