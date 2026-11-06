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
        n = int(data[idx])
        k = int(data[idx+1])
        a = [int(x) for x in data[idx+2:idx+2+k]]
        idx += 2 + k
        
        max_piece = max(a)
        ops = 0
        for x in a:
            ops += (2 * x - 1)
        ops -= (2 * max_piece - 1)
        out.append(str(ops))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
