import pandas as pd
from sklearn import linear_model

def get_data(filename):
    data=pd.read_csv(filename)
    flash_x_parameter=[]
    flash_y_parameter=[]
    got_x_parameter=[]
    got_y_parameter=[]
    for x1,y1,x2,y2 in zip(data['Flash_episode_number'],
                           data['Flash_us_viewers'],data['GoT_episode_number'],data['GoT_us_viewers']):
        flash_x_parameter.append([float(x1)])
        flash_y_parameter.append(float(y1))
        got_x_parameter.append([float(x2)])
        got_y_parameter.append(float(y2))
    return flash_x_parameter,flash_y_parameter,got_x_parameter,got_y_parameter
def find_more_viewers(x1,y1,x2,y2):
    regr1=linear_model.LinearRegression()
    regr1.fit(x1,y1)
    predicted_value1=regr1.predict([[10]])
    print("Prediction of Flash : ",predicted_value1)
    regr2 = linear_model.LinearRegression()
    regr2.fit(x2, y2)
    predicted_value2 = regr2.predict([[10]])
    print("Prediction of GoT : ", predicted_value2)
    if(predicted_value1>predicted_value2):
        print("Next episode of Flash Tv Show will have more viewers for next week ")
    else:
        print("Next episode of Game of Thrones Tv Show will have more viewers for next week")

if __name__=="__main__":
    x1,y1,x2,y2=get_data("ML Data/LR_Episodes.csv")
    find_more_viewers(x1,y1,x2,y2)