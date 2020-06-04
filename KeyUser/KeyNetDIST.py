#python -u "/home/hcs/cc/KeyTimeDIST-win.py"

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
与根微博的空间距离
'''

import pandas as pd

import networkx as nx

KeyUserPath = 'KeyUsers.csv'

KeyUserData = pd.read_csv(KeyUserPath,low_memory=False)

KeyUserData['NetDIST'] = ''

PiecePath = ''

ID2PartData = pd.read_csv(PiecePath+'ID2Part.csv',low_memory=False)

NanList = []

# KeyUserData.shape[0]
for i in range(0,KeyUserData.shape[0]):

    list_temp1 = ID2PartData[
        (ID2PartData.loc[:, '根微博用户ID'] ==
         KeyUserData.loc[i, 'root'])
    ].index.tolist()

    PieceData = pd.read_csv(PiecePath+ID2PartData.loc[list_temp1[0], 'filename'],low_memory=False)

    G = nx.Graph()

    for t in range(0, PieceData.shape[0]):
        G.add_edge(PieceData.loc[t, '转发微博用户ID'], PieceData.loc[t, '父微博用户ID'])

    KeyUserData.loc[i, 'NetDIST'] = \
        nx.shortest_path_length(G,
                                source=KeyUserData.loc[i,'父微博用户ID'],
                                target=KeyUserData.loc[i,'root'])

    # 观察运行情况#########################
    print()
    print(i)
    print(KeyUserData.loc[i, 'NetDIST'])
    ######################################

KeyUserData.to_csv(KeyUserPath,index=0)