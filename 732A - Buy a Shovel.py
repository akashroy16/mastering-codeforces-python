import sys
 
def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    k = int(data[0])
    r = int(data[1])
    
    for x in range(1, 11):
        if (x * k) % 10 == 0 or (x * k) % 10 == r:
            print(x)
            break
 
if __name__ == '__main__':
    solve()
