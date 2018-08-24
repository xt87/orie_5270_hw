from scipy.optimize import minimize
import numpy as np

def Rosenbrock(x):
    """
    This is to calculate the result of the Rosenbrock function of x while n=3
    :param x: an array of the starting point
    :return : the value of the calculated Rosenbrock function
    """
    b=0
    for i in range(2):
        a = 100 * (x[i+1]-x[i]**2)**2 + (1-x[i])**2
        b = b+a
    return b
    
def gradient(x):
    """
    This is to calculate the gradient of the Rosenbrock function of x while n=3
    :param x: an array consisting of the input values
    :return : an array which is the gradient vector of x
    """
    grad = np.array([-400*x[0]*x[1] + 400*x[0]**3 - 2*(1-x[0]),
                  -400*x[1]*x[2] + 400*x[1]**3 - 2*(1-x[1]) + 200*(x[1] - x[0]**2),
                  200*(x[2]-x[1]**2)])
    return grad
    
i = 0
res = [0,0,0,0,0]

if __name__ == "__main__":
    for i in range(5):
        x0 = 10*np.random.rand(1,3)-5
        res[i] = minimize(Rosenbrock,x0,method='BFGS',jac=gradient).fun

    print(min(res))
