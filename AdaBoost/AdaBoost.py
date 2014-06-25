# coding=gbk
import numpy as np
import scipy
import math

def loadSimpData():
    datMat = np.matrix( [[ 1. , 2.1],
                     [ 2. , 1.1],
                     [ 1.3, 1. ],
                     [ 1. , 1. ],
                     [ 2. , 1. ]] )
    classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return datMat,classLabels

#通过阀值比较对数据进行分类
def stumpClassify(dataMatrix,dimen,threshVal,threshIneq):
    retArray=np.ones((np.shape(dataMatrix)[0],1))
    if threshIneq == 'lt':
        #很巧妙的分类写法
        retArray[dataMatrix[:,dimen] <= threshVal] = -1.0
    else:
        retArray[dataMatrix[:,dimen] > threshVal]=-1.0
    return retArray

#遍历stumpClassify()函数所有的可能输入值，并找到数据集上最佳的单层决策树。即弱学习器
def buildStump(dataArr,classLabels,D):
    dataMatrix = np.mat(dataArr); labelMat = np.mat(classLabels).T
    m,n = np.shape(dataMatrix)#m个例子，每个例子n维
    numSteps = 10.0
    bestStump = {}#用于存储给定权重向量D时所得到的最佳单层决策树的相关信息。
    bestClasEst = np.mat(np.zeros((m,1)))
    minError=np.inf
    for i in range(n):#在数据集的所有特征上遍历
        rangeMin = dataMatrix[:,i].min(); rangeMax = dataMatrix[:,i].max();
        stepSize = (rangeMax-rangeMin)/numSteps
        for j in range(-1,int(numSteps)+1):
            for inequal in ['lt','gt']:
                threshVal = (rangeMin + float(j)* stepSize)
                predictedVals= \
                    stumpClassify(dataMatrix,i,threshVal,inequal)
                errArr = np.mat(np.ones((m,1)))
                errArr[predictedVals == labelMat] = 0
                #计算加权错误率
                weightedError=D.T*errArr
                #print "split:dim %d,thresh %.2f,thresh inequal: %s,the weighted error is %.3f" %(i,threshVal,inequal,weightedError)
                if weightedError< minError:
                    minError = weightedError
                    bestClasEst=predictedVals.copy();
                    bestStump['dim']=i
                    bestStump['thresh']=threshVal
                    bestStump['ineq']=inequal
    return bestStump,minError,bestClasEst

#输入包括数据集，类别标签以及迭代次数numIt,Decision stump ,是AdaBoost 最流行的的弱分类器
def adaBoostTrainDS(dataArr,classLabels,numIt=40):
    weakClassArr=[]
    m=np.shape(dataArr)[0]
    D=np.mat(np.ones((m,1))/m)
    aggClassEst=np.mat(np.zeros((m,1)))
    for i in range(numIt):
        bestStump,error,classEst=buildStump(dataArr,classLabels,D)
        print "D:",D.T
        alpha = float(0.5 * math.log((1.0-error)/max(error,1e-16)))#alpha值计算
        bestStump['alpha']=alpha
        weakClassArr.append(bestStump)
        print "classEst: ",classEst.T
        #计算下一次迭代中的新权重D
        expon= np.multiply(-1 * alpha * np.mat(classLabels).T,classEst)
        D= np.multiply(D,np.exp(expon))
        D= D/D.sum()
        #通过aggClassEst 变量保持运行时的类别估计值来实现2..
        aggClassEst += alpha * classEst
        print "aggClassEst: ",aggClassEst.T
        aggErrors= np.multiply(np.sign(aggClassEst) != np.mat(classLabels).T,np.ones((m,1)))
        errorRate = aggErrors.sum()/m
        print "total error: ",errorRate,"\n"
        if errorRate == 0.0:break
    return weakClassArr

def adaClassify(datToClass,classifierArr):
    dataMatrix = np.mat(datToClass)
    m = np.shape(dataMatrix)[0]
    aggClassEst = np.mat(np.zeros((m,1)))
    for i in range(len(classifierArr)):
        classEst = stumpClassify(dataMatrix,classifierArr[i]['dim'],classifierArr[i]['thresh'],classifierArr[i]['ineq'])
        aggClassEst += classifierArr[i]['alpha']* classEst
        print aggClassEst
    return np.sign(aggClassEst)

#引进新数据
def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t'))
    dataMat = [];labelMat=[]
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat-1):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat












