# Search Gradients & Search Distribution
假设已知一个概率分布函数（$\theta$为参数）$\pi_{\theta}$,为了得出最优的参数$\theta^*$，使用梯度下降法。
为了获取近似梯度，在样本中挑选$\lambda$个样本，满足$\mathbf{z} _k\sim \pi_\theta$.
评价$\theta$的函数为
$$
J(\theta)=\int f(\mathbf{z})\pi_{\theta} (\mathbf{z})d \mathbf{z}
$$

对$J(\theta)$进行梯度下降，则


$$
\begin{align*}
\nabla_\theta J(\theta)=\nabla_\theta \int f(\mathbf{z})\pi_\theta (\mathbf{z})d \mathbf{z}=\int f(\mathbf{z})\pi_\theta(\mathbf{z})\nabla_\theta log \pi_\theta(\mathbf{z})d \mathbf{z}&=E_\theta \left[f(\mathbf{z})\nabla_\theta log \pi_\theta(\mathbf{z}) \right] \\
\nabla log \pi_\theta(\mathbf{z})&=\frac{1}{\pi_\theta(\mathbf{z})}\nabla \mathbf{\pi_\theta(\mathbf{z})}
\end{align*}
$$
使用梯度下降
$$
    \theta\leftarrow\theta+\eta\nabla_\theta J(\theta)
$$
算法
|Algorithm 1:Canonical Search Gradient algorithm|
|--|
|$\mathbf{input}:f,\theta_{init}$<br/>$\mathbf{repeat}$ <br/>$\ \ \ \ \mathbf{for}\ \  k=1\dots\lambda \ \ do$<br/>$\ \ \ \ \ \ \ \ draw\ sample\ z_k \sim \pi(\cdot\vert\theta)$<br/>$\ \ \ \ \ \ \ \ evaluate\  the\  fitness\ f(\mathbf{z}_k)$<br/> $\ \ \ \ \ \ \ \  calculate\ log-derivatives\ \nabla_\theta log \pi(\mathbf{z} _k\vert \theta)$<br/>$\ \ \ \ \mathbf{end}$<br/>$$\nabla_\theta J\leftarrow \frac{1}{\lambda}\sum^{\lambda}_{k=1}\nabla_\theta\log\pi(\mathbf{z} _k\vert \theta)\cdot f(\mathbf{z} _k)$$ $\ \ \ \ \ \ \ \ \ \theta\leftarrow \theta + \eta\cdot\nabla_\theta J$<br/> $\mathbf{until} \ stop\ criterion\ is\ met$|
上述方式存在一个问题，就是模型非常不稳定，且依赖初始值。
# Natural Gradient
在Natural Gradient中使用 $D(\theta^{'}\Vert\theta)$来表示两个概率分布$\pi_\theta(\mathbf{z})$和$\pi_{\theta^{'}}(\mathbf{z})$的距离。我们在每一次更新参数的时候，我们希望在限定的距离内，往gradient最陡的方向走：
$$
\begin{align*}
max_{\Delta\theta}J(\theta+\Delta\theta)\approx J(\theta)+\Delta\theta^T\nabla_\theta J\\
s.t.D(\theta+\Delta\theta\Vert\theta)=\epsilon
\end{align*}
$$
当$\Delta\theta\rightarrow 0$时，我们有
$$
\begin{align*}
D(\theta+\Delta\theta\Vert\theta)&=\frac{1}{2}\Delta\theta^\top F(\theta)\Delta\theta\\
F(\theta)&=\int\pi_\theta(\mathbf{z})\nabla_\theta\log\pi_\theta(\mathbf{z})^\top \mathbf{dz}\\
&=E\left[\nabla_\theta\log\pi_\theta(\mathbf{z})\nabla_\theta\log\pi_\theta(\mathbf{z})^\top\right]
\end{align*}
$$