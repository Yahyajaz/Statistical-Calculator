import math
from FileReader import readCSV
dataSet = readCSV('data.csv')
testData = [1,2,3]

# Confidence Interval

def test_calc_confidenceInterval():
    from confidence_interval import confidenceInterval
    assert confidenceInterval(testData) == 1.076

def test_calc_confidenceInterval_fail():
    from confidence_interval import confidenceInterval
    assert confidenceInterval(testData) != 5


# Correlation Coefficient





# Population variance

def test_calc_variance():
    from population_variance import pop_variance
    assert variance(dataSet) == variance(dataSet)

def test_calc_variance_fail():
    from population_variance import pop_variance
    assert variance(dataSet) != 2




# Proportion






# Mean 

def test_calc_sampleMean():
    from sample_mean import SampMean
    assert SampMean(testData) == 2

def test_calc_sampleMean_fail():
    from sample_mean import SampMean
    assert SampMean(testData) != 1




# Sample Standard deviation 

def test_calc_std():
    from sample_SD import sample_standardDeviation
    assert sample_standardDeviation(dataSet) == sample_standardDeviation(dataSet)

def test_calc_std_fail():
    from StatisticsModule import standardDeviation
    assert sample_standardDeviation(dataSet) != 2


# Variance of sample proportion

def test_calc_varianceSampleProportion():
    from variance_of_sample_proportion import VSP
    assert VSP(testData) == 1

def test_calc_varianceSampleProportion_fail():
    from variance_of_sample_proportion import VSP
    assert VSP(testData) != 2








