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
        a = [int(data[idx]), int(data[idx+1]), int(data[idx+2])]
        idx += 3
        for _ in range(5):
            a.sort()
            a[0] += 1
        out.append(str(a[0] * a[1] * a[2]))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
