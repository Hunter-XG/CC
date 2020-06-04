#python -u "D:\\cc\\pycode\\PercentSort.py"

"""
@project: cc
@author: Dong
@file: PercentSort.py
@ide: PyCharm
@time: 2020.05.04-20.40
@code: utf-8
"""

'''
取转发次数降序排列的前5%
作为核心用户的候选者
'''

import pandas as pd

PercentPath = ''
# 转发数字出现次数的统计，源自piececount

CountPath = ''
# 被转发次数的统计，源自piecedata

ResultData = pd.DataFrame(columns=['index','父微博用户ID','count','total','percent','followers','root'])

CountList = []

# 30
for i in range(0,30):

    # 循环读取30个文件

    # 观察数据#########################
    print()
    print('file---' + str(i)+'----begin-begin-begin')
    ###################################

    PercentName = 'percent'+str(i)+'count.csv'
    # 文件名

    PercentData = pd.read_csv(PercentPath+PercentName,low_memory=False)
    # 读入文件

    PercentData = PercentData.sort_values('count',ascending=False)
    # 按count列降序排列

    PercentLine = 0.0
    # 百分比筛选的基准线

    m = 0
    # 默认开始累加百分比的位置

    ResultFile = 'D:\\cc\\percentsort\\Result-10%.csv'
    # 将要保存的文件

    while(True):

        PercentLine = PercentData.iat[m,3] + PercentLine
        # 基准线累加此行的百分比

        if(PercentLine>10.0):
            break
        else:
            m = m + 1
            # 跳到下一行

    CountName = 'part'+str(i)+'count.csv'
    # 文件名

    CountData = pd.read_csv(CountPath+CountName,low_memory=False)
    # 读取piececount文件

    if( m == 0):
        n = 0
        # 若为0，则证明转发量最大的第一条即过线
    else:
        n = m - 1
        # 不为0，则刚好累加到上一条后，最接近线而不过线

    list_temp1 = CountData[
        (CountData.loc[:, 'count'] >=
         PercentData.iat[n,0])
    ].index.tolist()

    # m处跳出循环
    # 此时PercentLine最后一次累加的是
    # m处的百分比
    # 即 累加了m的百分比后过5%
    # 即 累加到m-1刚好最接近5%
    # 则 转发数字大于m-1行数字的
    # 所有转发数字出现次数占比之和
    # 不到5%
    # 即我们筛选的核心用户
    # 即在此事件中
    # 转发次数超过m-1行转发数字的
    # 即视为核心用户
    # df.iat[-1,:] 与 df.iat[0,:] 等价

    # ResultData = pd.read_csv(ResultFile,low_memory=False)
    # 读入累计的核心用户文件

    CountTemp = CountData.loc[list_temp1, :]
    # 提取此次事件的核心用户群

    col_name = CountTemp.columns.tolist()

    col_name.insert(0,'index')

    CountTemp = CountTemp.reindex(columns=col_name)
    # 数据框新增0列为各行数据的序号

    for t in range(0,CountTemp.shape[0]):
        CountTemp.iat[t,0] = t + 1
        # 一次给序号赋值

    # 观察数据#########################
    print()
    print(CountTemp)
    ###################################

    if(CountTemp.empty):
        CountList.insert(0,i)

    ResultData = pd.concat([ResultData, CountTemp])
    # 合并到总的核心用户数据框

    ResultData.to_csv(ResultFile,index=0)
    # 写入到文件

print(CountList)
