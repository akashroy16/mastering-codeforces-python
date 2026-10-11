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
        idx += 1
        best_idx = -1
        max_qual = -1
        for i in range(1, n + 1):
            a = int(data[idx])
            b = int(data[idx+1])
            idx += 2
            if a <= 10 and b > max_qual:
                max_qual = b
                best_idx = i
        out.append(str(best_idx))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
