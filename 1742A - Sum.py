import sys
 
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    results = []
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        c = int(input_data[idx + 2])
        idx += 3
        
        if a + b == c or a + c == b or b + c == a:
            results.append("YES")
        else:
            results.append("NO")
            
    print('\n'.join(results))
 
if __name__ == '__main__':
    main()
