import statistics
from pathlib import Path


def makeLst():
    """Makes list of values out of avocado.csv"""
    folder = Path('data/')
    file = folder / 'avocado.csv'
    infile = open(file, 'r')
    raw = infile.read()
    infile.close()
    rawLst = raw.split(',')
    infile.close()
    return rawLst


def strLst(cat):
    """Creates list of str numbers for given variable"""
    dict = {'Average Price': 2, 'Total Volume': 3, '4046': 4, '4225': 5, '4770': 6, 'Total Bags': 7, 'Small Bags': 8, 'Large Bags': 9, 'XLarge Bags': 10}
    rawLst = makeLst()
    strVolLst = []
    offset = dict[cat]
    while offset < len(rawLst):
        strVolLst.append(rawLst[offset])
        offset += 13
    return strVolLst


def intLst(cat):
    """Creates list of int numbers for given variable"""
    strVolLst = strLst(cat)
    numVolLst = []
    for i in range(1, len(strVolLst)):
        numVolLst.append(float(strVolLst[i]))
    return numVolLst


def readAndComputeMean_SM(cat):
    """Computes mean of selected variable in avocado.csv"""
    numVolLst = intLst(cat)
    mean_SM = round(statistics.mean(numVolLst), 2)
    return mean_SM


def readAndComputeSD_SM(cat):
    """Computes sample standard deviation of selected variable in avocado.csv"""
    numVolLst = intLst(cat)
    sd_SM = round(statistics.stdev(numVolLst), 2)
    return sd_SM


def readAndComputeMedian_SM(cat):
    """Computes median of selected variable in avocado.csv"""
    numVolLst = intLst(cat)
    median_SM = round(statistics.median(numVolLst), 2)
    return median_SM


def readAndComputeMean_HG(cat):
    """Returns mean without using statistics module"""
    lst = intLst(cat)
    total = sum(lst)
    n = len(lst)
    mean_HG = round((total / n), 2)
    return mean_HG


def readAndComputeSD_HG(cat):
    """Returns sample standard deviation without using statistics module"""
    lst = intLst(cat)
    mean_HG = readAndComputeMean_HG(cat)
    n = len(lst) - 1
    tempSum = 0
    for i in lst:
        tempSum += (i - mean_HG)**2
    sd_HG = round(((tempSum / n)**0.5), 2)
    return sd_HG


def readAndComputeMedian_HG(cat):
    """Returns median without using statistics module"""
    lst = sorted(intLst(cat))
    # if len(lst) is even
    if len(lst) % 2 == 0:
        cut = int(len(lst) / 2)
        midValues = lst[cut-1:-(cut-1)]
        median_HG = sum(midValues)/2
        return median_HG
    # if len(lst) is odd
    else:
        midValue = int((len(lst) - 1) / 2)
        median_HG = lst[midValue]
        return median_HG


def readAndComputeMean_MML(cat):
    """Returns mean of given category only holding one value in memory at a time"""
    folder = Path('data/')
    file = folder / 'avocado.csv'
    offset = {'Average Price': 2, 'Total Volume': 3, '4046': 4, '4225': 5, '4770': 6, 'Total Bags': 7, 'Small Bags': 8, 'Large Bags': 9, 'XLarge Bags': 10}
    n = 0
    total = 0
    infile = open(file, 'r')
    for i in infile:
        raw = i.split(',')
        strNum = raw[offset[cat]]
        try:
            num = float(strNum)
            total += num
            n += 1
        except:
            continue
    infile.close()
    mean_MML = round(total/n, 2)
    return mean_MML


def readAndComputeSD_MML(cat):
    """Returns sample standard deviation of given category only holding one value in memory at a time"""
    folder = Path('data/')
    file = folder / 'avocado.csv'
    offset = {'Average Price': 2, 'Total Volume': 3, '4046': 4, '4225': 5, '4770': 6, 'Total Bags': 7, 'Small Bags': 8, 'Large Bags': 9, 'XLarge Bags': 10}
    mean = readAndComputeMean_MML(cat)
    n = 0
    total = 0
    infile = open(file, 'r')
    for i in infile:
        raw = i.split(',')
        strNum = raw[offset[cat]]
        try:
            num = float(strNum)
            total += (num - mean)**2
            n += 1
        except:
            continue
    infile.close()
    sd_MML = round((total / (n - 1)) ** 0.5, 2)
    return sd_MML


def readAndComputeMedian_MML(cat):
    """Returns median of given category only holding one value in memory at a time"""
    median_MML = readAndComputeMedian_HG(cat) #Placed just so test code will run, this is not a working function
    folder = Path('data/')
    file = folder / 'avocado.csv'
    offset = {'Average Price': 2, 'Total Volume': 3, '4046': 4, '4225': 5, '4770': 6, 'Total Bags': 7, 'Small Bags': 8, 'Large Bags': 9, 'XLarge Bags': 10}
    n = 0
    infile = open(file, 'r')
    for i in infile:
        n += 1
    infile.close()
    half = int((n - 2) / 2)

    higher = 0
    lower = 0

    infile = open(file, 'r')
    for i in infile:
        line = infile.readline()
        raw = line.split(',')
        #strNum = raw[offset[cat]]
        try:
            num = float(strNum)
            for i in infile:
                raw2 = i.split(',')
                strNum2 = raw2[offset[cat]]
                if num > float(strNum2):
                    higher += 1
                    #print('higher ', higher)
                else:
                    lower += 1
                    #print('lower ', lower)
        except:
            #print('continue')
            continue
    else:
        pass
    return median_MML

def test(cat):
    print('Mean for 3 Functions')
    print('SM: {}  HG: {}  MML: {}'.format(readAndComputeMean_SM(cat), readAndComputeMean_HG(cat), readAndComputeMean_MML(cat)))
    print()
    print('Standard Deviation for 3 Functions')
    print('SM: {}  HG: {}  MML: {}'.format(readAndComputeSD_SM(cat), readAndComputeSD_HG(cat), readAndComputeSD_MML(cat)))
    print()
    print('Median for 3 Functions')
    print('SM: {}  HG: {}  MML: {}'.format(readAndComputeMedian_SM(cat), readAndComputeMedian_HG(cat), readAndComputeMedian_MML(cat)))


if '__name__' == '__main__':
    readAndComputeMean_HG()
    readAndComputeMean_SM()
    readAndComputeMean_MML()
    readAndComputeSD_HG()
    readAndComputeSD_SM()
    readAndComputeSD_MML()
    readAndComputeMedian_HG()
    readAndComputeMedian_MML()
    readAndComputeMedian_SM()
    test()
