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
        s = data[idx+1]
        idx += 2
        
        left = 0
        right = n - 1
        
        while left < right and s[left] != s[right]:
            left += 1
            right -= 1
            
        out.append(str(right - left + 1))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
