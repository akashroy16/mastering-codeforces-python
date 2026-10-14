import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    k = int(data[0])
    a = [int(x) for x in data[1:13]]
    if k == 0:
        print(0)
        return
    a.sort(reverse=True)
    curr = 0
    months = 0
    for val in a:
        curr += val
        months += 1
        if curr >= k:
            print(months)
            return
    print("-1")

if __name__ == '__main__':
    solve()
