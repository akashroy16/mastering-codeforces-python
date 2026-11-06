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
        
        max_sum = a[0]
        curr_sum = a[0]
        for i in range(1, n):
            if abs(a[i]) % 2 == abs(a[i-1]) % 2:
                curr_sum = a[i]
            else:
                curr_sum = max(a[i], curr_sum + a[i])
            max_sum = max(max_sum, curr_sum)
        out.append(str(max_sum))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
