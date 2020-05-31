# Computational Communication

第二届传播数据挖掘竞赛

汕大凤凰花队

核心用户挖掘与传播规模预测

## 数据描述

### KnnPredict

* `userFeature.csv`：核心用户的行为特征及其微博的传播规模
  * `index`：该数据在原始集中的位置
  * `父微博用户ID`：该数据的用户身份标识
  * `count`：被转发量
  * `followers`：粉丝量
  * `TimeDIST`：与该事件根微博的时间距离
  * `NetDIST`：与该事件根微博的空间距离
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


