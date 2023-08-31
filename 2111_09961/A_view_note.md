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

## 3.2 Score-Based Attack
攻击时有时无法获得梯度信息，于是从分类器的结果进行攻击。
|<h5>论文|成果|
|:-----|-|
|Chen, P.-Y., Zhang, H., Sharma, Y., Yi, J. and Hsieh, C.-J. (2017) Zoo: Zeroth order optimization based black-box attacks to deep neural networks without training substitute models. In
Proceedings of the 10th ACM Workshop on Artificial Intelligence and Security, 15–26.|利用分数信息估计梯度,并制造对抗样本|
|Ilyas, A., Engstrom, L., Athalye, A. and Lin, J. (2018) Black-box adversarial attacks with limited queries and information. In International Conference on Machine Learning, 2137–2146.|利用自然进化策略估计梯度|

基于分数攻击可分为以下两类
### Gradient-approximation based methods 
梯度近似方式
ZOO（Zeroth Order Optimization Based Attack）方式是一种梯度近似的方式
$$
    \frac{\partial f(\mathbf{x})}{\partial x_{(i)}}\approx\frac{f(\mathbf{x}-h \mathbf{e}_i)-f(\mathbf{x}-h \mathbf{e} _i)}{2h}
$$
其中，h为一个小常数，$\mathbf{e} _i$为一个标准基向量,在输入维度很大的情况下，引入了几种技术来扩大估计。
|论文|成果|
|--|--|
|Chen, P.-Y., Zhang, H., Sharma, Y., Yi, J. and Hsieh, C.-J. (2017) Zoo: Zeroth order optimization based black-box attacks to deep neural networks without training substitute models. In Proceedings of the 10th ACM Workshop on Artificial Intelligence and Security, 15–26.|ZOO|
|Ilyas, A., Engstrom, L., Athalye, A. and Lin, J. (2018) Black-box adversarial attacks with limited queries and information. In International Conference on Machine Learning, 2137–2146.|NES|
|Ilyas, A., Engstrom, L. and Madry, A. (2019) Prior convictions: Black-box adversarial attacks with bandits and priors. In International Conference on Learning Representations.|Bandits Attack|
NES估计出损失梯度后，根据估计梯度生成对抗性示例
$$
\frac{1}{\sigma n}\sum_{i=1}^{n}\mathbf{\delta} _i f(\mathbf{x}+\sigma \mathbf{\delta}_i)
$$
其中n为估计梯度的搜索次数，$\delta _i$为$\mathcal{N}(0,I)$采样的随机方向，$\sigma$是搜索步骤的标准偏差。