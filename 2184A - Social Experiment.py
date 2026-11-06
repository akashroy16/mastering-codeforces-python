import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        n = int(data[i])
        if n % 2 == 0:
            out.append("0")
        else:
            out.append("1")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
