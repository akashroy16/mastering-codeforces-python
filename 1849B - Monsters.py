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
        a = [int(x) for x in data[idx+2:idx+2+n]]
        idx += 2 + n
        
        monsters = []
        for i, val in enumerate(a):
            rem = val % k
            if rem == 0:
                rem = k
            monsters.append((-rem, i + 1))
        monsters.sort()
        ans = [str(m[1]) for m in monsters]
        out.append(" ".join(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
