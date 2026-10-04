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
        
        if "..." in s:
            out.append("2")
        else:
            out.append(str(s.count('.')))
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
