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
        
        max_sum = 0
        i = 0
        while i < n:
            curr_max = a[i]
            j = i
            while j < n and ((a[i] > 0 and a[j] > 0) or (a[i] < 0 and a[j] < 0)):
                curr_max = max(curr_max, a[j])
                j += 1
            max_sum += curr_max
            i = j
        out.append(str(max_sum))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
