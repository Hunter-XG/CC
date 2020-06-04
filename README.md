# Computational Communication

第二届传播数据挖掘竞赛

汕大凤凰花队

核心用户挖掘与传播规模预测

## 数据描述

* 以下描述中的该用户均代指转发数据中的转发用户

### KnnPredict

* `userFeature.csv`：核心用户的行为特征及其微博的传播规模
  * `index`：该数据在原始集中的位置
  * `父微博用户ID`：该数据的用户身份标识
  * `count`：被转发量
  * `followers`：粉丝量
  * `TimeDIST`：与该事件根微博的时间距离
  * `NetDIST`：该事件用户传播网络中该用户与根微博的距离
  * `feature`：该数据的标签

* `percent-train.csv` ：准确率为percent的训练集
  
  * 同上 

* `percent-test.csv` ：准确率为percent的测试集

  * 同上 

* `KnnClassify.py`：训练代码

  * 详见代码注释
  
* `percentList.csv`：准确率
  * `index`： 训练序号
  * `hitpercent`：该训练的准确率


### SortPercent

* `Result-percent.csv`：所有事件中转发量前percent的用户
  * `index`：该数据在原始集中的位置
  * `父微博用户ID`：该数据的用户身份标识
  * `count`：被转发量
  * `total`：该事件总转发量
  * `percent`：该转发量的占比
  * `followers`：粉丝量
  * `root`：该转发数据的根用户
  
* `SortPercent.py`：取所有事件中，前percent的用户
   * 详见代码注释


### KeyUsers

* `Average.csv`：所有事件中转发量大于该事件平均转发量的用户
  * `index`：该数据在原始集中的位置
  * `父微博用户ID`：该数据的用户身份标识
  * `count`：被转发量
  * `total`：该事件总转发量
  * `percent`：该转发量的占比
  * `followers`：粉丝量
  * `root`：该转发数据的根用户
  * `CphsI`：该用户的转发量除以该事件的平均转发量得到的指数

* `KeyUsers.csv`：核心用户
  * `父微博用户ID`：该数据的用户身份标识
  * `count`：被转发量
  * `total`：该事件总转发量
  * `percent`：该转发量的占比
  * `followers`：粉丝量
  * `TimeDIST`：与该事件根微博的时间距离
  * `NetDIST`：该事件用户传播网络中该用户与根微博的距离
  
* `KeyUsers.py`：取Result-6%.csv和Average.csv中重叠的转发用户作为核心用户
   * 详见代码注释
  
* `KeyNetDIST.py`：计算该用户与该事件根用户在用户传播网络中的距离
  * 详见代码注释
  
* `KeyTimeDIST.py`：计算该用户与该事件根用户的时间距离
  * 详见代码注释