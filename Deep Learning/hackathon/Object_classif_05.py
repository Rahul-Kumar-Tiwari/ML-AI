import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import tensorflow as tf
from keras.models import Sequential
#%matplotlib inline
import pickle

from keras.layers import Dense, Dropout,Activation,Flatten
from keras.layers import Convolution2D,MaxPooling2D
from keras.utils import np_utils

print("Group No:- 05")
print("Group members:-\n\tRahul Kumar-262191\n\tNihal Gaurav-262261\n\tBishop Bishal-266604\n\tKaushlendra Pandey-232044")
print("---------------------------")
print("Requrements:-")
print("-------------")
print("Please provide the Directory(path) DataDir and Test_Data_Dir path for Training and Testing Data")
print("-----------------------------")
print("OutPut:-")
print("--------")
print("For see the Output Prediction.csv file or see the Real Image vs Prediction Graph")
print(".............................")
print(".............................")

DataDir="C:/Users/RAHUL TIWARI/Desktop/iitk/Object classification/train"
Categories=['bike','car','none','person']

training_data=[]
def prepare_training_data():   #Read image from given path and append in list
    for category in Categories:
        path = os.path.join(DataDir, category)
        class_num=Categories.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img),cv2.IMREAD_GRAYSCALE)
                new_array=cv2.resize(img_array,(450,400))
                training_data.append([new_array,class_num])
            except Exception as e:
                print("The Exception happen in reading the image:= ",e)
prepare_training_data()
print(len(training_data))

import random
random.shuffle(training_data)

x=[]    #for storing the image data and corrosponding image
y=[]

for features,label in training_data:     #Storing the image and labels in x and y
    x.append([features])
    y.append(label)
x=np.array(x).reshape(len(x),1,450,400)

 #load data in pickle
x=x/255.0
y=np_utils.to_categorical(y,4)

model=Sequential()  #model adding

model.add(Convolution2D(32,(3,3),activation='relu',input_shape=(1,450,400),data_format='channels_first'))
#convolution

model.add(MaxPooling2D(pool_size=(2,2)))
#for max pooling

model.add(Flatten())
#for Dimension Reducing

model.add(Dense(128,activation='relu'))
#activation function and first nodes are added

model.add(Dropout(0.4))
#droupout(node breaking)
model.add(Dense(64,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(16,activation='relu'))
model.add(Dense(4,activation='softmax'))
#help(model.compile)
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

model.fit(x,y,batch_size=4,epochs=5,verbose=1)

model.save("saved_model.hs")

#summary of the model
summery=model.summary()
print(summery)

#after training model store in pickle
# filename='finalized_model.sav'
# pickle.dump(model_fit,open(filename,'wb'))
#
# print('MODEL DUMPED SUCESSFULLY INTO A FILE BY PICKLE......\n........\n.......\n.....')