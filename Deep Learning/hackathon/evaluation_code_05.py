import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import tensorflow as tf
from keras.models import  Sequential
#%matplotlib inline
import pickle
from keras.models import load_model

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

Categories=['bike','car','none','person']
filename='finalized_model.sav'
# loaded_model=pickle.load(open(filename,'rb'))
# print("model loaded sucessfully from file by pickle")
# print(".....\n.......\n.......")

loaded_model=load_model("saved_model.hs")

#prediction of img for give path in Test_Data_Dir
Scoring_set="C:/Users/RAHUL TIWARI/Desktop/iitk/Object classification/private_scoring"
    #input("please enter the file directory where Image is Located:")
prediction_list=[]

def prepare_prediction_data(filepath):
    for img in os.listdir(filepath):
        img_array=cv2.imread(os.path.join(filepath, img),cv2.IMREAD_GRAYSCALE)
        resize_image=cv2.resize(img_array,(200,200))
        prediction_list.append([resize_image])
    new_array=np.array(prediction_list)
    return new_array.reshape(len(prediction_list),1,200,200)
prediction=loaded_model.predict([prepare_prediction_data(Scoring_set)])
print(prediction)
image_index=[]
for img_array in prediction:
    for img_label_index in range(len(img_array)):
        if(img_array[img_label_index]==1):
            image_index.append(img_label_index)
            #print(img_label_index)


#Graph ploting image vs prediction
image_for_plot=[]   #image list for ploting
image_name=[]    #for storing the index of the category(predicted)
print("Real Image vs Prediction")
print("-----------------------------------")
print("-----------------------------------")
def prepare_plot_data(filepath):
    for img,label in zip(os.listdir(filepath),image_index):
        image_name.append(os.path.split(img)[-1])
        img_array=cv2.imread(os.path.join(filepath, img))
        # plt.imshow(img_array)
        # plt.xticks([])
        # plt.yticks([])
        # plt.xlabel(Categories[label])
        # plt.show()
    return None
prepare_plot_data(Scoring_set)

# writing a csv file
import csv

myData = ["Image_Name", "Image_Label"]
s = ","
myFile = open('Prediction.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerow(myData)
    for im_name, im_label in zip(image_name, image_index):
        line = [im_name, Categories[im_label]]
        writer.writerow(line)
print("Writing complete")
myFile.close()

#Graph ploting betwwen epach vs accuracy and eppoch vs loss
#sumarize the history for accuracy
plt.plot(loaded_model.history['acc'])
plt.title('model accuracy vs epoch')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.show()
# summarize history for loss
plt.plot(loaded_model.history['loss'])
plt.title('model loss vs epoch')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.show()