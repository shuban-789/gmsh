#!/usr/bin/python3
import gmsh
import sys
import os

def square():
    # INIT
    gmsh.initialize()
    gmsh.model.add("square")

    # POINTS --> (x, y, z, size, tag)
    size = 0.01
    gmsh.model.geo.addPoint(0, 0, 0, size, 1)
    gmsh.model.geo.addPoint(.1, 0, 0, size, 2)
    gmsh.model.geo.addPoint(.1, .1, 0, size, 3)
    gmsh.model.geo.addPoint(0, .1, 0, size, 4)

    # LINES --> (p1 tag, p2 tag, line tag)
    gmsh.model.geo.addLine(1, 2, 1)
    gmsh.model.geo.addLine(2, 3, 2)
    gmsh.model.geo.addLine(3, 4, 3)
    gmsh.model.geo.addLine(4, 1, 4)

    if '-al' in sys.argv:
        # LINE LOOP --> ([line tags], loop tag)
        gmsh.model.geo.addCurveLoop([1, 2, 3, 4], 1)
        gmsh.model.geo.addPlaneSurface([1], 1)

    gmsh.model.geo.synchronize()
    gmsh.model.addPhysicalGroup(1, [1, 2, 4], 5)
    gmsh.model.addPhysicalGroup(2, [1], name="Square Surface")

    gmsh.model.mesh.generate(2)

    gmsh.write("square.msh")

    gmsh.fltk.run()
    gmsh.finalize()
    
def cube():
    # INIT
    gmsh.initialize()
    gmsh.model.add("square")

    # POINTS --> (x, y, z, size, tag)
    size = 0.01
    gmsh.model.geo.addPoint(0, 0, 0, size, 1)
    gmsh.model.geo.addPoint(.1, 0, 0, size, 2)
    gmsh.model.geo.addPoint(.1, .1, 0, size, 3)
    gmsh.model.geo.addPoint(0, .1, 0, size, 4)
    gmsh.model.geo.addPoint(0, 0, .1, size, 5)
    gmsh.model.geo.addPoint(.1, 0, .1, size, 6)
    gmsh.model.geo.addPoint(.1, .1, .1, size, 7)
    gmsh.model.geo.addPoint(0, .1, .1, size, 8)

    # LINES --> (p1 tag, p2 tag, line tag)
    gmsh.model.geo.addLine(1, 2, 1)
    gmsh.model.geo.addLine(2, 3, 2)
    gmsh.model.geo.addLine(3, 4, 3)
    gmsh.model.geo.addLine(4, 1, 4)
    gmsh.model.geo.addLine(1, 5, 5)
    gmsh.model.geo.addLine(2, 6, 6)
    gmsh.model.geo.addLine(3, 7, 7)
    gmsh.model.geo.addLine(4, 8, 8)
    gmsh.model.geo.addLine(5, 6, 9)
    gmsh.model.geo.addLine(6, 7, 10)
    gmsh.model.geo.addLine(7, 8, 11)
    gmsh.model.geo.addLine(8, 5, 12)

    if '-al' in sys.argv:
        # LINE LOOP --> ([line tags], loop tag)
        gmsh.model.geo.addCurveLoop([1, 2, 3, 4], 1)
        gmsh.model.geo.addPlaneSurface([1], 1)

    gmsh.model.geo.synchronize()
    gmsh.model.addPhysicalGroup(1, [1, 2, 4], 5)
    gmsh.model.addPhysicalGroup(2, [1], name="Cube Surface")

    gmsh.model.mesh.generate(2)

    gmsh.write("cube.msh")

    gmsh.fltk.run()
    gmsh.finalize()

def clean():
    os.system("rm ./*.msh")

def main():
    if '-s' in sys.argv:
        square()
    elif '-c' in sys.argv:
        cube()
    elif "clean" in sys.argv:
        clean()
    else:
        print("Usage: main.py [-s | -c]")
    
if __name__ == "__main__":
    main()