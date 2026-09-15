import sys
 
data = sys.stdin.read().split()
 
if data:
    n = int(data[0])
    
    p = int(data[1])
    x_levels = data[2:2 + p]
    
    q_offset = 2 + p
    q = int(data[q_offset])
    y_levels = data[q_offset + 1:q_offset + 1 + q]
    
    combined_levels = set(map(int, x_levels + y_levels))
    
    if len(combined_levels) == n:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")
