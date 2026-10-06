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
        b = [int(x) for x in data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        a = [b[0]]
        for i in range(1, n):
            if b[i] < b[i-1]:
                a.append(b[i])
            a.append(b[i])
            
        out.append(str(len(a)))
        out.append(" ".join(map(str, a)))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
