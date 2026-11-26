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
        m = int(data[idx + 1])
        idx += 2
        words = data[idx : idx + n]
        idx += n
        used = 0
        count = 0
        for w in words:
            if used + len(w) <= m:
                used += len(w)
                count += 1
            else:
                break
        out.append(str(count))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
