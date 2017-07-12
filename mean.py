def mean(rawData):
    #rawData is a list of values
    total = 0.0
    for thisEntry in rawData:
        total = total + float(thisEntry)
    meanValue = total / float(len(rawData))
    return meanValue

def expectedValueProb(xi, prob):
    #xi is list of outcomes
    #prob is list of probabilities for the corresponding outcome
    ev = 0.0
    for i in range(len(xi)):
        ev = ev + (xi[i] * prob[i])
    return ev

def varianceProb(xi, mean, prob):
    var = 0.0
    for i in range(len(xi)):
        var = var + ((xi[i] - mean)**2 * prob[i])
    return var

def stdDevProb(xi, mean, prob):
    var = varianceProb(xi, mean, prob)
    return var**0.5

def median(rawData):
    sortedData = rawData
    sortedData.sort()
    medianItem = (float(len(rawData)) + 1.0) / 2.0
    if len(rawData) % 2 != 0:
        #print medianItem
        return sortedData[int(medianItem)]
    else:
        medianMin = sortedData[int(medianItem) - 1] 
        medianMax = sortedData[int(medianItem)]
        medianValue = (float(medianMin) + float(medianMax)) / 2.0
        return medianValue

def mode(rawData):
    sortedData = rawData
    sortedData.sort()
    frequencyDict = {}
    for thisEntry in sortedData:
        frequencyDict[str(thisEntry)] = 0
    for thisEntry in sortedData:
        frequencyDict[str(thisEntry)] = frequencyDict[str(thisEntry)] + 1
    highestEntry = ""
    highestValue = 0
    for thisEntry in frequencyDict.keys():
        if frequencyDict[thisEntry] > highestValue:
            highestValue = frequencyDict[thisEntry]
            highestEntry = thisEntry
    return highestEntry

def midrange(rawData):
    sortedData = rawData
    sortedData.sort()
    midrangeValue = (float(sortedData[0]) + float(sortedData[-1])) / 2.0
    return midrangeValue

def firstQuartile(rawData):
    sortedData = rawData
    sortedData.sort()
    numOfPoints = len(rawData)
    firstQuartileValue = 0.25 * (numOfPoints + 1)
    if len(rawData) % 4 != 0.0:
        #print "div by 4"
    	return sortedData[int(firstQuartileValue)]
    else:
        firstQMin = sortedData[int(firstQuartileValue)-1]
        firstQMax = sortedData[int(firstQuartileValue)]
	#print firstQMin, firstQMax
        firstQValue = (float(firstQMin) + float(firstQMax)) / 2.0
        return firstQValue

def secondQuartile(rawData):
    sortedData = rawData
    sortedData.sort()
    numOfPoints = len(rawData)
    secondQuartileValue = 0.5 * (numOfPoints + 1)
    if len(rawData) % 2 != 0.0:
        #print "div by 2"
        return sortedData[int(secondQuartileValue)]
    else:
        secondQMin = sortedData[int(secondQuartileValue)-1]
        secondQMax = sortedData[int(secondQuartileValue)]
        #print secondQMin, secondQMax
        secondQValue = (float(secondQMin) + float(secondQMax)) / 2.0
        return secondQValue

def thirdQuartile(rawData):
    sortedData = rawData
    sortedData.sort()
    numOfPoints = len(rawData)
    thirdQuartileValue = 0.75 * (numOfPoints + 1)
    #print thirdQuartileValue
    if len(rawData) % 4 == 0.0:
        #print "div by 4"
    	return sortedData[int(thirdQuartileValue)]
    else:
        thirdQMin = sortedData[int(thirdQuartileValue)-1]
	thirdQMax = sortedData[int(thirdQuartileValue)]
	#print thirdQMin, thirdQMax
	thirdQValue = (float(thirdQMin) + float(thirdQMax)) / 2.0
	return thirdQValue

def midhinge(rawData):
    firstQuart = firstQuartile(rawData)
    thirdQuart = thirdQuartile(rawData)
    midhingeValue = (float(thirdQuart) + float(firstQuart)) / 2.0
    return midhingeValue

def variance(rawData):
    sortedData = rawData
    sortedData.sort()
    numOfPoints = len(rawData)
    meanValue = mean(rawData)
    sumOfDeltas = 0.0
    for thisEntry in sortedData:
        thisEntryValue = (thisEntry - meanValue)**2
        sumOfDeltas = sumOfDeltas + thisEntryValue
    varianceValue = sumOfDeltas / numOfPoints
    return varianceValue

def standardDeviation(rawData):
    varianceValue = variance(rawData)
    stdDevValue = varianceValue ** 0.5
    return stdDevValue

