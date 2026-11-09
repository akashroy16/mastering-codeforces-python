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
        f = int(data[idx + 1])
        k = int(data[idx + 2])
        idx += 3
        a = [int(x) for x in data[idx : idx + n]]
        idx += n
        target = a[f - 1]
        a.sort(reverse=True)
        rem = a[k:]
        take = a[:k]
        in_take = target in take
        in_rem = target in rem
        if in_take and in_rem:
            out.append("MAYBE")
        elif in_take:
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
