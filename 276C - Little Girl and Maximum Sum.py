import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    q = int(data[1])
    a = [int(x) for x in data[2:2+n]]
    
    diff = [0] * (n + 2)
    idx = 2 + n
    for _ in range(q):
        l = int(data[idx])
        r = int(data[idx+1])
        idx += 2
        diff[l] += 1
        diff[r + 1] -= 1
        
    freq = [0] * (n + 1)
    curr = 0
    for i in range(1, n + 1):
        curr += diff[i]
        freq[i-1] = curr
        
    a.sort(reverse=True)
    freq.sort(reverse=True)
    
    ans = sum(a[i] * freq[i] for i in range(n))
    print(ans)

if __name__ == '__main__':
    solve()
