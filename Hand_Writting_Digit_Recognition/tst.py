from scipy.misc import imread, imresize, bytescale
from scipy import misc
img=imread("four123.jpg")
print("shape = ", img.shape)
img=imresize(img,(8,8))
print("shape = ", img.shape)
print("image is",img)


img=img.astype(float)
img=bytescale(img,high=16.0,low=0)

# print("Img.Shape:",image.shape)
# print("\n",img)
# print("j")

# x_testData=[]
# for c in img:
#     for r in c:
#         x_testData.append(sum(r)/3.0)
# print("x_test",x_testData)
# print("x_test Data:\n",len(x_testData))
# x_testData=[x_testData]
# print(len(x_testData))