def fiveNumber(rawData):
    sortedData = rawData
    sortedData.sort()
    xSmallest = sortedData[0]
    xLargest = sortedData[-1]
    medianVal = median(rawData)
    q1 = firstQuartile(rawData)
    q3 = thirdQuartile(rawData)

    print xSmallest, q1, medianVal, q3, xLargest


    #probablility is stable for all events
    #only one occurence at a time, not simultaneous
    #all events independent

    #x=number of successes
    #lam=expected number of nonconformities per area of opportunity

    #P(X = x| lam) = (e^-lam * lam^x) / x!
    import math
    xBang = math.factorial(x)
    e = math.e #2.72

    finalVal = (e**(-(lam)) * (lam**x)) / xBang

    stdDev = lam**0.5
    print "P(X =", x, ") =", finalVal
    print "mu =", lam
    print "variance =", lam
    print "stdDev =", stdDev
    print ""
    return finalVal

def hypergeometric(rawData):
    return True

def binomial(x, n, p):
    #for a situation with only two possible outcomes: success or failure
    #probability of success is constant: p. Failure: 1 - p.
    #"bernoulli event", mutually exclusive, collectively exhaustive
    #each trial is independent of other trials
    #n = number of events
    #(X = x) random variable X equals a specific number x

    #P(X = x|n,p) = (n!/x!(n-x)! * p^x * (1-p)^(n-x)

    import math
    nBang = math.factorial(n)
    xBang = math.factorial(x)
    nxBang = math.factorial(n-x)

    allSeqs = nBang / (xBang * nxBang)

    xSuccess = (p**x)*(1-p)**(n-x)

    finalVal = allSeqs * xSuccess

    #follows pascal's triangle
    #nearly bell shaped for large n and p=.5
    #skewed right for p< .5
    #skewed left for p> .5
    #mu = np
    #variance = n * p * (1-p)

    print "P(X =", x, ") =", finalVal
    print "mu =", n * p
    print "variance =", n * p * (1 -p)
    print "stdDev =", (n * p * (1-p))**0.5
    print ""
    return finalVal

def normalProbPaper(i, n):
    #The cumulative percentage p(sub)i for the ith observation in an ordered array
    probI = ((i - 0.5) / n) * 100
    return probI

def orderedQuantile(i, n):
    #The Z value on a standard norm dist below which the proportion i/(n+1) 
    #of the area under the curve is contained
    o = i / (n+1)
    print i,"th Ordered Quantile"
    return o

########################
###Getting Continuous###
########################

# probability distributions P(a <= X <= b) = integran(a, b, f(x) dx)
# cumulative P(X <= b) = integral(

def uniform(a, b):
    #a = start value
    #b = end value
    mu = (a + b) / 2
    variance = (b - a)**2 / 12
    stdDev = variance**0.5
    prob = 1 / (b - a)

    print "Mu =", mu
    print "Var =", variance
    print "Std Dev =", stdDev
    print "Prob =", prob
    return prob
    

def normal(x, mu, stdDev):
    import math
    #prob = (1 / (2 * math.pi)**0.5 * stdDev * x) * (math.e**((-0.5(x - mu)/ stdDev)) ** 2)
    #prob = (1.0 / ((2.0 * math.pi)**0.5 * stdDev * x)) * (math.e**((-0.5(x - mu)/ stdDev)) ** 2.0)
    firstPart = 1.0 / ((2.0 * math.pi)**0.5 * stdDev * x)
    secondPart = math.e**((-0.5*(x - mu)/ stdDev**2.0)) 

    firstCalcProb = firstPart * secondPart
    print firstCalcProb

    variance = float(stdDev)**2
    denom = (2*math.pi*variance)**0.5
    num = math.exp(-(float(x) - float(mu))**2/(2*variance))
    calcProb = num/denom
    print calcProb

    import scipy.stats
    prob = scipy.stats.norm(mu, stdDev).pdf(x)
    return prob

def logNormal(x, mu, stdDev):
    import math
    import scipy.stats

    mean = math.e**(mu + ((stdDev**2) / 2))
    sigma = ((math.e**(2*mu + (stdDev)**2) * (math.e**(stdDev**2) - 1)))**0.5
    print "Mu =", mean
    print "StdDev = ", sigma
    prob = scipy.stats.norm(mu, stdDev).pdf(math.log(x))
    zValue = (math.log(x) - mu) / stdDev
    print "Z =", zValue
    return prob

def normalZ(x, mu, stdDev):
    #Returns in "Standard Deviation Units"
    zulu = (x - mu) / stdDev
    return zulu

def normalX(z, mu, stdDev):
    xRay = mu + (z * stdDev)
    return xRay

