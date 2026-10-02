import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    tasks = [int(x) for x in data[2:2+m]]
    
    curr = 1
    ans = 0
    
    for house in tasks:
        if house >= curr:
            ans += house - curr
        else:
            ans += n - (curr - house)
        curr = house
        
    print(ans)

if __name__ == '__main__':
    solve()
