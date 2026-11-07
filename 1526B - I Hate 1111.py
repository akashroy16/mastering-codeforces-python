import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        x = int(data[i])
        possible = False
        for a in range(11):
            if x >= 111 * a and (x - 111 * a) % 11 == 0:
                possible = True
                break
        if possible:
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
