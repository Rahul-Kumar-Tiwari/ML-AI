import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x,y):
    n=np.size(x)

    m_x=np.mean(x)
    m_y=np.mean(y)

    #cslculating cross-deviation and deviation
    ss_xy=np.sum(x*y)-n*m_x*m_y
    ss_xx = np.sum(x * x) - n * m_x * m_x

    #calculating regression coefficent
    m=ss_xy/ss_xx
    c=m_y-m*m_x
    a=np.mean(y/x)
    print(a)
    return [m,c]
def plot_regression_line(x,y,b):
    #ploting the actual points as scatter plot
    plt.scatter(x,y,color='m',marker='o',s=30)

    #predicted response vector
    y_pred=b[0]+b[1]*x
    print(y_pred)

    plt.scatter(x,y_pred,color='g')
    plt.plot(x,y_pred,color='b')

    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()

def main():
    x=np.array([1,1,2,3,4,5,6,7,8,9])
    y=np.array([1,3,2,5,7,8,8,9,10,12])

    m,c=estimate_coef(x,y)
    print("Estimated coefficent:\n")
    print("slope m=",m)
    print("y-intercept c=",c)

    plot_regression_line(x,y,[c,m])

if __name__=="__main__":
    main()