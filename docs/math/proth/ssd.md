# 样本及抽样分布

## 随机样本

### 总体 个体

研究对象的某项指标的全体称为总体，总体的每个元素称为个体，总体包含的个体称为容量，容量有限的总体称为有限总体

!!! tip
    1. 一个总体对应一个随机变量 $X$，$X$ 的分布函数和数字特征称为总体的分布函数的数字特征
    2. 当研究对象要观测多个数量指标，可用多维随机变量及联合分布来描述整体
    3. 总体包含个体样本很大时，可作为无限总体

$$
简单随机抽样 
\begin{cases} 
随机性：要求总体中每个个体被选入样本的机会均等 \\ \\
独立性：要求样本中每个样品的取值不影响其他的取值
\end{cases}
$$

### 随机样本

#### 样本

与总体独立同分布的 $n$ 个随机变量 $X_1,X_2 \cdots X_n$，称为总体 $X$ 的简单随机样本，简称为样本，其中 $n$ 称为样本容量，相应测定的样本值 $x_1,x_2\cdots x_n$ 称为一组样本观察值，又称为 $X$ 的 $n$ 个独立的观察值，$x_i$ 称为样品

!!! tip
    1. 样本 $X_1,X_2 \cdots X_n$ 也是随机变量，它与总体同分布（由抽样的随机性决定）
    2. $X_1,X_2 \cdots X_n$ 相互独立（由抽样的独立性决定）
    3. 样本是由若干独立同分布随机变量构成

#### 样本的联合分布

设 $X$ 是一个总体，$X_1,X_2 \cdots X_n$ 是来自总体 $X$ 的长度为 $n$ 的样本，由 $X_1,X_2 \cdots X_n$ 独立性可知，若 $X$  的分布函数为 $X$，则 $X_1,X_2\cdots X_n$ 联合分布函数为

$$
F^*(x_1,x_2,\cdots,x_n) = P\{X_1\le x_1,X_2\le x_2,\cdots,X_n \le x_n\} = F(x_1)F(x_2)\cdots F(x_n) = \prod_{i=1}^{n} F(x_i)
$$

联合概率密度为

$$
f^*(x_1,x_2,\cdots,x_n) = \prod_{i=1}^{n} f(x_i)
$$

## 抽样分布

### 统计量

设 $X_1,X_2\cdots X_n$ 为事件总体 $X$ 的一个样本，若样本函数 $g(X_1,X_2,\cdots,X_n)$  中不含分布的未知参数，则 $g(X_1,X_2,\cdots,X_n)$ 为统计量，称 $g(x_1,x_2,\cdots,x_n)$ 为统计量 $g(X_1,X_2,\cdots,X_n)$ 的观察值

### 常用的统计量

- 样本均值：
    - $\overline{X} = \frac{1}{n} \sum_{i=1}^{n} X_i$
    - 观察值：$\overline{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$
- 样本方差：
    - $S^2 = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \overline{X})^2 = \frac{1}{n-1} (\sum_{i=1}^{n} X_i^2 - n\overline{X}^2)$    $ES^2 = DX$    无偏估计
    - $B^2 = \frac{1}{n} \sum_{i=1}^{n}(X_i - \overline{X})^2$    渐近无偏估计
- 样本标准差：$S = \sqrt{S^2} = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (X_i - \overline{X})^2}$
- 样本 $k$ 阶原点矩：$A_k = \frac{1}{n} \sum_{i=1}^{n} X_i^k, k =1,2\cdots$
- 样本 $k$  阶中心矩：$B_k = \frac{1}{n} \sum_{i=1}^{n} (X_i-\overline{X})^k, k =2,3\cdots$

!!! tip
    设 $EX = \mu,DX = \sigma^2$，$X_1,X_2\cdots X_n$  为来自总体 $X$ 的一个样本，$E\overline{X} = \mu,D\overline{X} = \frac{\sigma^2}{n},ES^2=\sigma^2$ 

    证明：

    $$
    \begin{align*}
    E\overline{X} &= E(\frac{1}{n}\sum_{i=1}^{n}X_i) = \frac{1}{n} \sum_{i=1}^{n} EX_i = \frac{1}{n}\cdot n\mu = \mu \\
    D\overline{X} &= D(\frac{1}{n}\sum_{i=1}^{n}X_i) = \frac{1}{n^2} \sum_{i=1}^{n} DX_i = \frac{1}{n^2}\cdot n\sigma^2 = \frac{\sigma^2}{n} \\
    ES^2 &= E(\frac{1}{n-1}(\sum_{i=1}^n X_i^2 - n\overline{X}^2)) = \frac{1}{n-1}(\sum_{i=1}^nEX_i^2 - nE\overline{X}^2) \\
    &= \frac{1}{n-1} [\sum_{i=1}^{n}(\sigma^2+\mu^2) - n(\frac{\sigma^2}{n}+\mu^2)] = \frac{1}{n-1}(n\sigma^2+n\mu^2-\sigma^2-n\mu^2) = \sigma^2
    \end{align*}
    $$

### 抽样分布

#### 上 $\alpha$ 分位点（以标准正态分布为例）

若 $Z_\alpha$ 满足条件 $P\{|X > Z_k|\} = \alpha$，则称 $Z_\alpha$ 为标准正态分布的上 $\alpha$ 分位点

#### $\chi^2$ 分布

