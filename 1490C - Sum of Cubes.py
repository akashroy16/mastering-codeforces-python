import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    
    cubes = set()
    for i in range(1, 10001):
        cubes.add(i**3)
        
    out = []
    for i in range(1, t + 1):
        x = int(data[i])
        found = False
        for a in range(1, int(x**(1/3)) + 1):
            if x - a**3 in cubes:
                found = True
                break
        if found:
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
