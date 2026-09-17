import sys
 
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    names = input_data[1:]
    
    db = {}
    result = []
    
    for name in names:
        if name not in db:
            db[name] = 1
            result.append("OK")
        else:
            count = db[name]
            result.append(f"{name}{count}")
            db[name] += 1
            
    print('\n'.join(result))
 
if __name__ == '__main__':
    main()
