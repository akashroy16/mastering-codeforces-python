import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    a = int(data[0])
    b = int(data[1])
    
    different = min(a, b)
    same = (max(a, b) - different) // 2
    
    print(different, same)

if __name__ == '__main__':
    solve()
