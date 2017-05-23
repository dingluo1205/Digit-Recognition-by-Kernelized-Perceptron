import math

import data

def dot_kf(u, v):
    """
    The basic dot product kernel returns u*v+1.

    Args:
        u: list of numbers
        v: list of numbers
    

    Returns:
        dot(u,v) + 1
    """
    # TODO

    result = 1
    for i in range(0,len(u)):
            result = u[i]*v[i]+result
    
    return result

def poly_kernel(d):
    """
    The polynomial kernel.

    Args:
        d: a number

    Returns:
        A function that takes two vectors u and v,
        and returns (u*v+1)^d.
    """

    def kf(u, v):
        # TODO: implement the kernel function
        s = dot_kf(u,v)
        # for i in range(0,d):
        #     s = s * s
        s = s ** d
        return s
    return kf

def exp_kernel(s):
    """
    The exponential kernel.

    Args:
        s: a number

    Returns:
        A function that takes two vectors u and v,
        and returns exp(-||u-v||/(2*s^2))
    """
    def kf(u, v):
        # TODO: implement the kernel function
        result = 0
        for i in range(0,len(u)):
            result = u[i]-v[i]+result
        result = abs(result)
        result = -float(result)/(2*s*s)
        result = math.exp(result)
        return result
    return kf

class Perceptron(object):

    def __init__(self, kf,data,label,a):
        """
        Args:
            kf - a kernel function that takes in two vectors and returns
            a single number.
        """
        self.kf = kf
        self.data = data
        self.label = label
        self.weight = a
        
        # TODO: add more fields as needed

    def update(self, point, label):
        """
        Updates the parameters of the perceptron, given a point and a label.

        Args:
            point: a list of numbers
            label: either 1 or -1

        Returns:
            True if there is an update (prediction is wrong),
            False otherwise (prediction is accurate).
        """
        # TODO
        if (self.predict(point)==label):
            return False
        else:
            return True

    def predict(self, point):
        """
        Given a point, predicts the label of that point (1 or -1).
        """
        # TODO
        s = 0
        for i in range(0,len(self.data)):
            s = s + self.weight[i]*self.kf(point,self.data[i])
        if s > 0 :
            return 1
        else:
            return -1


# Feel free to add any helper functions as needed.


if __name__ == '__main__':
    val_data, val_labs = data.load_data('data/validation.csv')
    test_data, test_labs = data.load_data('data/test.csv')
    # TODO: implement code for running the problems
    
    #implement kernel
    def kernel1():
         a = [0]*len(val_data)
         train = Perceptron(dot_kf,val_data,val_labs,a)
         L = [0]*(len(val_data)/100)
         count = 0
         loss = 0
         for t in range(0,1):
             for i in range(0,len(val_data)):
                 if train.update(val_data[i],val_labs[i]):
                     train.weight[i] = train.weight[i] + val_labs[i]
                     loss = loss + 1
                 if ((i+1)%100 ==0):
                     L[count] = float(loss)/(i+1)
                     count = count + 1
         print L
    

   
    
    #implement polynomial kernel
    def polykernel():
        a = [0]*len(val_data)
        count = 0
        loss = 0
        d = [1,3,5,7,10,15,20]
        L = [0]*len(d)
        for j in range(0,len(d)):
            train = Perceptron(poly_kernel(d[j]),val_data,val_labs,a)
            for i in range(0,len(val_data)):
                if train.update(val_data[i],val_labs[i]):
                    train.weight[i] = train.weight[i] + val_labs[i]
                    loss = loss + 1
            L[count] = float(loss)/1000
            count = count + 1
            loss = 0
        print L


    
    #implement Exponential kernel
    def expkernel(d):
        a = [0]*len(val_data)
        L = [0]*(len(val_data)/100)
        count = 0
        loss = 0
        train = Perceptron(exp_kernel(d),val_data,val_labs,a)
        for t in range(0,1):
            for i in range(0,len(val_data)):
                if train.update(val_data[i],val_labs[i]):
                    train.weight[i] = train.weight[i] + val_labs[i]
                    loss = loss + 1
                if ((i+1)%100 ==0):
                    L[count] = float(loss)/(i+1)
                    count = count + 1
        print L
    

    #run the test on three different kinds of kernels
    kernel1()
    polykernel()
    expkernel(5)
    expkernel(10)




