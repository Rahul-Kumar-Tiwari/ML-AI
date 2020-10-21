import pandas as pd
from sklearn import linear_model
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import classification_report

import warnings
warnings.filterwarnings(action="ignore")

def get_data(filename):
    #hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
    dataframe = pd.read_csv(filename)
    a = np.array(dataframe)

    x = a[:,0:4:]
    y = a[:,4]


    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=4)

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(x_train, y_train)
    y_predicted=model.predict([[4.5,3.0,1.5,0.2],[6.2,2.7 ,4.6,1.8]])
    print(y_predicted)
    model.fit(x_train, y_train)
    predicted = model.predict(x_test)
    report = classification_report(y_test,predicted)
    print(report)




if __name__=="__main__":
    get_data("https://goo.gl/QnHW4g")
