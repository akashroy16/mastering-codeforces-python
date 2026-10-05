import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    
    height = 0
    used = 0
    
    while True:
        height += 1
        needed = height * (height + 1) // 2
        if used + needed <= n:
            used += needed
        else:
            height -= 1
            break
            
    print(height)

if __name__ == '__main__':
    solve()
