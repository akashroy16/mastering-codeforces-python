import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    t = [int(x) for x in data[1:1+n]]
    
    p1, p2, p3 = [], [], []
    for i, val in enumerate(t, start=1):
        if val == 1:
            p1.append(i)
        elif val == 2:
            p2.append(i)
        elif val == 3:
            p3.append(i)
            
    w = min(len(p1), len(p2), len(p3))
    print(w)
    
    out = []
    for i in range(w):
        out.append(f"{p1[i]} {p2[i]} {p3[i]}")
        
    if out:
        print('\n'.join(out))

if __name__ == '__main__':
    solve()
