import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    nums = [int(x) for x in data]
    nums.sort()
    
    abc = nums[3]
    a = abc - nums[2]
    b = abc - nums[1]
    c = abc - nums[0]
    
    print(a, b, c)

if __name__ == '__main__':
    solve()
