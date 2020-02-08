#encoding='utf-8'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
import pydotplus
import operator
import pickle
import copy
import re
import os

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
class_name='好瓜'

class TrieNode(object):
    def __init__(self, value=None,label=None, count=0, parent=None,result=None):
        # 值
        self.value = value
        #节点属性
        self.label=label
        # 频数统计
        self.count = count
        # 父结点
        self.parent = parent
        # 子节点，{value:TrieNode}
        self.children = {}
        #最终结果
        self.result=result

def insert(cur_node, dataset,labels):
    classlist = [item[-1] for item in dataset]
    if len(classlist)==0:
        return
    if classlist.count(classlist[0]) == len(classlist):
        child=TrieNode(parent=cur_node,result=classlist[0])
        return
    if len(dataset[0]) == 1:
        child=TrieNode(parent=cur_node,result=majorityCnt(classlist))
        return
    bestfeat = chooseBestFeatureToSplit(dataset)
    bestfeatlabel = labels[bestfeat]
    cur_node.label=bestfeatlabel
    cur_node.count=len(dataset)
    featValues = [item[bestfeat] for item in dataset]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        dataset=splitDataSet(dataset,bestfeat,value)
        child=TrieNode(value=value,count=len(dataset),parent=cur_node)
        cur_node.children[value]=child
        tmp=child #这很重要，不能直接用cur_node
        insert(tmp,dataset,labels)

def createTree0(dataset,labels):
    root=TrieNode()
    insert(root,dataset,labels)
    return root


def createDataset():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


def calcShannonEnt(dataSet):
    number_of_data = len(dataSet)
    labelsCount = {}
    for item in dataSet:
        currentlabel = item[-1]
        if currentlabel not in labelsCount.keys():
            labelsCount[currentlabel] = 0
        labelsCount[currentlabel] += 1
    ShannonEnt = 0
    for key in labelsCount:
        prob = float(labelsCount[key] / number_of_data)
        ShannonEnt -= prob * np.log2(prob)
    return ShannonEnt


def splitDataSet(dataSet, index, value):
    retDataset = []
    for item in dataSet:
        if item[index] == value:
            reduceditem = item[:index]
            reduceditem.extend(item[index + 1:])
            retDataset.append(reduceditem)
    return retDataset


def chooseBestFeatureToSplit(dataSet):
    number_of_features = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain, bestFeature = 0.0, -1
    for i in range(number_of_features):
        featurelist = [item[i] for item in dataSet]
        uniqueVals = set(featurelist)
        newEntropy = 0
        for value in uniqueVals:
            subdataset = splitDataSet(dataSet, i, value=value)
            prob = float(len(subdataset) / len(dataSet))
            newEntropy += prob * calcShannonEnt(subdataset)
        infoGain = baseEntropy - newEntropy  # 信息增益
        # print(
        #     'infoGain=',
        #     infoGain,
        #     'bestFeature=',
        #     i,
        #     baseEntropy,
        #     newEntropy)
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classlist):
    classcount={}
    for item in classlist:
        if item not in classcount.keys():
            classcount[item]=0
        classcount[item]+=1
    sortedclasscount=sorted(classcount,key=operator.itemgetter(1),reverse=True)
    return sortedclasscount[0][0]

def createTree(dataset, labels):
    classlist = [item[-1] for item in dataset]
    if classlist.count(classlist[0]) == len(classlist):
        return classlist[0]
    if len(dataset[0]) == 1:
        return majorityCnt(classlist)
    bestfeat = chooseBestFeatureToSplit(dataset)
    bestfeatlabel = labels[bestfeat]
    mytree = {bestfeatlabel: {}}
    # 取出最优列，然后它的branch做分类
    featValues = [example[bestfeat] for example in dataset]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        # 求出剩余的标签label
        subLabels = labels[0:bestfeat]+labels[bestfeat+1:]
        # 遍历当前选择特征包含的所有属性值，在每个数据集划分上递归调用函数createTree()
        mytree[bestfeatlabel][value] = createTree(
            splitDataSet(dataset, bestfeat, value), subLabels)
        # print 'myTree', value, myTree
    return mytree

def createtreeclass(dataset,labels): #输出极其不稳定
    classlist = [item[-1] for item in dataset]
    if classlist.count(classlist[0]) == len(classlist):
        return
    if len(dataset[0]) == 1:
        return

