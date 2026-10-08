import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        s = data[i]
        c0 = s.count('0')
        c1 = s.count('1')
        moves = min(c0, c1)
        if moves % 2 == 1:
            out.append("DA")
        else:
            out.append("NET")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
