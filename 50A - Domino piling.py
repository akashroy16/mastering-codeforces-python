import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    m, n = int(input_data[0]), int(input_data[1])
    print((m * n) // 2)

if __name__ == '__main__':
    main()
