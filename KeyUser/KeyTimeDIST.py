#python -u "/home/hcs/cc/KeyTimeDIST.py"

"""
@project: cc
@author: Dong
@file: KeyTimeDIST-win.py
@ide: PyCharm
@time: 2020.05.18-20.46
@code: utf-8
"""

'''
核心用户
与根微博的时间距离
'''

import pandas as pd

KeyUserPath = 'KeyUsers.csv'

KeyUserData = pd.read_csv(KeyUserPath,low_memory=False)

KeyUserData['TimeDIST'] = 0

PiecePath = ''

ID2PartData = pd.read_csv(PiecePath+'ID2Part.csv',low_memory=False)

NanList = []

# KeyUserData.shape[0]
for i in range(0,KeyUserData.shape[0]):
    if( not( KeyUserData.loc[i,'父微博用户ID'] == KeyUserData.loc[i,'root'] ) ):

        list_temp1 = ID2PartData[
            (ID2PartData.loc[:, '根微博用户ID'] ==
             KeyUserData.loc[i, 'root'])
        ].index.tolist()

        PieceData = pd.read_csv(PiecePath+ID2PartData.loc[list_temp1[0], 'filename'],low_memory=False)

        list_temp2 = PieceData[
            (PieceData.loc[:, '转发微博用户ID'] ==
             KeyUserData.loc[i,'父微博用户ID'])
        ].index.tolist()

        if(list_temp2):
            KeyUserData.loc[i, 'TimeDIST'] = PieceData.loc[list_temp2[0], 'TimeDIST']

        else:
            NanList.append(i)


        # 观察运行情况#########################
        print()
        print(i)
        print(KeyUserData.loc[i, 'TimeDIST'])
        print(NanList)
        ######################################

print(KeyUserData)
KeyUserData.drop(labels=NanList,inplace=True)
print(KeyUserData)

KeyUserData.to_csv(KeyUserPath,index=0)