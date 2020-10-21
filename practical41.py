import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def get_data(file_name):
    dataframe=pd.read_csv(file_name)
    print(dataframe)
    x_parameters=np.array(dataframe['square_feet'])
    y_parameters=np.array(dataframe['price'])

    return [x_parameters,y_parameters]
def estimate_coef(x,y,quest_value):
    n=np.size(x)

    m_x=np.mean(x)
    m_y=np.mean(y)


    #cslculating cross-deviation and deviation
    ss_xy=np.sum(x*y)-n*m_x*m_y
    ss_xx = np.sum(x * x) - n * m_x * m_x

    #calculating regression coefficent
    m=ss_xy/ss_xx
    c=m_y-m*m_x
    predicted_cost=m*quest_value+c
    print("Predicted price : ",predicted_cost)

    return [m,c,predicted_cost]
def plot_regression_line(x,y,b,quest_value):
    #ploting the actual points as scatter plot
    plt.scatter(x,y,color='m',marker='o',s=30)

    #predicted response vector
    y_pred=b[0]+b[1]*x
    print(y_pred)

    plt.scatter(x,y_pred,color='g')
    plt.plot(x,y_pred,color='b')

    plt.scatter(quest_value,b[2],color='c',s=30)
    plt.xlabel('Area in square feet')
    plt.ylabel('price in Rupees')

    plt.show()

def main():
    x, y = get_data('ML Data/LR_House_price.csv')
    question_value = 700
    m,c,predicted_cost=estimate_coef(x,y,question_value)
    print("Estimated coefficent:\n")
    print("slope m=",m)
    print("y-intercept c=",c)

    plot_regression_line(x,y,[c,m,predicted_cost],question_value)

if __name__=="__main__":
    main()