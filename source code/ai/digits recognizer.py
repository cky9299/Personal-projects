import numpy as np
import gzip
from random import randint
import matplotlib.pyplot as plt

def sigmoid(_z):
    a=1/(1+np.exp(-_z))
    return a

with open("custom train img10", 'rb') as f: #using decompressed training img set
    image_data = f.read()
totalPixels=len(image_data) #=47040000
noImg=int(totalPixels/784) #=60000.0 conv to int
x = np.frombuffer(image_data, dtype=np.uint8).reshape((noImg,784))

X=np.insert(x,[0][0],1,1)

with gzip.open('trainlabels.gz', 'r') as f:
    magic_number = int.from_bytes(f.read(4), 'big')
    label_count = int.from_bytes(f.read(4), 'big') #60 000
    labels=f.read()
labelsLen=len(labels)
labels=np.frombuffer(labels, dtype=np.uint8) #1d np arr


wog=[]
for i in range(7850): #bias included else 7840 for 10 hidden neurons
    wog.append(float(randint(-10,10)))
#randomly init all weights. output is arr weights
wog=np.array(wog)
wog=np.reshape(wog,(785,10))
activationThreshold=0.5

for i in range(10):
    w=wog[:,i:i+1] #785x1 ie weights for one neuron

    z=X@w
    a=sigmoid(z)#mx1
    for rowBuster in range(noImg):    
        if a[rowBuster]==0:
            a[rowBuster]=1e-323
        elif a[rowBuster]==1:
            a[rowBuster]=0.9999999999999999
        
    #E=(y.lg a + (1-y).lg(1-a)) *-1/m
    y=[]


    for labelCounter in range(labelsLen):
        if labels[labelCounter]==i:
            y.append(1) #append 1 if isThisDigit.
        else:
            y.append(0) #appebd 0 if not thisdigit.
    y=np.array(y)
    y=np.reshape(y,(60000,1)) #why not 60kx10? coz we doing neuron by neuron so use this atm

    EyIndex=[]; Ey=[] #Ey has initial cost f and after iter
    ##E=(y^T*lg a + (1-y)^T*lg(1-a)) *-1/m
    E=((y.T)@(np.log10(a)) + ((1-y).T)@(np.log10(1-a))) *-1/noImg
    #EL=list(E)
    #print(list(E)[0][0])

    Ey.append(list(E)[0][0])

    α=1
    Ecomp=99999

    for noIter in range(100):    
        w -= α/noImg *( (X.T) @ (a-y)) #returns (n+1) x 1. 2d arr
        z=X@w
        a=sigmoid(z)#mx1
        for rowBuster in range(noImg):    
            if a[rowBuster]==0:
                a[rowBuster]=1e-323
            elif a[rowBuster]==1:
                a[rowBuster]=0.9999999999999999
        E = (y.T@np.log10(a) + (1-y).T@np.log10(1-a)) *-1/noImg #noIter=1 to 10000
        if E > Ecomp:
            w=wcomp
            continue
        Ecomp=E
        wcomp=w        
        Ey.append(list(E)[0][0])
        

   
    
    EyLen=len(Ey)
    for l in range(EyLen): #when noIter==0, Ey==og cost f
        EyIndex.append(l)
    #print(EyIndex)
    #ID=randint(1,999999)
    plot0=plt.figure(i)
    plt.title('cost func vs noIter for neuron '+str(i)+', α='+str(α))
    plt.plot(EyIndex,Ey,'rx')
    plt.xlabel('no iter')
    plt.ylabel('cost func')
    plot0.show()

    thisNeuronError = 0
    
    for aiter in range(60000):
        if a[aiter][0] >= activationThreshold and y[aiter][0] == 0:
            thisNeuronError+=1
                
        elif a[aiter][0] < activationThreshold and y[aiter][0] == 1:
            thisNeuronError+=1


    #print('AT:',activationThreshold,'trainSetError of neuron',i,'=',thisNeuronError/noImg)
    print('trainSetError of digit',i,'=',thisNeuronError/noImg)
    #activationThreshold+=0.1

#test neurons
#override everything except w to save mem coz no need use alr
with open("custom test img10", 'rb') as f: #X,a,y diff. w same coz trained  
    image_data = f.read()
totalPixels=len(image_data) #=47040000
noImg=int(totalPixels/784) #=10000.0 conv to int
x = np.frombuffer(image_data, dtype=np.uint8).reshape((noImg,784))#x = np.frombuffer(image_data, dtype=np.uint8)

X=np.insert(x,[0][0],1,1)

with gzip.open('klabels.gz', 'r') as f: #labels denote numbers
    magic_number = int.from_bytes(f.read(4), 'big')
    label_count = int.from_bytes(f.read(4), 'big') #10 000
    labels=f.read()
labelsLen=len(labels)
labels=np.frombuffer(labels, dtype=np.uint8) #1d np arr

for i in range(10):
    z=X@w
    a=sigmoid(z)#mx1
    for rowBuster in range(noImg):    
        if a[rowBuster]==0:
            a[rowBuster]=1e-323
        elif a[rowBuster]==1:
            a[rowBuster]=0.9999999999999999
        
    y=[]

    for labelCounter in range(labelsLen):
        if labels[labelCounter]==i:
            y.append(1)
        else:
            y.append(0)
    y=np.array(y)
    y=np.reshape(y,(10000,1)) #why not 60kx10? coz we doing neuron by neuron so use this atm

    thisNeuronError = 0
    
    for aiter in range(10000):
        if a[aiter][0] >= activationThreshold and y[aiter][0] == 0:
            thisNeuronError+=1
                
        elif a[aiter][0] < activationThreshold and y[aiter][0] == 1:
            thisNeuronError+=1

    print('testSetError of digit',i,'=',thisNeuronError/noImg)