def binomialZ(x, n, p):
    # also z = x - mu / sigma
    #variance should be at least 10
    zulu = x - n*p / (n*p*(1-p))**0.5
    return zulu

def poissonZ(x, mu, lam):
    # variance should be at least 5
    Z = x - lam / (lam)**0.5
    return Z

def exponential(x, lam):
    ## lambda = rate of change
    import math
    #P(x<=X) =  1 - e^-lam*x
    mu = 1.0 / lam
    print "Mu =", mu
    stdDev = 1.0 / lam
    print "StdDev =", stdDev
    prob = 1 - math.e**(-(lam)*(x))
    print "P(X<=", x, ") = ", prob
    return prob

def weibull(x, alpha, beta):
    #P(X <= x) = 1 - e^-(x/beta)^alpha
    import math
    prob = 1.0 - math.e**(-(x/beta)**alpha)
    print "P(X <=", x, ") =", prob
    return  prob

def sampleDist(sampleSize, mean, stdDev):
    #only if sample is normally distributed
    #sample standard deviation is also standard error
    sampleMean = mean
    sampleStdDev = stdDev / sampleSize**0.5
    print "SampleMean =", sampleMean
    print "Sample StdDev =", sampleStdDev

def upperLowerBoundsOfSample(zValue, mean, stdDev, sampleSize):
    # bounds of sample mean or s
    #percent convert to zValue of 1/2 of percentage
    lowerLimit = mean - zValue * (stdDev / sampleSize**0.5)
    upperLimit = mean + zValue * (stdDev / sampleSize**0.5)
    print "Lower Limit:", lowerLimit
    print "Upper Limit:", upperLimit
    return lowerLimit, upperLimit

def sampleDistOfProportion(sampleSize, failLower, failUpper):
    denom = (failLower * ( 1 - failLower) / sampleSize)**0.5
    numer = failUpper - failLower
    zulu = numer / denom
    return zulu

##Point Estimators##
## unbiasedness - expected value of statistic is equal to population parameter
## efficiency - precision of sample statistic as estimator of pop. parameter
## consistency - effect sample size has on the usefulness of the estimator

##confidience interval estimation of the mean
## 

# if you don't have the whole pop mean, use the sample mean
# xBar +=(Z)(stdDev / sqrt(n))
def sampleMeanInterval(xBar, zValue, stdDev, sampleSize):
    #use if stdDev is known
    lowerLimit = xBar - zValue * (stdDev / sampleSize**0.5)
    upperLimit = xBar + zValue * (stdDev / sampleSize**0.5)

    return lowerLimit, upperLimit

# (1-alpha) * 100%
# xbar - zValue(sigma / sqrt(n)) <= mu <= xBar + zValue(sigma/sqrt(n))
# zValue comes from the confidence interval
# z = value corresponding to an area of (1-alpha)/2 
# from the center of a standard normal dist
# for 95% confidence zValue is 1.96 or probablility of .4750 on 
# either side of the zero

def studentsT(xBar, t_of_DoF, sampleStdDev, sampleSize):
    # mu = population mean, s = sampleStdDev, n = sample size
    # n-1 degrees of freedom
    # as n gets larger t dist gets closer and closer to normal dist
    # symmetrical
    # t table gives you the area of the tails (cross DoF and alpha)
    # alpha = leftover of percentage / 2
    # (1 - alpha) = percentage of confidence, alpha = 100 - PoC

    #used to find range for population mean
    #used when stdDev is not known
    degOfFreedom = sampleSize-1
    numer = xBar - t_of_DoF
    denom = sampleStdDev / sampleSize**0.5
    finalVal = numer / denom
    print "final val:", finalVal

    tLower = xBar - t_of_DoF * (sampleStdDev/sampleSize**0.5)
    tUpper = xBar + t_of_DoF * (sampleStdDev/sampleSize**0.5)


    print "Degrees of Freedom:", degOfFreedom
    print tLower, "<= mu <=", tUpper
    return tLower, tUpper


def chiSquare(sampleSize, sampleStdDev, chiUpper, chiLower):
    #Not symmetric
    #as DoF increases chiSquare becomes more nearly symmetrical
    #P(x(sub 1-alpha/2)^2 < x^2 < x(sub alpha/2)^2) = 1-alpha
    #used to find the population variance or stdDev

    #chiSquare table 95% confidence -> 1-alpha = 0.95 -> alpha = 0.05
    # alpha/2 = 0.025 = chiUpper
    # 1-alpha = .975 = chiLower

    #(n-1) ( s**2 / chiUpper) <= sigma**2 <= n-1 * (s**2 / chiLower)

    ##used to find range for population variance
    lowerVal = (sampleSize-1) * (sampleStdDev**2 / chiUpper)
    upperVal = (sampleSize-1) * (sampleStdDev**2 / chiLower)

    print lowerVal, "<= variance <=", upperVal
    print lowerVal**0.5, "<= sigma <=", upperVal**0.5
    return lowerVal, upperVal

