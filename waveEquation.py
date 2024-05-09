import numpy as np
import matplotlib.pyplot as plt


size_x = 100
size_y = 100

h = 0.2
dt = 0.001
alpha = 2

D = np.zeros((size_x,size_y))

D_buf = np.zeros((size_x,size_y))



plt.ion()



for step in range(1000000):
    for i in range(1,size_x-1):
        for j in range(1,size_y-1):
            diff_x=(T[i-1][j] - 2*T[i][j] + T[i+1][j])
            diff_y=(T[i][j-1] - 2*T[i][j] + T[i][j+1])
         
            T_buf[i][j] = T[i][j] + alpha * dt*1/(h**2) * (diff_x+diff_y)
            
    T = np.array(T_buf, copy=True) 
    
    #T[:][0]=T[:][1]*0.9
    
    
    
    for i in range(45):
        T[i][50] = 0
        T[i+55][50] = 0
        
    
    print(np.sum(T))
    #print(step)
    plt.imshow(T,cmap="hot")
    #plt.plot(T[1][:])
    plt.show()
    plt.pause(0.001)
    plt.clf()      
    