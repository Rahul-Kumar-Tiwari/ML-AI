import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

DataDir="C:/Users/RAHUL TIWARI/Desktop/iitk/train"
Categories=['Black-grass','Charlock','Cleavers','Common Chickweed','Common wheat','Fat Hen',
            'Loose Silky-bent','Maize','Scentless Mayweed','Shepherds Purse',
            'Small-flowered Cranesbill','Sugar beet']
for category in Categories:
    path=os.path.join(DataDir,category)
    for img in os.listdir(path):
        img_array=cv2.imread(os.path.join(path,img))
        plt.imshow(img_array)
        plt.show()
        break
    break

training_data=[]
def create_training_data():
    for category in Categories:
        path = os.path.join(DataDir, category)
        class_num=Categories.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img))
                new_array=cv2.resize(img_array,(100,100))
                training_data.append([new_array,class_num])
            except Exception as e:
                pass
create_training_data()
print(len(training_data))

import random
random.shuffle(training_data)
for sample in training_data[:10]:
    print(sample[1])


