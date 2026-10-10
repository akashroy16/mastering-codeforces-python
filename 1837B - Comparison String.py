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
        s = data[idx+1]
        idx += 2
        max_len = 1
        curr_len = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                curr_len += 1
            else:
                curr_len = 1
            if curr_len > max_len:
                max_len = curr_len
        out.append(str(max_len + 1))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
