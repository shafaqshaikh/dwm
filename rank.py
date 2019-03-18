import numpy as np

n= int(input("Enter the Number: "))
d= 0.85
eps=1.0e-8


print("\n Please enter the adjacency matrix for the network")
print("\nType 1 if there is a link from a page i to j else type 0")
links=[]

for i in range (0,n):
    L=[]
    for j in range (0,n):
        L.append(int(input('page' + str(i+1)+'to page' + str(j+1)+': ')))
    links.append(L)

outboundL=np.zeros((n,),dtype=int)

for i in range (0,n):
    
    for j in range (0,n):
        if links[i][j]==1:
            outboundL[i] = outboundL[i] +1
            
            
M= np.zeros((n,n))
for io in range (0,n):
    
    for j in range (0,n):
        if links[i][j]==1:
            M[i][j] = 1/outboundL[j]


M=np.matrix(M)
oneColMat=np.matrix(np.ones((n,1),dtype=int))

R = np.matrix(np.full ((n,1),1/n))

while True:
    Rnext = d*np.dot(M,R)+ ((1-d)/n)*oneColMat
    diff = np.subtract(Rnext, R)
    if np.linalg.norm(diff)<eps:
        break
    R = Rnext
    
    