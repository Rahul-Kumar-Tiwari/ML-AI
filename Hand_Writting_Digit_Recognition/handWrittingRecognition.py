import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings(action="ignore")


from sklearn import datasets, svm
digits=datasets.load_digits()
print("Digits: ",digits.keys())
print("digits.target-----:",digits.target)

images_and_labels=list(zip(digits.images,digits.target))
print("len(images_and_labels):",len(images_and_labels))


for index,[image,label] in enumerate(images_and_labels[:5]):
    print("index: ",index,"image:\n",image,"label \n",label)
    plt.subplot(2, 5, index + 1)
    plt.axis('on')
    plt.imshow(image,cmap=plt.cm.gray_r,interpolation='nearest')
    plt.title("Training: %i"%label)
#plt.show()


n_samples=len(digits.images)
print('N_samples',n_samples)

imageData=digits.images.reshape((n_samples,-1))
print("After Reshaped: len(imageData[0]) : ",len(imageData[0]))


#create a cllassifier : a support vector classifier
classifier=svm.SVC(gamma=0.001)

#we learn the digits on the first half of the digits
classifier.fit(imageData[:n_samples//2],digits.target[:n_samples//2])

#Now predict the value of the digit on the second half:
expected=digits.target[n_samples//2:]

predicted=classifier.predict(imageData[n_samples//2:])

images_and_predictions=list(zip(digits.images[n_samples//2:],predicted))

for index,[image,prediction] in enumerate(images_and_predictions[:5]):
    plt.subplot(2,5, index+6)
    plt.axis('on')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title("Training: %i" %prediction)
print("Original Values: ",digits.target[n_samples//2:(n_samples//2)+5])
plt.show()

from scipy.misc import imread, imresize, bytescale
from scipy import misc
img=imread("Three2.jpeg")
img=imresize(img,(8,8))
print("image is",img)

classifier=svm.SVC(gamma=0.001)
classifier.fit(imageData[:],digits.target[:])
img=img.astype(digits.images.dtype)
img=bytescale(img,high=16.0,low=0)

print("Img.Shape:",image.shape)
print("\n",img)
print("j")

x_testData=[]
for c in img:
    for r in c:
        x_testData.append(sum(r)/3.0)
print("x_test",x_testData)
print("x_test Data:\n",len(x_testData))
x_testData=[x_testData]
print(len(x_testData))
print("machine output ",classifier.predict(x_testData))
plt.show()