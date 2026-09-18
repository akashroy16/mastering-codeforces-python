import sys
 
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    
    for i in range(1, t + 1):
        s = input_data[i]
        length = len(s)
        ans = []
        
        for idx, digit in enumerate(s):
            if digit != '0':
                ans.append(digit + '0' * (length - 1 - idx))
                
        results.append(str(len(ans)))
        results.append(" ".join(ans))
        
    print('\n'.join(results))
 
if __name__ == '__main__':
    main()
    
