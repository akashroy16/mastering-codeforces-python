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
        a = [int(x) for x in data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        even_mismatch = 0
        odd_mismatch = 0
        
        for i in range(n):
            if i % 2 != a[i] % 2:
                if i % 2 == 0:
                    even_mismatch += 1
                else:
                    odd_mismatch += 1
                    
        if even_mismatch == odd_mismatch:
            out.append(str(even_mismatch))
        else:
            out.append("-1")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
