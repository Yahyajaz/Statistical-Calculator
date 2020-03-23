from FileReader import readCSV

confidence = 0.95

dataSet = readCSV('test.csv')

def confidenceInterval(dataSet):
    n = len(dataSet)
    m = sum(dataSet) / n
    std = math.sqrt(sum([(val - m)**2 for val in dataSet])/(len(dataSet) - 1))
    std_err = std / math.sqrt(n)
    t = m / std_err
    h = std_err * t * float(1 + confidence) / float(2., n - 1)

    start = m + h
    end = m - h
    
    return start, end

    print ("Confidence Interval is:", start, end)
