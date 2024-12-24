---
stas: true
comment: True
---

# 随机变量的数字特征

## 数学期望

### 离散型随机变量的数学期望

#### 定义

设离散型随机变量 $X$ 的分布律为 $P\{X = x_k\} = p_k (k=1,2\cdots n)$，若级数 $\sum_{k=1}^{\infin} x_k p_k$ 绝对收敛（即 $\sum_{k=1}^{\infin} |x_k p_k|$  绝对收敛），则称级数 $\sum_{k=1}^{\infin} x_k p_k$  为 $X$ 的数学期望，简称期望，也称均值，记作 $E(X)$ 或 $EX$，否则期望不存在

!!! tip
    1. $E(X)$ 为一个实数，而非变量，其为一种加权平均。它从本质上体现随机变量取可能值的真正平均值，也称均值
    2. 随机变量取值随机，不可能要求 $X$ 按 $x_1,x_2\cdots x_3$ 的顺序逐个取，在求和时可能会改变项的顺序，要求 $\sum_{k=1}^{\infin}$  绝对收敛保证了级数的和不会随着各项次序的改变而改变，因而期望是唯一存在的


### 连续型随机变量的数学期望

#### 定义

设连续型随机变量 $X$ 的概率密度为 $f(x)$，若广义积分 $\int_{-\infin}^{+\infin}xf(x)\mathrm{d}x$ 绝对收敛，则称积分 $\int_{-\infin}^{+\infin}xf(x)\mathrm{d}x$ 为 $X$ 的数学期望，简称期望，也称均值，记作 $E(X)$ 或 $EX$，否则期望不存在

### 随机变量函数的数学期望

#### 定理

设 $Y$ 为随机变量 $X$ 的函数，记 $Y = g(X)$

- 如果 $X$ 为离散型随机变量，它的分布律 $P\{X = x_k\} = p_k(k=1,2\cdots )$，若 $\sum_{k=1}^{\infin}g(x_k)p_k$ 绝对收敛，则有

$$
E(Y) = E(g(x)) = \sum_{k=1}^{\infin} g(x_k)p_k
$$

- 如果 $X$ 为连续型随机变量，它的概率密度为 $f(x)$，若 $\int_{-\infin}^{+\infin} f(x)g(x)\mathrm{d}x$ 绝对收敛，则有

$$
E(Y) = E(g(x)) = \int_{-\infin}^{+\infin} g(x)f(x)\mathrm{d}x
$$

### 二维随机变量的数学期望

若 $Z = g(X,Y)$，$g(X,Y)$ 为连续函数

- 若 $(X,Y)$ 为离散型随机变量，其分布律为 $P\{X=x_i,Y=y_j\} = p_{ij}(i,j=1,2\cdots n)$，若级数 $\sum_{i=1}^{\infin}\sum_{j=1}^{\infin}g(x_i,y_j)p_{ij}$ 绝对收敛，则有

$$
Eg(X,Y) = \sum_{i=1}^{\infin}\sum_{j=1}^{\infin}g(x_i,y_j)p_{ij}
$$

- 若 $(X,Y)$ 为连续型随机变量，其分布律为 $f(x,y)$，若级数 $\int_{-\infin}^{+\infin} g(x,y)f(x,y) \mathrm{d}x\mathrm{d}y$ 绝对收敛，则有

$$
Eg(X,Y) = \int_{-\infin}^{+\infin}\int_{-\infin}^{+\infin} g(x,y)f(x,y) \mathrm{d}x\mathrm{d}y
$$

### 期望的性质

1. $E(\mathrm{C}) = \mathrm{C}$
2. $E(\mathrm{C}X) = \mathrm{C}E(X)$
3. $E(X+Y) = E(X) + E(Y)$

推广：对于 $X_1,X_2\cdots X_n$ 有 $E(X_1+X_2+\cdots+X_n) = E(X_1) + E(X_2) + \cdots + E(X_n)$

1. 若 $X,Y$ 相互独立，则 $E(XY) = E(X)E(Y)$

