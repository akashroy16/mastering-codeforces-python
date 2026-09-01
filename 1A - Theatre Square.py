import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n, m, a = int(input_data[0]), int(input_data[1]), int(input_data[2])
    
    flagstones_n = (n + a - 1) // a
    flagstones_m = (m + a - 1) // a
    
    print(flagstones_n * flagstones_m)

if __name__ == '__main__':
    main()
