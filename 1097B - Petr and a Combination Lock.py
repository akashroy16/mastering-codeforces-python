import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    a = [int(x) for x in data[1:1+n]]
    
    possible = False
    for mask in range(1 << n):
        current_deg = 0
        for i in range(n):
            if (mask >> i) & 1:
                current_deg += a[i]
            else:
                current_deg -= a[i]
        if current_deg % 360 == 0:
            possible = True
            break
            
    if possible:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()
