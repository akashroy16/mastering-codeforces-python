import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    a = [int(x) for x in data[1:]]
    possible = False
    for i in range(1 << n):
        s = 0
        for j in range(n):
            if (i >> j) & 1:
                s += a[j]
            else:
                s -= a[j]
        if s % 360 == 0:
            possible = True
            break
    print("YES" if possible else "NO")

if __name__ == '__main__':
    solve()
