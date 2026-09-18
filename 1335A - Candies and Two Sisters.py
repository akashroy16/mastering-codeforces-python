import sys
 
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(input_data[i])
        results.append(str((n - 1) // 2))
        
    print('\n'.join(results))
 
if __name__ == '__main__':
    main()
    
