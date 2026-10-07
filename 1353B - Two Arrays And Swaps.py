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
        a = [int(x) for x in data[idx+2 : idx+2+n]]
        b = [int(x) for x in data[idx+2+n : idx+2+2*n]]
        idx += 2 + 2 * n
        
        a.sort()
        b.sort(reverse=True)
        
        for i in range(min(k, n)):
            if b[i] > a[i]:
                a[i] = b[i]
            else:
                break
                
        out.append(str(sum(a)))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
