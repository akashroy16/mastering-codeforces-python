import sys

def main():
    expression = sys.stdin.read().strip()
    if not expression:
        return
    
    numbers = expression.split('+')
    numbers.sort()
    
    print('+'.join(numbers))

if __name__ == '__main__':
    main()
