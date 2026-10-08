import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    v = [int(x) for x in data[1:n+1]]
    idx = n + 1
    m = int(data[idx])
    idx += 1
    
    u = sorted(v)
    pref_v = [0] * (n + 1)
    pref_u = [0] * (n + 1)
    for i in range(n):
        pref_v[i+1] = pref_v[i] + v[i]
        pref_u[i+1] = pref_u[i] + u[i]
        
    out = []
    for _ in range(m):
        type_q = int(data[idx])
        l = int(data[idx+1])
        r = int(data[idx+2])
        idx += 3
        if type_q == 1:
            out.append(str(pref_v[r] - pref_v[l-1]))
        else:
            out.append(str(pref_u[r] - pref_u[l-1]))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
