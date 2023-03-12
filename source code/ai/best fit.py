import matplotlib.pyplot as plt
import numpy as np
import random


def PlotDot():
    x = [] #one feature. all elements r training sets,m
    y = [] #actual value. h-y errror
      
    a=random.randint(2,50)

    for i in range(a):
        x.append(random.uniform(-10,10)) #populate x arr with rng
        y.append(random.uniform(-10,10))


    plt.plot(x,y,'rx')
    plt.xlabel('independent var, x')
    plt.ylabel('y_actual')
    return x,y

def CalGradient():
    #x=[x1,x2,...]
    global x
    global y
    xLen=len(x)
    yLen=len(y)
    x=np.array(x)
    x=np.reshape(x,(xLen,1))
    y=np.array(y)
    y=np.reshape(y,(yLen,1))
    
    X=np.concatenate((np.ones((xLen,1)),x),axis=1) #axis=1 is vertical concat. 0 for horizontal
    #W=(X^T*X)^-1*X^T*y
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
w=CalGradient()
PlotLine()


'''
1. gen rng coords
2. use grad des to find best fit eq
3. plot
'''
