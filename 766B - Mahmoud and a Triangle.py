import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    a = [int(x) for x in data[1:n+1]]
    
    a.sort()
    possible = False
    for i in range(n - 2):
        if a[i] + a[i+1] > a[i+2]:
            possible = True
            break
            
    if possible:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()
