import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    
    for i in range(1, t + 1):
        expr = data[i]
        out.append(str(int(expr[0]) + int(expr[2])))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
