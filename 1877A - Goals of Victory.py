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
        a = [int(x) for x in data[idx+1 : idx+n]]
        idx += n
        
        # Total efficiency sum across all teams is 0
        out.append(str(-sum(a)))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
