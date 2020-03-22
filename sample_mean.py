from FileReader import readCSV
import math

dataSet = readCSV('test.csv', nrows = 10)


def sampleMean(dataSet):
        if len(dataSet) == 0:
                return 0
        smean = sum(dataSet) / len(dataSet)

        return smean

#dataSet = [1,2,3,4,5,6,7,8,9,10]
print(sampleMean(dataSet))
