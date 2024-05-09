import numpy as np
import matplotlib.pyplot as plt


size_x = 100
size_y = 100

h = 0.2
dt = 0.001
c = 100

U = np.zeros((size_x,size_y))
U_minus_eins = np.zeros((size_x,size_y))
#U_minus_eins.fill(1)

U_buf = np.zeros((size_x,size_y))



plt.ion()

U[:][0] = 100

for step in range(1000000):
    for i in range(1,size_x-1):
        for j in range(1,size_y-1):
            diff_x=(U[i-1][j] - 2*U[i][j] + U[i+1][j])
            diff_y=(U[i][j-1] - 2*U[i][j] + U[i][j+1])
         
            U_buf[i][j] = (diff_x+diff_y) * c**2 * dt**2 + 2*U[i][j] - U_minus_eins[i][j]
            
    U_minus_eins = np.array(U, copy=True)        
    U = np.array(U_buf, copy=True) 
    
        
    
  
    print(step)
    plt.imshow(U,cmap="hot")
    plt.show()
    plt.pause(0.001)
    plt.clf()      
    
    