def classify(inputTree, featLabels, testVec):
    """
    给输入的节点，进行分类
    Args:
        inputTree  决策树模型
        featLabels Feature标签对应的名称
        testVec    测试输入的数据
    Returns:
        classLabel 分类的结果值，需要映射label才能知道名称
    """
    # 获取tree的根节点对于的key值
    keys=[k for k in inputTree.keys()]
    firstStr = keys[0]
    # 通过key得到根节点对应的value
    secondDict = inputTree[firstStr]
    # 判断根节点名称获取根节点在label中的先后顺序，这样就知道输入的testVec怎么开始对照树来做分类
    featIndex = featLabels.index(firstStr)
    # 测试数据，找到根节点对应的label位置，也就知道从输入的数据的第几位来开始分类
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    # print ('+++', firstStr, 'xxx', secondDict, '---', key, '>>>', valueOfFeat)
    # 判断分枝是否结束: 判断valueOfFeat是否是dict类型
    if isinstance(valueOfFeat, dict):
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else:
        classLabel = valueOfFeat
    return classLabel



def test_acuracy(inputTree,labels,testdata):
    count = 0
    len_of_testdata = len(testdata)
    for item in testdata:
        if classify(inputTree, labels, item[:-1]) == item[-1]:
            count += 1
    return count / len_of_testdata

def classify_accuracy(D, label):
    return D.loc[D["好瓜"] == label].shape[0]


# def post_pruning(tree,traindata,testdata):


def storeTree(inputTree, filename):
    with open(filename, 'wb') as fw:
        pickle.dump(inputTree, fw)

def grabTree(filename):
    with open(filename) as f:
        pickle.load(f)


def get_tree_height(tree):
    if not isinstance(tree, dict):
        return 1
    maxheight=0
    keys=[k for k in tree.keys()]
    childrentrees=[tree[key] for key in keys]
    for childtree in childrentrees:
        childheight=1+get_tree_height(childtree)
        if childheight>maxheight:
            maxheight=childheight
    return maxheight

def fishTest():
    dataset,labels=createDataset()
    myTree = createTree(dataset, copy.deepcopy(labels))
    print(myTree)
    # [1, 1]表示要取的分支上的节点位置，对应的结果值
    print(classify(myTree, labels, [1, 1]))
    print(classify(myTree, labels, [1, 0]))
    print(classify(myTree, labels, [0, 1]))
    # 获得树的高度
    print(get_tree_height(myTree))

def ContactLensesTest():
    """
    Desc:
        预测隐形眼镜的测试代码
    Args:
        none
    Returns:
        none
    """
    # 加载隐形眼镜相关的 文本文件 数据
    with open('lenses.txt') as fr:
        # 解析数据，获得 features 数据
        lenses = [inst.strip().split('\t') for inst in fr.readlines()]
        # 得到数据的对应的 Labels
        lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
        # 使用上面的创建决策树的代码，构造预测隐形眼镜的决策树
        lensesTree = createTree(lenses, lensesLabels)
        print(lensesTree)
        print(get_tree_height(lensesTree))

def WatermelonTest():
    melon = np.loadtxt('watermelon.txt',delimiter='\t',dtype=str,encoding='utf-8')
    pattern = re.compile(r"[ ]+")
    traindata=[]
    testdata=[]
    trainindex=[1,2,3,6,9,10,13,14,15,16]
    testindex=set(range(1,17))-set(trainindex)
    for i in trainindex:
        a = re.split(pattern, melon[i])
        traindata.append(a)
    for i in testindex:
        a=re.split(pattern,melon[i])
        testdata.append(a)
    labels=re.split(pattern,melon[0])[:-1]
    # treeroot = createTree0(dataset=traindata, labels=labels)
    # print(treeroot.children)
    # cur_node=treeroot
    # next_node=list(cur_node.children.values())
    # for item in next_node:
    #     print(item.children)
    # print(next_next_node.children)
    watermelonTree = createTree(traindata, labels)
    print(watermelonTree)
    print(test_acuracy(watermelonTree,labels,testdata))
    # d=pd.DataFrame(testdata)
    # print(classify_accuracy(d, labels[0]))
    # count=0
    # len_of_testdata=len(testindex)
    # for item in testdata:
    #     if classify(watermelonTree,labels,item[:-1])==item[-1]:
    #         count+=1
    # print(count/len_of_testdata)


if __name__ == "__main__":
    # fishTest()
    # ContactLensesTest()
    WatermelonTest()