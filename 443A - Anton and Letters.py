s = input().strip()
 
inner = s[1:-1]
 
if not inner:
    print(0)
else:
    letters = inner.split(', ')
    print(len(set(letters)))
