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
        p = int(data[idx+1])
        a = [int(x) for x in data[idx+2:idx+2+n]]
        b = [int(x) for x in data[idx+2+n:idx+2+2*n]]
        idx += 2 + 2 * n
        
        villagers = sorted(zip(b, a))
        cost = p
        shared = 1
        for cost_b, cap_a in villagers:
            if cost_b >= p:
                break
            take = min(n - shared, cap_a)
            cost += take * cost_b
            shared += take
            if shared == n:
                break
        cost += (n - shared) * p
        out.append(str(cost))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
