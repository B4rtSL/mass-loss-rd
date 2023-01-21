import numpy as np
import scipy 

g=9.81

def velocity(mass, rho, area, cz):
    velocity = 2*mass*g/rho/area/cz
    return print(velocity)

def cx(cz, cx0, lambda_e):
    cx=[]
    for i in cz:
        cxs=cx0+i*i/3.14/lambda_e
        cx.append(cxs)



#velocity(10, 1.22, 10, 1.5)