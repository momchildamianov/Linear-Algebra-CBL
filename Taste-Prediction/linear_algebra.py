from numpy import array, matmul, dot, zeros, ones, eye, diag, polyfit, transpose, inf, arccos
from numpy.linalg import solve, norm, det, eig, eigh, eigvals, eigvalsh, inv, lstsq, svd, matrix_power,matrix_rank
from numpy.random import randn, rand, randint, seed
from math import pi, sin, cos

#Load all known values in vectors
emo = [2,1,2,2,1,2,1,-1]
momo = [2,2,2,-1,2,2,-1,0]
svetlana = [1,0,-2,-1,1,2,-1,1]
teddie = [-1,2,-2,-1,0,2,1,1]
martina = [0,2,1,1,0,2,1,-1]
#Stack all vectors in a matrix for accesibility since we can easily iterate through the matrix
matrix = [emo,momo,svetlana,teddie,martina]
#Denote unknown values with -3 since it is outside of scope of ratings
iva = [2,-3,-3,2,1,-3,1,-3]
#Create a new vector, "Green vector", of known values
nIva = []
#Keep track of known values
notNull = []
#Keep track of angles for each person compared with Iva
angles = {}

#Locate known values
for i in range(8):
    if iva[i] != -3:
        notNull.append(i)
        nIva.append(iva[i])

#Get a string with the value of the variable name
def var_name(variable):
    for name in globals():
        if eval(name) == variable:
            return name

#Compute the dot product, norm, and finally, angle between two vectors
def computeAngle(v1, v2):
    nv1 = []
    for i in notNull:
        nv1.append(v1[i])
    if norm(nv1) == 0:
        angle = inf
    else:
        angle = arccos(dot(nv1,v2)/(norm(nv1)*norm(v2)))
    angles[var_name(v1)] = angle
    return angle

#Compute all angles between known members and Iva, and then find the minimal value the angle can take
def compare(matrix):
    for v in matrix:
        computeAngle(v,nIva)
    min = 91
    for i in angles.values():
        if min > i:
            min = i
    return min

#Store the minimal angle value
min = compare(matrix=matrix)
#Get the key of the value with lowest angle
key_list = list(angles.keys())
val_list = list(angles.values())
closest = val_list.index(min)

def predict(angles):
    print(matrix[closest])

predict(angles=angles)