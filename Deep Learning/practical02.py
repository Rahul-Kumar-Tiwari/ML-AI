# import numpy as np
# from keras.models import Sequential
#
# import matplotlib.pyplot as plt
#
# from keras.layers import Dense, Dropout,Activation,Flatten
# from keras.layers import Convolution2D,MaxPooling2D
# from keras.utils import np_utils
from keras.datasets import fashion_mnist
#
(x_train,y_train),(x_test,y_test)=fashion_mnist.load_data()
# print(y_train[45])
# print(type(x_train))
# print(x_train.shape)
# print(x_test.shape)
# # x_train=x_train[:10000]
# # y_train=y_train[:10000]
#
x_test=x_test[:5000]
# # y_test=y_test[:5000]
#
# import collections
# count=collections.Counter(y_train)
# print(count)
#
# class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
#                'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
#
# plt.figure(figsize=(15,15))
# for i in range(50):
#     plt.subplot(5,10,i+1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.grid(False)
#     plt.imshow(x_train[i],cmap=plt.get_cmap('nipy_spectral'))
#     plt.xlabel(class_names[y_train[i]])
# plt.show()
#
# x_train=x_train.reshape(x_train.shape[0],1,28,28)
x_test=x_test.reshape(x_test.shape[0],1,28,28)
# print(x_train[0,0,14,14])
# x_train=x_train.astype('float32')
x_test=x_test.astype('float32')
#
#
# x_train = x_train/255
x_test = x_test/255
#
# y_train=np_utils.to_categorical(y_train,10)
# y_test=np_utils.to_categorical(y_test,10)
#
#
# model=Sequential()
#
# model.add(Convolution2D(32,(3,3),activation='relu',input_shape=(1,28,28),data_format='channels_first'))
#
# model.add(MaxPooling2D(pool_size=(2,2)))
#
# model.add(Flatten())
#
# model.add(Dense(128,activation='relu'))
#
# model.add(Dropout(0.4))
# model.add(Dense(10,activation='softmax'))
# #help(model.compile)
# model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
#
# model.fit(x_train,y_train,batch_size=32,epochs=2,verbose=1)
# prediction=model.predict(np.array([x_train[5],]))
# print(prediction)
#
# score=model.evaluate(x_test,y_test,verbose=1)
# print(score)
# summery=model.summary()
# print(summery)

# model.save("practical2.hs")
from keras.models import load_model
loaded_model=load_model("practical2.hs")
prediction=loaded_model.predict([x_test])
print(prediction)

for img_array in prediction:
    for img_label_index in range(len(img_array)):
        print(img_label_index)
        # if(img_array[img_label_index]==1):
        #     print(img_label_index)
        #     #print(img_label_index)
    break




