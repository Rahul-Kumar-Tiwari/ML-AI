import pandas as pd
import matplotlib.pyplot as plt

from sklearn import linear_model

import warnings
warnings.filterwarnings(action="ignore")

def get_data(file_name):
    dataframe=pd.read_csv(file_name)
    print(dataframe)
    x_parameters=[]
    y_parameters=[]
    for single_square_feet,single_price_value in zip(dataframe['square_feet'],dataframe['price']):
        x_parameters.append([float(single_square_feet)])
        y_parameters.append(float(single_price_value))
    return x_parameters,y_parameters
def linear_model_main(x_parameters,y_parameters,quest_value):
    regr=linear_model.LinearRegression()
    print("Area: ",x_parameters)
    print("price: ",y_parameters)
    regr.fit(x_parameters,y_parameters)
    predicted_ans=regr.predict([[quest_value]])
    predications={}
    predications['coefficient']=regr.coef_
    predications['intercept']=regr.intercept_
    predications['predicted_ans']=predicted_ans
    print("output from machine =",predicted_ans)

    plt.scatter(x_parameters,y_parameters,color='m',marker='o',s=30)
    all_predicted_Y=regr.predict(x_parameters)
    plt.scatter(x_parameters,all_predicted_Y,color='b')
    plt.plot(x_parameters,all_predicted_Y,color='r')
    plt.scatter(quest_value,predicted_ans,color='g')
    plt.xlabel('Area in square feet')
    plt.ylabel('price in Rupees')
    plt.show()
    return predications

if __name__=="__main__":
    x,y=get_data('ML Data/LR_House_price.csv')
    question_value=700
    result=linear_model_main(x,y,question_value)
    print("Intercept value ",result['intercept'])
    print("Coefficent ",result['coefficient'])
    print("Predicted House Price value:",result['predicted_ans'])