#wlasciwosci
import numpy as np

E=2.0e10
v=0.3
h=0.25
#geometria
w1=(-1,0)
w2=(0,0)
w3=(-1,12.359)
#pomocnicze
x32=w3[0]-w2[0]
x31=w3[0]-w1[0]
x21=w2[0]-w1[0]

y32=w3[1]-w2[1]
y31=w3[1]-w1[1]
y21=w2[1]-w1[1]

#obliczone
A=(1/2)*(x32*y21-x21*y32)*-1
A=6.179902628682753

B=(1/(2*A))*np.array([[y32,0,-y31,0,y21,0],
                      [0,-x32,0,x31,0,-x21],
                      [-x32,y32,x31,-y31,-x21,y21]])
B=np.array([[-1,0,1,0,0,0],
            [0,-0.08091,0,0,0,0.08091],
            [-0.08091,-1,0,1,0.08091,0]
            ])
vp=1
tp = (1 - v) / 2
D = (E/(1-v*v))*np.array([[vp, v, 0],
                [v, vp, 0],
                [0, 0, tp]])
z=np.zeros((3,3))
r1=np.hstack((D,z,z))
r2=np.hstack((z,D,z))
r3=np.hstack((z,z,D))
nD=np.vstack((r1,r2,r3))
ke1=h*A*np.matmul(B.T,D)
ke=np.matmul(ke1,B)
wsp1=(E*h)/(4*A*(1-v*v))
wsp2=(E*h)/(8*A*(1+v))
c1n=wsp1*np.array([y32**2,-v*y32*x32,-y32*y31])
c1s=wsp2*np.array([x32**2,-x32*y32,-x32*x31])
wyn=c1s +c1n
p=2