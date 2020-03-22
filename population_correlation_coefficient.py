from FileReader import readCSV
import numpy

dataSet = readCSV('data.csv')

def population_corelation_coefficient(dataSet):
    if len(dataSet) == 0:
        return 0
    
    cal_mean = sum(dataSet) / len(dataSet)
    return (numpy.cov(dataSet)/cal_mean)


#dataSet = [1,2,3,4,5,6,7,8,9,10]
print (population_corelation_coefficient(dataSet))