#######################################
##prediction interval estimate for a future individual value
#######################################

#xbar +- t_of_DoF * s * sqrt(1 + 1/n)
def predictFutureValue(xBar, t_of_DoF, sampleStdDev, sampleSize):
     lowerVal = xBar - (t_of_DoF * sampleStdDev * (1 + 1/sampleSize)**0.5)
     upperVal = xBar + (t_of_DoF * sampleStdDev * (1 + 1/sampleSize)**0.5)

     print lowerVal, "<= X(f) <=", upperVal

########################################
##Tolerence intervals
#########################################
# an interval that includes at least a certain proportion of measurements with  a stated confidence
#K1 and K2 = confidence level of (1-alpha)*100% for p*100%
#xBar +- K2s -> two-sided
# xBar - K1s -> lower Bount
# xBar + K1x -> upper bound
# devlop a 95% tolerance interval for 90%
#p=0.9
#n=25
#confidence=95%
# K2 values table looks for n and p at certain confidences

def k1lower(xBar, k1Val, sampleStdDev):
    lowerVal = xBar - (k1Val*sampleStdDev)
    return lowerVal

def k1upper(xBar, k1Val, sampleStdDev):
    upperVal = xBar + (k1Val*sampleStdDev)
    return upperVal

def k2(xBar, p, k2Val, sampleStdDev):
    #p = x/n
    lowerVal = xBar - (k2Val*sampleStdDev)
    upperVal = xBar + (k2Val*sampleStdDev)
    print lowerVal, "<->", upperVal

##################################################    
##Confidence interval estimation of the proportion
##################################################
# p = X/n
# pi = population proportion
# Z = crit val from normal dist
# n = sample size

def proportionEstimate(p, zValue, sampleSize):
    lowerVal = p - (zValue * ((p*(1-p))/sampleSize)**0.5)
    upperVal = p + (zValue * ((p*(1-p))/sampleSize)**0.5)

    print lowerVal, "<= pi <=", upperVal

def sampleMean(rawData):
    total = 0.0
    for thisDatum in rawData:
        total = total + thisDatum
    return total / len(rawData)

def sampleStdDev(rawData):
    nummer = 0.0
    xBar = sampleMean(rawData)
    for thisDatum in rawData:
        nummer = nummer + (thisDatum - xBar)**2
    denom = len(rawData)-1

    return (nummer/denom)**0.5

##############################################
##Hypothesis Testing
##############################################

#Z Test (sigma known)
#t Test (sigma unknown)
#F Test
#Chi Square Test
#two tailed and one tailed tests
#p-value
#Connection with Confidence interval
#Z Test for the proportion

#Null hypothesis: H0: hypothesis of no difference (from previous readings)
#Alternative hypothesis: H1: something changed
#Always test Null hypothesis
#    ALWAYS refers to scefified value of population parameter (not sample)
#    ALWAYS contains an equal sign (can contain <, >)
#    alternative NEVER contains an equal sign

# critical values calculated by (Z, t, F, chiSquare) based on desired level of significance
# 95% confidence, two-tailed = 1.96, alpha = 0.05
# 95% confidence, one-tailed = 1.645, alpha = 0.05
# 99% confidence, two-tailed = 2.57, alpha = 0.01
# 99.9% confidence, two-tailed = 3.29, alpha = 0.001
# if critical value between acceptance region (confidence interval) can't reject null hypothesis

#Type I error - false negative: NH is rejected when True
#    occurs with a probability of alpha, alpha = level of significance - CHOSEN
#    1-alpha = confidence coefficient
#    common values: 0.05, 0.01 == 95%, 99% confidence

#Type II error - false psitive
#    occurs with a probability of beta, beta = consumer's risk
#    1-beta = power of test (conditional probability of rejecting NH when false and should be rejected)
#    depends on alpha, difference between hypothesized and actual parameter value, and sample size

########
##Z Test
########
def zTest_twoTailed(xBar, mu, sigma, sampleSize):
    #use when sigma is known
    numer = (xBar - mu) 
    denom =  sigma / (sampleSize**0.5)
    zValue = numer / denom
    print "Is %s in the chosen confidence interval?" % str(zValue)
    return zValue

