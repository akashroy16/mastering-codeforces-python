import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    x = 0
    
    for statement in input_data[1:n + 1]:
        if '+' in statement:
            x += 1
        else:
            x -= 1
            
    print(x)

if __name__ == '__main__':
    main()
