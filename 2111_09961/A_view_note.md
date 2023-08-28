# Abstract
关于机器学习对抗的综述，其中所有的代码均开源
# Introduction
机器学习在许多任务中（图像分类，语音识别，机器翻译和游戏）容易收到对抗例子的干扰

对图像叠加一个微小的扰动，人眼无法看出区别但是对于原本分类正确的模型造成干扰。对于线性模型、逻辑回归和基于树的模型均有作用。因此存在两方面研究
- 攻击
- 防御
在连续输入和离散输入均有影响

相关资料
- 物体检测领域 Serban, A., Poll, E. and Visser, J. (2020) Adversarial examples on object recognition: A compre-hensive survey. ACM Computing Surveys (CSUR), 53, 1–38.
- 计算机视觉与自然语音处理 Qiu, S., Liu, Q., Zhou, S. and Wu, C. (2019) Review of artificial intelligence adversarial attack and defense technologies. Applied Sciences, 9, 909.
  
    Raghuram, J., Chandrasekaran, V., Jha, S. and Banerjee, S. (2020) Detecting anomalous inputs to DNN classifiers by joint statistical testing at the layers. arXiv preprint arXiv:2007.15147.

    Ren, K., Zheng, T., Qin, Z. and Liu, X. (2020) Adversarial attacks and defenses in deep learning Engineering, 6, 346–360.
# Deep Neural Networks

# Attack
对抗攻击是根据自然样本和被攻击模型生成对抗性示例的过程,目标是生成一个很小的扰动$\delta$使得
$$
    \mathbf{x}^* = \mathbf{x} + \delta
$$
让被攻击模型错误分类。

攻击分为两种：
- 有目标攻击(targeted attack) 使对抗样本被分类为目标类别
- 无针对性(untargeted attack) 使对抗样本分错误即可

攻击方法分为三种:
- 基于梯度 (Gradient-Based)
- 基于分数 (Score-Based)
- 基于决策 (decision-Based)

最近研究表明多种类别攻击的组合可能导致更强大的攻击

情景分为两种：
- 黑盒 只有预测结果(score)可知
- 白盒 全部参数可知
- 灰盒 部分参数可知 
  
## 3.1 Gradient-Based Attack

利用损失函数的梯度来形成对抗例子的输入

|   <h5> 例子|
|:------|
|   <li> FGSM 快速梯度符号法 |
|   <li> BIM 和 PGD 快速梯度迭代法的对比版本 | 

### FGSM
[FGSM_note](./FGSM_note.md)

## 3.2