import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    idx = 1
    mishka = 0
    chris = 0
    
    for _ in range(n):
        m = int(data[idx])
        c = int(data[idx+1])
        idx += 2
        
        if m > c:
            mishka += 1
        elif c > m:
            chris += 1
            
    if mishka > chris:
        print("Mishka")
    elif chris > mishka:
        print("Chris")
    else:
        print("Friendship is magic!^^")

if __name__ == '__main__':
    solve()
