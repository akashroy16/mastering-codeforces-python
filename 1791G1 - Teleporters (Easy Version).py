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
        c = int(data[idx + 1])
        idx += 2
        a = [int(x) for x in data[idx : idx + n]]
        idx += n
        costs = [a[i] + i + 1 for i in range(n)]
        costs.sort()
        count = 0
        for cost in costs:
            if c >= cost:
                c -= cost
                count += 1
            else:
                break
        out.append(str(count))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
