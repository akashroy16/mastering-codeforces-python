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
        a = [int(x) for x in data[idx : idx + n]]
        idx += n
        s = sum(a)
        rem = s % 3
        if rem == 0:
            out.append("0")
        elif rem == 2:
            out.append("1")
        else:
            has_rem1 = any(x % 3 == 1 for x in a)
            if has_rem1:
                out.append("1")
            else:
                out.append("2")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
