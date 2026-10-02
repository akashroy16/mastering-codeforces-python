import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        nums = [int(data[idx]), int(data[idx+1]), int(data[idx+2])]
        idx += 3
        nums.sort()
        out.append(str(nums[1]))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
