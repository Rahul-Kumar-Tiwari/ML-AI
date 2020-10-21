import numpy as np
from operator import itemgetter
import csv,os

class KNNClassifer(object):
    def __init__(self):
        self.training_features=None
        self.training_labels=None
        self.test_features=None

        self.elegantResult="most likely,{0}'{1}' is  of type of '{2}'"
    def loadTrainingDataFromFile(self,file_path):
        if file_path is not None and os.path.exists(file_path):
            tr_features=[]
            self.training_labels=[]
            with open(file_path,'r') as training_data_file:
                reader=csv.DictReader(training_data_file)
                for row in reader:
                    if row['moviename']!='?':
                        tr_features.append([float(row['kicks']),float(row['kisses'])])
                        self.training_labels.append(row['movietype'])
                    else:
                        self.test_features=np.array([float(row['kicks']),float(row['kisses'])])
            if len(tr_features)>0:
                self.training_features=np.array(tr_features)
            print(self.training_features)
            print(self.training_labels)
            print(self.test_features)
    def classifyTestData(self,test_data=None,k=0):
        print("classifyTestData: test_data",test_data)
        if test_data is not None:
            self.test_features=np.array(test_data,dtype=float)
        print("classifyTestData: self.test_features: ",self.test_features)

        if self.test_features is not None and self.training_features is not None\
                and self.training_labels is not None and k>0:
            print(self.test_features)
            print(self.training_features)
            print(self.training_labels)
            featureVectorSize=self.training_features.shape[0]
            print(featureVectorSize)
            tileofTestData=np.tile(self.test_features,(featureVectorSize,1))
            print(tileofTestData)
            diffMat=self.training_features-tileofTestData
            print(diffMat)
            sqDiffMat=diffMat**2
            print(sqDiffMat)
            sqDistances=sqDiffMat.sum(axis=1)
            print(sqDistances)
            distances=sqDistances**0.5
            print(distances)
            sortedDistanceIndices=distances.argsort()
            print(sortedDistanceIndices)
            print(self.training_labels)
            classCount={}
            for i in range(k):
                print("hi",sortedDistanceIndices[i])
                voteILabel=self.training_labels[sortedDistanceIndices[i]]
                print(voteILabel)
                classCount[voteILabel]=classCount.get(voteILabel,0)+1
            print(classCount)
            sortedClassCount=sorted(classCount.items(),key=itemgetter(1),reverse=True)
            print("sortedclassCount",sortedClassCount)
            print(sortedClassCount[0])
            print(sortedClassCount[0][0])
            return sortedClassCount[0][0]
        else:
            return "can't determine result for empty test-data"
def predictmovieType():
    instance=KNNClassifer()
    instance.loadTrainingDataFromFile("ML Data/LgR_Movies_kNN_classifier.csv")
    print("***********************************************")
    my_test_data=[50,50]
    classOfTestData = instance.classifyTestData(test_data=my_test_data, k=5)
    #classOfTestData = instance.classifyTestData(test_data=None, k=5)
    #print(classOfTestData)
    return instance.elegantResult.format('Movie',str(instance.test_features),classOfTestData)
if __name__=="__main__":
    print(predictmovieType())