推广：若 $X_1,X_2\cdots X_n$ 相互独立，则 $E(X_1X_2\cdots X_n) = E(X_1)  E(X_2)\cdots E(X_n)$

## 方差

### 方差

#### 定义

假设 $X$ 为一个随机变量，若 $E(X-EX)^2$ 存在，则称 $E(X-EX)^2$ 为 $X$ 的方差，记作 $D(X)$  或 $DX$，即

$$
D(X) = E(X-EX)^2
$$

而 $\sqrt{D(X)}$ 称为 $X$ 的均方差或标准差

!!! tip
    方差反映了 $X$ 的取值与期望的偏离程度，刻画了随机变量取值的分散程度

#### 计算

1. 定义法
    - 离散型：$DX = \sum_{k=1}^{\infin} (x_k - EX)^2 p_k$
    - 连续型：$DX = \int_{-\infin}^{+\infin} (x-EX)^2f(x)\mathrm{d}x$
2. 公式法

$$
\begin{align*}
DX &= E(X-EX)^2 = E(X^2-2X\cdot EX + (EX)^2) \\
&= E(X) -2(EX)^2 + (EX)^2 \\ &= EX^2 - (EX)^2
\end{align*} 
$$

#### 性质

1. $D\mathrm{C} = 0$
2. $D(\mathrm{C}X) = E(\mathrm{C}X)^2 - [E(\mathrm{C}X)]^2 = \mathrm{C}^2EX^2 - \mathrm{C}^2(EX)^2 = \mathrm{C}^2 DX$


!!! tip
    若 $a,b$ 为常数，$D(aX+b)= a^2DX$

3. 设 $X$ 为随机变量，$\mathrm{C}$ 为常数，且 $\mathrm{C} \neq EX$，则 $DX < E(X-\mathrm{C})^2$
4. 设 $X,Y$ 相互独立，则 $D(X\pm Y) = DX + DY$ 


!!! tip
      - 证明：

    $$
    \begin{align*}
    D(X+Y) &= E[(X+Y)-E(X+Y)]^2\\ &= E[(X-EX)+(Y-EY)]^2 \\ &= E[(X-EX)^2+2(X-EX)(Y-EY)+(Y-EY)^2] \\ &=E(X-EX)^2 + E(Y-EY)^2 + 2E(X-EX)(Y-EY) \\ &= DX + DY + 2E(X-EX)(Y-EY)
    \end{align*} 
    $$

    又 $X,Y$ 相互独立，此时 $E(X-EX)(Y-EY) = 0$，则 $D(X+Y) = DX + DY$

    - 推广：对于 $n$ 个相互独立的随机变量 $X_1,X_2\cdots X_n$

    $$
    D(X_1 \pm X_2 \pm \cdots \pm X_n) = DX_1 + DX_2 + \cdots + DX_n 
    $$

5. $D(X) = 0 \Leftrightarrow P\{X=E(X)\} = 1$

!!! tip
    设随机变量 $X$，$EX = \mu$，$DX = \sigma^2 \neq 0$ 记 $X^* = \frac{X-EX}{\sqrt{DX}} = \frac{X-\mu}{\sigma}$，则 $EX^* = 0$，$DX^* = 1$

### 常用分布的期望与方差

$$
\begin{array}{|c|c|c|c|}\hline\textbf{分布类型} & \textbf{参数范围} & \textbf{期望值 (EX)} & \textbf{方差 (DX)} \\\hline0-1 \text{ 分布} & p \in [0,1] & p & pq \\\hline\text{二项分布} & n \in \mathbb{N}, \, p \in [0,1] & np & npq \\\hline\text{泊松分布} & \lambda > 0 & \lambda & \lambda \\\hline\text{均匀分布} & a < b, \, a, b \in \mathbb{R} & \frac{a+b}{2} & \frac{(b-a)^2}{12} \\\hline\text{指数分布} & \theta > 0 & \theta & \theta^2 \\\hline\text{正态分布} & \mu \in \mathbb{R}, \, \sigma^2 > 0 & \mu & \sigma^2 \\\hline\end{array}
$$

