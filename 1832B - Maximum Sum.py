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
        
        a.sort()
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] + a[i]
            
        max_sum = 0
        for i in range(k + 1):
            left = 2 * i
            right = n - (k - i)
            current_sum = pref[right] - pref[left]
            max_sum = max(max_sum, current_sum)
        out.append(str(max_sum))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
