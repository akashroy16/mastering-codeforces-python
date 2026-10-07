import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    idx = 1
    
    alex_happy = False
    for _ in range(n):
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        if a != b:
            alex_happy = True
            
    if alex_happy:
        print("Happy Alex")
    else:
        print("Poor Alex")

if __name__ == '__main__':
    solve()