## 协方差及其相关系数

### 协方差

#### 定义

设 $X,Y$ 为两个随机变量，若 $E[(X-EX)(Y-EY)]$ 存在，则称其为随机变量 $X,Y$ 的协方差，记为 $\mathrm{Cov}(X,Y)$


!!! tip
      - $\mathrm{Cov}(X,Y)$ 刻画了 $X$ 和 $Y$ 线性关系的强弱
      - 协方差的计算公式：$\mathrm{Cov}(X,Y) = EXY - EXEY$
      - $D(X\pm Y) = DX + DY \pm 2\mathrm{Cov}(X,Y)$

#### 性质

1. $\mathrm{Cov}(X,Y) = \mathrm{Cov}(Y,X)$
2. $\mathrm{Cov}(aX,bY) = ab\mathrm{Cov}(X,Y)$
3. $\mathrm{Cov}(X_1+X_2,Y) = \mathrm{Cov}(X_1,Y) + \mathrm{Cov}(X_2,Y)$ 及 $\mathrm{Cov}(X,Y_1+Y_2) = \mathrm{Cov}(X,Y_1) + \mathrm{Cov}(X,Y_2)$

### 相关系数

#### 定义

称 $\rho_{XY} = \frac{\mathrm{Cov}(X,Y)}{\sqrt{EX}\sqrt{EY}}$ 为 $X,Y$ 的相关系数或标准协方差

#### 性质

设 $\rho_{XY}$ 为 $X,Y$ 的相关系统，则

1. $|\rho_{XY}| \le 1$
2. $|\rho_{XY}|$ 的充要条件是 $X,Y$ 的依概率线性相关，即存在常数 $a,b$ 使 $P\{Y=ax+b\} = 1$

#### 意义

1. $|\rho_{XY}|$ 越接近 $1$，则 $X,Y$ 线性关系越强
    - 若 $\rho_{XY} = 1$ 称正相关
    - 若 $\rho_{XY} = -1$ 称负相关
2. $|\rho_{XY}|$ 越接近 $0$，则 $X,Y$ 线性关系越弱
    - 若 $\rho_{XY} = 0$，称 $X,Y$ 不相关


!!! tip
    $X,Y$  相互独立 $\Rightarrow$ $X,Y$ 不相关


#### 总结

1. $X,Y$ 不相关 $\Leftrightarrow$ $\rho_{XY}$ $\Leftrightarrow$ $\mathrm{Cov}(X,Y)$ $\Leftrightarrow$ $EXY = EXEY$ $\Leftrightarrow$ $D(X+Y) = DX + DY$
2. 当 $X,Y$ 服从二维正态分布时，$X,Y$ 不相关（$\rho_{XY} = 0$）$\Leftrightarrow$ $X,Y$ 相互独立

### 矩，协方差矩阵

#### 矩

1. $EX^k$ ——— $k$ 阶原点矩
2. $E(X-EX)^k$ ——— $k$ 阶中心矩
3. $EX^kY^l$ ——— $k+l$ 阶混合原点矩
4. $E(E-EX)^k(Y-EY)^l$ ——— $k+l$ 阶混合中心矩

#### 协方差矩阵

设 $n$  维随机变量 $(X_1,X_2\cdots X_n)$ 的二阶混合中心矩 $C_{ij} = \mathrm{Cov}(X_i,X_j) (i,j = 1,2\cdots)$ 都有效，则称矩阵

$$
C = \begin{pmatrix}
C_{11} & C_{12} & \cdots & C_{1n}\\
C_{21} & C_{22} & \cdots & C_{2n}\\
\vdots & \vdots &        & \vdots\\
C_{n1} & C_{n2} & \cdots & C_{nn}
\end{pmatrix}
$$

为随机变量 $(X_1,X_2\cdots X_n)$ 的协方差矩阵