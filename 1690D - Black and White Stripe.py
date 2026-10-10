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
        s = data[idx+2]
        idx += 3
        curr_w = sum(1 for i in range(k) if s[i] == 'W')
        min_w = curr_w
        for i in range(k, n):
            if s[i] == 'W':
                curr_w += 1
            if s[i - k] == 'W':
                curr_w -= 1
            if curr_w < min_w:
                min_w = curr_w
        out.append(str(min_w))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
