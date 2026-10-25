import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for _ in range(t):
        n = int(data[idx])
        a = int(data[idx+1])
        b = int(data[idx+2])
        idx += 3
        res = []
        for i in range(n):
            res.append(alphabet[i % b])
        out.append("".join(res))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
