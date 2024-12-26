import numpy as np

def vers_norm(point,center):
    a=center[0]
    b=center[1]
    c=center[2]
    point = (point[0]-a,point[1]-b,point[2]-c)
    x=-2*(point[0])
    y=-2*(point[1])
    z=-2*(point[2])
    vec= np.array([x,y,z])*-1
    vers=vec/np.linalg.norm(vec)
    return vers
