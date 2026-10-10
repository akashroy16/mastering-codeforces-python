import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    a = [int(x) for x in data[1:n+1]]
    
    sorted_a = sorted(a)
    if a == sorted_a:
        print("yes")
        print("1 1")
        return
        
    l = 0
    while l < n and a[l] == sorted_a[l]:
        l += 1
        
    r = n - 1
    while r >= 0 and a[r] == sorted_a[r]:
        r -= 1
        
    a[l:r+1] = reversed(a[l:r+1])
    if a == sorted_a:
        print("yes")
        print(f"{l+1} {r+1}")
    else:
        print("no")

if __name__ == '__main__':
    solve()
