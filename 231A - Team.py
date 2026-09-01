import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    solved_count = 0
    
    idx = 1
    for _ in range(n):
        p, v, t = int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])
        if p + v + t >= 2:
            solved_count += 1
        idx += 3
        
    print(solved_count)

if __name__ == '__main__':
    main()
