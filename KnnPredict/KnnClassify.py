#python -u "/home/cc/KnnClassify.py"

"""
@project: cc
@author: Dong
@file: KnnClassify.py
@ide: PyCharm
@time: 2020.05.20-21.21
@code: utf-8
"""

'''
对核心用户进行分类
'''

def KnnFunc():

    userFeature = pd.read_csv('userFeature.csv')

    userFeature1 = userFeature[(userFeature['count']<1000)].sample(frac=0.5)

    userFeature2 = userFeature[(userFeature['count']>1000)].sample(frac=0.5)
    
    # 随机抽取50%的作为训练集

    trainFeature = pd.concat([userFeature1, userFeature2])

    testFeature = userFeature.drop(labels=trainFeature.index)
    
    # 剩下的50%作为测试集

    knn = neighbors.KNeighborsClassifier()

    # traindata = np.c_[trainFeature['followers'],trainFeature['TimeDIST'],trainFeature['NetDIST']]

    traindata = np.c_[trainFeature['TimeDIST'],trainFeature['NetDIST']]
    
    # 取时间距离和空间距离作为特征

    labels = np.array(trainFeature['feature'])
    
    # 取转发量作为标签

    knn.fit(traindata,labels)
    
    # 训练模型

    # testdata = np.c_[testFeature['followers'],testFeature['TimeDIST'],testFeature['NetDIST']]

    testdata = np.c_[testFeature['TimeDIST'],testFeature['NetDIST']]

    np.array(testFeature['feature'])
    
    # 生成测试集

    result = (knn.predict(testdata) == np.array(testFeature['feature']))
    
    # 预测结果与真实结果的比较

    resultCount = collections.Counter(result)

    hitPercent = 100 * resultCount[True] / (resultCount[True] + resultCount[False])
    
    # 计算预测的准确率

    trainFeature = trainFeature.reset_index()

    trainFeature.to_csv(str(round(hitPercent,2))+'-train.csv',index=0)

    testFeature = testFeature.reset_index()

    testFeature.to_csv(str(round(hitPercent,2))+'-test.csv',index=0)
    
    # 保存训练集和测试集

    return round(hitPercent,2)


import pandas as pd

import numpy as np

from sklearn import neighbors

import collections

percentList = []

# 用于存储准确率

for i in range(0,100):

    k = KnnFunc()
    
    # 得到此次训练的准确率
    
    percentList.append(k)

    #############################
    # 观察运行情况
    print()
    print(i)
    print(k)
    #############################

percentList = pd.DataFrame(data=percentList,columns=['hitpercent'])

percentList.to_csv('percentList31.csv',index=0)

# 保存100次训练的准确率