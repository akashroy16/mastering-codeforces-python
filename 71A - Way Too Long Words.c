import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    words = input_data[1:n + 1]
    
    results = []
    for word in words:
        if len(word) > 10:
            results.append(f"{word[0]}{len(word) - 2}{word[-1]}")
        else:
            results.append(word)
            
    print('\n'.join(results))

if __name__ == '__main__':
    main()
