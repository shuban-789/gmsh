#!/usr/bin/python3
import gmsh
import sys
import os
import numpy as np

def dodecahedron_points() -> set:
    phi = (1 + np.sqrt(5)) / 2

    vertices = [
        (+-1, +-1, +-1),
        (0, +-1, +-phi), 
        (+-1, +-phi, 0), 
        (+-phi, 0, +-1)
    ]

    points = set()
    for x, y, z in vertices:
        for sx in [-1, 1]:
            for sy in [-1, 1]:
                for sz in [-1, 1]:
                    points.add((sx*x, sy*y, sz*z))

    return sorted(points)

def dodecahedron():
    # INIT
    gmsh.initialize()
    gmsh.model.add("dodecahedron")

    # POINTS --> (x, y, z, size, tag)
    size = 0.01
    points = dodecahedron_points()
    for i in range(len(points)):
        gmsh.model.geo.addPoint(points[i][0], points[i][1], points[i][2], size, i+1)
    

    # LINES --> (p1 tag, p2 tag, line tag)\
    index = 1
    for j in range(1, 20):
        for k in range(j+1, 20):
            gmsh.model.geo.addLine(j, k, index)
            index += 1

    gmsh.model.geo.synchronize()
    gmsh.model.addPhysicalGroup(1, [1, 2, 4], 5)
    gmsh.model.addPhysicalGroup(2, [1], name="Dodecahedron Surface")

    gmsh.model.mesh.generate(2)

    gmsh.write("dodecahedron.msh")

    gmsh.fltk.run()
    gmsh.finalize()    
    
def clean():
    os.system("rm ./*.msh")

def main():
    if '-d' in sys.argv:
        dodecahedron()
    elif "clean" in sys.argv:
        clean()
    else:
        print("Usage: main.py [-s | -c]")

if __name__ == '__main__':
    main()