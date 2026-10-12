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
        b = [int(x) for x in data[idx+1:idx+1+n]]
        idx += 1 + n
        a = []
        left = 0
        right = n - 1
        while left <= right:
            if left == right:
                a.append(str(b[left]))
            else:
                a.append(str(b[left]))
                a.append(str(b[right]))
            left += 1
            right -= 1
        out.append(" ".join(a))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
