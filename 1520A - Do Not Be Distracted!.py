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
        
        seen = set()
        suspicious = False
        prev = ''
        
        for ch in s:
            if ch != prev:
                if ch in seen:
                    suspicious = True
                    break
                seen.add(ch)
                prev = ch
                
        if suspicious:
            out.append("NO")
        else:
            out.append("YES")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
