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
        a = int(data[idx])
        b = int(data[idx + 1])
        c = int(data[idx + 2])
        x = int(data[idx + 3])
        y = int(data[idx + 4])
        idx += 5
        req_dogs = max(0, x - a)
        req_cats = max(0, y - b)
        if req_dogs + req_cats <= c:
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
