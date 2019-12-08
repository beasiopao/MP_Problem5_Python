from matplotlib import pyplot as plt
import numpy as np

n = np.linspace(0,199,200)  

#User-input x(n)
function_xn = input('Enter a function x(n): ') #NOTE: Test input is np.sin(((3*n*np.pi)/100))
def x(n):
    fxn_x = eval(function_xn)  
    return fxn_x 

#piecewise function y(n)
for a in range(200):
    if a==0:
        y = ((-1.5)*x(n)) + (2*x(n+1)) - (0.5*x(n+2))
    elif a>0 and a<=199:
        y = (0.5*x(n+1)) - (0.5*x(n-1))
    else:
        y = (1.5*x(n)) - (2*x(n-1)) + (0.5*x(n-2))

#Graph of x(n) and y(n)
plt.plot(x(n),'-', c = 'tab:purple', label = 'x(n)')
plt.plot(y, '-',  c = 'tab:pink', label = 'y(n)')
plt.legend()
plt.title('Graphs of x(n) and y(n)')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()
plt.show()