- 定义：设 $X_1,X_2\cdots X_n$ 为总体 $N(0,1)$ 的样本，则称统计量 $\chi^2 = X_1^2+X_2^2+\cdots+X_n^2$ 服从自由度为 $n$ 的 $\chi^2$ 分布，记为 $\chi^2 \sim \chi^2(n)$，其概率密度函数为

$$
f(y) = \begin{cases}
\frac{1}{2^{\frac{n}{2}}\Gamma(\frac{n}{2})}y^{\frac{n}{2}-1}e^{-\frac{y}{2}},\ \ y>0 \\
0,\ \ other
\end{cases}
$$

!!! tip
    1. $\chi^2$ 为连续型随机变量
    2. $\chi^2(n)$ 分布中的参数 $n$ 称为自由度


- 性质
    - 可加性：设 $\chi_1^2 \sim \chi^2(n_1),\chi_2^2 \sim \chi^2(n_2)$，且 $\chi_1^2,\chi_2^2$ 相互独立，则 $\chi_1^2 + \chi_2^2 \sim \chi^2(n_1+n_2)$
    
    !!! Abstract
        证明：设 $\chi_1^2 = X_1^2 + X_2^2 + \cdots+ X_n^2, \ \chi_2^2 = Y_1^2 + Y_2^2 + \cdots + Y^2_n$  其中 $X_i \sim N(0,1),Y \sim N(0,1)$ 且相互独立，则
        
        $$
        \chi_1^2 + \chi_2^2 = X_1^2+X_2^2 + \cdots +X_n^2 + Y_1^2+Y_2^2 + \cdots + Y_n^2 \sim \chi^2(n_1+n_2)
        $$
    
    - 若 $\chi^2 \sim \chi^2(n)$，则 $E(\chi^2) = n,\ D(\chi^2) = 2n$
- $\chi^2$  分布的上 $\alpha$ 分位点：对给定的 $\alpha \in (0,1)$，称满足条件 $P\{\chi^2 > \chi_{\alpha}^2(n)\} = \alpha$ 的 $\chi_{\alpha}^2(n)$ 为 $\chi^2(n)$ 的上 $\alpha$ 分位点，也称 $1-\alpha$ 分位数

#### $t$ 分布

- 定义：设 $X \sim N(0,1), \ Y \sim \chi^2(n)$，且 $X,Y$ 相互独立，则称随机变量 $t = \frac{X}{\sqrt{\frac{Y}{n}}}$ 服从自由度为 $n$ 的 $t$ 分布，记为 $t \sim t(n)$

!!! tip
    $t$ 为连续型随机变量，取值 $(-\infin,+\infin)$


- $t$ 分布的上 $\alpha$ 分位点：对给定的 $\alpha \in (0,1)$，称满足条件 $P\{t > t_{\alpha}(n)\} = \alpha$ 的 $t_{\alpha}(n)$ 为 $t(n)$ 的上 $\alpha$ 分位点，也称 $1-\alpha$ 分位数

#### $F$ 分布

- 定义：设 $U \sim \chi^2(n_1),V \sim \chi^2(n_2)$，且 $U,V$ 相互独立，则称随机变量 $F = \frac{U/n_1}{V/n_2}$ 服从自由度为 $(n_1,n_2)$ 的 $F$ 分布，记为 $F \sim F(n_1,n_2)$
- $F$ 分布的上 $\alpha$ 分位点：对给定的 $\alpha \in (0,1)$，称满足条件 $P\{t > F_{\alpha}(n_1,n_2)\} = \alpha$ 的 $F_{\alpha}(n_1,n_2)$ 为 $F(n_1,n_2)$ 的上 $\alpha$ 分位点，也称 $1-\alpha$ 分位数，可知

$$
F_{1-\alpha}(n_1,n_2) = \frac{1}{F_\alpha(n_2,n_1)}
$$

!!! tip
    1. $\chi^2 = X_1^2+X_2^2+\cdots+X_n^2(X_i \sim N(0,1))$
    2. $t = \frac{X}{\sqrt{Y/n}}(X\sim N(0,1),\ Y\sim \chi^2(n))$
    3. $F=\frac{U/n_1}{V/n_2}(U \sim \chi^2(n_1),V \sim \chi^2(n_2))$


### 正态总体的样本均值与样本方差的分布

!!! note "定理1"

    设 $X_1,X_2,\cdots X_n$ 服从正态分布 $X \sim N(\mu,\sigma^2)$，则

    1. $\overline{X} \sim N(\mu,\frac{1}{n}\sigma^2)$
    2. $\frac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)$
    3. $\overline{X}$ 与 $S^2$ 相互独立
    4. $\frac{\overline{X}-\mu}{S/\sqrt{n}} \sim t(n-1)$

!!! note "定理2"
    设 $X_1,X_2,\cdots X_{n_1}$ 服从正态分布 $X \sim N(\mu_1,\sigma_1^2)$，设 $Y_1,Y_2,\cdots Y_{n_2}$ 服从正态分布 $Y \sim N(\mu_2,\sigma_2^2)$’

    1. $\frac{S_1^2/S_2^2}{\sigma_1^2+\sigma_2^2} \sim F(n_1-1,n_2-1)$
    2. 当 $\sigma_1^2=\sigma_2^2=\sigma^2$时

    $$
    \begin{cases}
    \frac{(\overline{X}-\overline{Y})}{S_w\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}} \sim t(n_1+n_2-2) \\
    \\
    S_w^2 = \frac{(n_1-1)S_1^2+(n_2-1)S_2^2}{n_1+n_2-2},\ \ S_w = \sqrt{S_w^2}
    \end{cases}
    $$