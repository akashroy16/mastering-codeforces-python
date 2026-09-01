import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    sum_x = sum_y = sum_z = 0
    
    idx = 1
    for _ in range(n):
        sum_x += int(data[idx])
        sum_y += int(data[idx + 1])
        sum_z += int(data[idx + 2])
        idx += 3
        
    if sum_x == 0 and sum_y == 0 and sum_z == 0:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
