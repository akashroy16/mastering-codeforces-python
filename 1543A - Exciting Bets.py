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
        b = int(data[idx+1])
        idx += 2
        if a == b:
            out.append("0 0")
        else:
            diff = abs(a - b)
            moves = min(a % diff, diff - (a % diff))
            out.append(f"{diff} {moves}")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
