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
        
        min_candy = min(a)
        eaten = sum(x - min_candy for x in a)
        out.append(str(eaten))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
