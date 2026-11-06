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
        a = [int(x) for x in data[idx+1:idx+1+n]]
        idx += 1 + n
        
        counts = [0] * 26
        res = []
        for count in a:
            for i in range(26):
                if counts[i] == count:
                    res.append(chr(ord('a') + i))
                    counts[i] += 1
                    break
        out.append("".join(res))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
