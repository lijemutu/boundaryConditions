import pyvista as pv
import numpy as np

meshBigFile = 'BC/E13_outer.stl'
meshSmallFile = 'BC/E15_outer.stl'

meshSmall = pv.PolyData(meshSmallFile)
meshBig = pv.PolyData(meshBigFile)


meshSmallNormals = meshSmall.compute_normals(point_normals=True, cell_normals=False,
                                             auto_orient_normals=True)
pp = pv.Plotter()
meshSmallNormals["distances"] = np.empty(meshSmall.n_points)
meshSmallNormals["surfacePoints"] = np.empty([meshSmall.n_points, 3])
normalVectors = np.empty([meshSmall.n_points, 6])
for i in range(meshSmallNormals.n_points):
    p = meshSmallNormals.points[i]
    #vec = meshSmallNormals["Normals"][i] * meshSmallNormals.length
    vec = meshSmallNormals["Normals"][i]*2

    p0 = p - vec
    p1 = p + vec
    ip, ic = meshBig.ray_trace(p0, p1, first_point=True)
    meshSmallNormals["surfacePoints"][i] = ip
    dist = np.sqrt(np.sum((ip - p)**2))
    meshSmallNormals["distances"][i] = dist
    if i % 8 == 0:
        ray = pv.Line(p, ip)
        pp.add_mesh(ray, color="blue", line_width=3, label="Ray Segment")


normalVectors[:, 0:3] = meshSmall.points
normalVectors[:, 3:] = meshSmallNormals["surfacePoints"]-meshSmall.points

np.savetxt("E13-E15outer.csv",normalVectors)


# Replace zeros with nans
mask = meshSmallNormals["distances"] == 0
meshSmallNormals["distances"][mask] = np.nan




#pp.add_mesh(meshSmall, opacity=0.75 ,smooth_shading=True)
#pp.add_mesh(meshBig, opacity=0.75, smooth_shading=True)
pp.add_mesh(meshSmallNormals, opacity=0.60,
            scalars="distances", smooth_shading=True)
pp.add_mesh(meshBig, color=True, opacity=0.60, smooth_shading=True)
pp.show_grid()
pp.show()
