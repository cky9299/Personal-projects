import matplotlib.pyplot as plt
import numpy as np
import random


def PlotDot():
    x = []; y = []
      
    a=random.randint(2,50)

    for i in range(a):
        x.append(random.uniform(-10,10)) #populate x arr whose len is rng with rng
        y.append(random.uniform(-10,10))


    plt.plot(x,y,'rx')
    plt.xlabel('x')
    plt.ylabel('y')
    return x, y

def CalGradient(x, y):
    xLen=len(x) #xlen = ylen since loop same no times
    x=np.array(x)
    x=np.reshape(x,(xLen,1)) #xLen x 1
    y=np.array(y)
    y=np.reshape(y,(xLen,1)) #yLen x 1
    
    X=np.concatenate((np.ones((xLen,1)),x),axis=1) #axis=1 is vertical concat. 0 for horizontal    #W=(X^T*X)^-1*X^T*y; use normal eq to cal weights; similar to minimizing mse cost f; X dimensions are xLen x 2: [[1,],[1,]..] #W=weight, X=design matrix, y=actual value #2 x xlen * xlen x 2 = 2x2 * 2 x xlen = 2xxlen * xlenx1 = 2x1
    XT=X.transpose()
    w=np.linalg.inv(XT@X)@XT@y #[w0,w1]
    return w


def PlotLine():
    a=np.arange(min(x),max(x),.0001)
    plt.plot(a,w[0][0]+w[1][0]*a)
    plt.show()
    if w[0][0]>=0:
        print('The equation is y =',str(w[1][0])+'x +',str(w[0][0]))
    else:
        print('The equation is y =',str(w[1][0])+'x',str(w[0][0]))



x,y=PlotDot()
w=CalGradient(x,y)
PlotLine()


'''
1. gen rng coords
2. use grad des to find best fit eq
3. plot
'''
