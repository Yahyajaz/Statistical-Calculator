from FileReader import readCSV
from scipy.stats import sem, t
from scipy import mean
confidence = 0.95

dataSet = readCSV('data.csv')

def confidenceInterval(dataSet):
        n = len(dataSet)
        m = sum(dataSet)/len(dataSet)
        std_err = sem(dataSet)
        h = std_err * t.ppf((1 + confidence) / 2, n - 1)

        start = m + h
        end = m - h
        return ([start, end])

#dataSet = [1,2,3,4,5,6,7,8,9,10]
print (confidenceInterval(dataSet))
