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
        
        max_val = max(a)
        b = [x for x in a if x != max_val]
        c = [x for x in a if x == max_val]
        
        if not b:
            out.append("-1")
        else:
            out.append(f"{len(b)} {len(c)}")
            out.append(" ".join(map(str, b)))
            out.append(" ".join(map(str, c)))
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
