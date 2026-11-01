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
        a1 = int(data[idx])
        a2 = int(data[idx+1])
        a4 = int(data[idx+2])
        a5 = int(data[idx+3])
        idx += 4
        
        max_f = 0
        for a3 in [a1 + a2, a4 - a2, a5 - a4]:
            c = 0
            if a3 == a1 + a2: c += 1
            if a4 == a2 + a3: c += 1
            if a5 == a3 + a4: c += 1
            max_f = max(max_f, c)
        out.append(str(max_f))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
