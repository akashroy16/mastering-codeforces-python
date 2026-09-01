import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    matrix = [int(x) for x in input_data[:25]]
    one_index = matrix.index(1)
    
    row = one_index // 5
    col = one_index % 5
    
    moves = abs(row - 2) + abs(col - 2)
    print(moves)

if __name__ == '__main__':
    main()
