# EHTA
经验传热分析
Empirical Heat Transfer Analysis

EHTA是用开源工具创造的开源软件。
EHTA的说明，手册均采用开源软件进行编辑。

组织形式
EHTA的开发者是任何有兴趣，且自愿进行此工作的人。

理念
EHTA，如其名字所表达的，利用基于经验、半经验的传热公式进行计算。它不使用有限元分析的方法，也无法得出那种方法所得出的温度场等结果。
EHTA所用到的传热计算方法、数值方法、程序运行机理附有尽可能详尽的说明。使用者如果愿意可以用这些说明对程序结果手算复核。
EHTA采用热阻来模拟各传热过程。例如，从换热器的管程向壳程传热，可以视作管侧传热热阻、管壁热阻和壳程热阻的串联。
使用者可以用根据需要进行这些热阻的串联，来模拟不同传热情景。
EHTA是一个库，它的使用是通过在使用者的程序中调用其函数实现的。它可以作为换热器设计程序提供传热计算的内核。但是它不包括机械校核和震动分析的部分。使用者也可以为它定制各种界面。

实现
EHTA能够被python程序方便地使用。
