#!/usr/bin/python3
import gmsh

MESH = "./simple.msh"
OUTPUT = "./output.py"

def mesh2script(mesh: str):
    f = open(OUTPUT, "w")
    f.write("#!/usr/bin/python3\n")
    f.write("import gmsh\n")
    f.write("impoty numpy as np\n")
    f.write("\n")
    
    gmsh.initialize()
    gmsh.open(mesh)
    
    f.write("gmsh.initialize()\n")
    model_name = gmsh.model.getCurrent()
    f.write(f'gmsh.model.add("{model_name}")\n')
    f.write("\n")
    
    f.write("size = 0.01\n")
    
    node_tags, node_coords, _ = gmsh.model.mesh.getNodes()
    for i in range(len(node_tags)):
        x, y, z = node_coords[3 * i], node_coords[3 * i + 1], node_coords[3 * i + 2]
        f.write(f'gmsh.model.geo.addPoint({x}, {y}, {z}, size, {node_tags[i]})\n')
    f.write("\n")
    
    _, element_tags, node_connectivity = gmsh.model.mesh.getElements(dim=1)
    for i, tag in enumerate(element_tags[0]):
        start_node, end_node = node_connectivity[0][2 * i], node_connectivity[0][2 * i + 1]
        f.write(f"gmsh.model.geo.addLine({start_node}, {end_node}, {tag})\n")
    f.write("\n")
    
    _, surface_tags, _ = gmsh.model.mesh.getElements(dim=2)
    if len(surface_tags) > 0 and len(surface_tags[0]) > 0:
        f.write(f"gmsh.model.geo.addCurveLoop({list(element_tags[0])}, 1)\n")
        f.write(f"gmsh.model.geo.addPlaneSurface([1], 1)\n")
    f.write("\n")
    
    f.write("gmsh.model.geo.synchronize()\n")
    f.write("\n")

    physical_groups = gmsh.model.getPhysicalGroups()
    for dim, tag in physical_groups:
        entities = gmsh.model.getEntitiesForPhysicalGroup(dim, tag)
        name = gmsh.model.getPhysicalName(dim, tag)
        if name:
            f.write(f'gmsh.model.addPhysicalGroup({dim}, {entities}, name="{name}")\n')
        else:
            f.write(f"gmsh.model.addPhysicalGroup({dim}, {entities}, {tag})\n")
    f.write("\n")

    f.write("gmsh.model.mesh.generate(2)\n")
    f.write("gmsh.finalize()\n")

    f.close()
    gmsh.finalize()

if __name__ == "__main__":
    mesh2script(MESH)