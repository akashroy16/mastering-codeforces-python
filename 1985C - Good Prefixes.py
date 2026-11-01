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
        
        pref_sum = 0
        max_val = 0
        ans = 0
        for x in a:
            pref_sum += x
            max_val = max(max_val, x)
            if pref_sum - max_val == max_val:
                ans += 1
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
