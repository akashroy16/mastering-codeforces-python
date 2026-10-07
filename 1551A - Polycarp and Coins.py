import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        c1 = n // 3
        c2 = n // 3
        
        if n % 3 == 1:
            c1 += 1
        elif n % 3 == 2:
            c2 += 1
            
        out.append(f"{c1} {c2}")
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
