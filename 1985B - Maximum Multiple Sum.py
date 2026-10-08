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
        if n == 3:
            out.append("3")
        else:
            out.append("2")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
