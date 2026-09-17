import sys
 
faces = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}
 
data = sys.stdin.read().split()
 
if data:
    n = int(data[0])
    total = sum(faces[poly] for poly in data[1:])
    print(total)
