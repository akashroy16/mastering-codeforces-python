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
        
        gold = 0
        given = 0
        for x in a:
            if x >= k:
                gold += x
            elif x == 0 and gold > 0:
                gold -= 1
                given += 1
        out.append(str(given))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
