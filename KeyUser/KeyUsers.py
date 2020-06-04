#python -u "D:\\cc\\pycode\\KeyUsers.py"

"""
@project: cc
@author: Dong
@file: KeyUsers.py
@ide: PyCharm
@time: 2020.05.07-19.20
@code: utf-8
"""

'''
筛选出CphsI-10.csv和Result-6%.csv中重合的部分
'''

import pandas as pd

CphsIPath = 'Average.csv'

ResultPath = 'Result-6%.csv'

CphsIData = pd.read_csv(CphsIPath,low_memory=False)

ResultData = pd.read_csv(ResultPath,low_memory=False)

KeyUsers = pd.DataFrame(columns=['index','父微博用户ID','count','total','percent','followers','root'])

list1 = []

# alltime.shape[0]-1
for i in range( 0 , CphsIData.shape[0] ) :

    # 观察运行情况#########################
    print()
    print(i)
    ######################################

    list_temp1 = []
    list_temp1 = CphsIData[
        (CphsIData.loc[ i , '父微博用户ID'] ==
         ResultData.loc[ : , '父微博用户ID'])
        ].index.tolist()
    # 获取符合条件的行的索引值

    if (list_temp1) :
    # 如果列表不空，即找到对应值

        for t in range(0,len(list_temp1)):
            if(
            (CphsIData.loc[ i , 'count'] == ResultData.loc[ list_temp1[t] , 'count'])
            and
            (CphsIData.loc[ i , 'total'] == ResultData.loc[ list_temp1[t] , 'total'])
            ) :

                # 观察运行情况#########################
                print()
                print("yes")
                print(CphsIData.loc[ i , '父微博用户ID'])
                print(ResultData.loc[ list_temp1[0] , '父微博用户ID'])
                print(list_temp1)
                ######################################

                list_temp2 = []
                list_temp2.append(list_temp1[t])

                KeyUsersTemp = ResultData.loc[list_temp2, :]

                KeyUsers = pd.concat([KeyUsers, KeyUsersTemp])

                KeyUsers.to_csv('D:\\cc\\KeyUsers.csv',index=0)

                break

    else :
    # 列表空，无对应，记下此时的行数
        list1.append(i)

        # 观察运行情况#########################
        print()
        print("no")
        ######################################

# 打印time中在score找不到的行数
print()
print("finish-----------------------------------")
print(list1)