#Hyphothesis Testing
# 1. State Null Hypothesis
# 2. State Alternative Hypothesis
# 3. Choose level of significance, alpha
# 4. Choose sample size, n
# 5. Determine appropriate statistical technique and corresponding test statistic
# 6. Set up critical values that divide rejection and acceptance regions
# 7. Collect Data, xBar, zValue
# 8. Determine if in rejection or acceptance
# 9. Make statisitcal decision
#10. Express statistical decision in terms of the problem

##################
##p-Value approach
##################
# probability of obtaining a test statistic equal to or more extreme than the result obtained from the sample data
# p-Value referred to observed level of significance
# if p-Value is >= alpha, NH is not rejected
# if p-Value is < alpha, NH is rejected

########
#p-Value
########
# probability of Z being more extreme than 1.5 stdDev units
# confidence level chose as 95%, alpha = 0.05
# prob of (Z > +1.5) = 0.5 - .4332 (value found on table A2 for 1.5) = 0.0668
# prob of (Z < -1.5) = 0.0668
# p-Value = 0.1336 (both sides added together)
# if p-Value > alpha -> NH not rejected

def pValueTest():
    return

# 1. State Null Hypothesis
# 2. State Alternative Hypothesis
# 3. Choose alpha
# 4. Choose n
# 5. Determine appropriate technique
# 6. Collect Data
# 7. Calc p-Value
# 8. Compare p-Value and alpha
# 9. Accept or Reject
#10. Express decision in terms of the problem

######################################
##One Tailed Tests (Directional Tests)
## Just put all the alpha on one side of the graph and calculate that.
######################################
# if H0 >= put alpha (rejection area) on the left side
# if H0 <= put alpha (rejection area) on the right side

# if alpha = 0.05 (95%) zValue is 1.645

def tTest(xBar, mu, s, n):
    #use when sigma is unknown
    tValue = (xBar - mu) / (s / (n)**0.5)
    print "Is %s within the acceptance region?" % str(tValue)
    print "DoF: %s" % str(n-1) 
    return tValue

def zTest_proportion(p, pi, n):
    # 
    zValue = (p - pi) / (n * pi * (1-pi))**0.5
    print zValue

#p-Value vs Critical Value
# use probabilities corresponding to values of test statistic
# compare p to alpha instead of t to tC
# does not assume dist is normal

#Connection with Confidence Interval
# Compute the confidence interval for the same statistic
# if the hypothesized population paramer is within the interval, accept the NH
# equivalent to a two-tailed test

# Ztest for difference between two means

def zTest_twoMeans(xBar_one, xBar_two, mu_one, mu_two, sigma_one, sigma_two, sampleSize_one, sampleSize_two):
    numer = (xBar_one - xBar_two) - (mu_one - mu_two)
    denom = ((sigma_one**2 / sampleSize_one) + (sigma_two**2 / sampleSize_two))**0.5
    zValue = numer / denom
    print "Is %s in the acceptance region?" % str(zValue)
    return zValue

def tTest_twoMeans(xBar_1, xBar_2, mu_1, mu_2, n_1, n_2, s_1, s_2):
    ## from two groups where equal and unknown sigmas
    pSV_numer = ((n_1 - 1) * s_1**2) + ((n_2 - 1) * s_2**2) 
    pSV_denom = (n_1 - 1) + (n_2 - 1)
    pSV = pSV_numer / pSV_denom

    numer = (xBar_1 - xBar_2) - (mu_1 - mu_2)
    denom = (pSV * (1/n_1 + 1/n_2))**0.5
    tValue = numer / denom

    print "Pooled Sample Variance: %s" % str(pSV)
    print "DoF: %s" % str(n_1 + n_2 - 2.0)
    return tValue

def tTest_diffMeans(xBar_1, xBar_2, mu_1, mu_2, s_1, s_2, n_1, n_2):
    #random samples form independent groups with normal dist, with unequal
    # and unknown sigma_1 and sigma_2

    #Satterthwaite approximation
    df_numer = (s_1**2 / n_1) + (s_2**2 / n_2)
    df_denom = ((s_1**2 / n_2)**2 / (n_1 - 1)) + ((s_2**2 / n_2)**2 / (n_2 -1))
    df = numer / denom

    tDF_numer = (xBar_1 - xBar_2) - (mu_1 - mu_2)
    tDF_denom - ((s_1**2 / n_1) + (s_2**2 / n_2))**0.5
    tDF = tDF_numer / tDF_denom
 
    print "DoF: %s" % str(df)
    print "tDF: %s" % str(tDF)

def fTest_twoVariances(s_1, s_2):
    fValue = s_1**2 / s_2**2

    fU = 1
    fL = 1/fu
    return fValue







