---
stas: true
comment: True
---

# 多维随机变量及其分布

## 二维随机变量

### 二维随机变量

#### 定义

设有随机变量 $E$，样本空间为 $S$，对 $\forall e \in S$，有 $X=X(e),Y=Y(e)$ 为定义上 $S$ 上的随机变量，由 $X,Y$ 构成的一个向量 $(X,Y)$ 称为二维随机变量

#### 分布函数

- 定义：假设 $(X,Y)$ 为二维随机变量，对 $\forall x,y \in R$，有二元函数 $F(x,y) = P\{(X\le x)\cap (Y \le y)\} = P\{X \le x,Y\le y\}$ 称为 $(X,Y)$ 的分布函数，或称 $X$ 和 $Y$ 的联合分布函数

!!! tip
    $$
    P\{x_1 < X \le x_2,y_1 < Y \le y_2\} = F(x_2,y_2) - F(x_2,y_1) + F(x_1,y_1) - F(x_1,y_2)
    $$

- 性质
    1. $F(x,y)$ 对于 $x$  或 $y$ 都是不减的
        1. $\forall x_2 > x_1,y = y_0 ,F(x_2,y_0) \ge F(x_1,y_0)$
        2. $\forall y_2 > y_1,x = x_0 ,F(x_0,y_2) \ge F(x_0,y_1)$
    2. $0 \le F(x,y) \le 1$
        1. $F(-\infin,y_0) = 0$
        2. $F(x_0,-\infin) = 0$
        3. $F(-\infin,\infin) = 0$
        4. $F(+\infin,+\infin) = 1$
    3. $F(x,y)$ 对 $x$ 或 $y$ 均是右连续的
        1. $F(x+0,y) = F(x,y)$
        2. $F(x,y+0) = F(x,y)$
    4. 对于任意 $(x_1,y_1),(x_2,y_2),x_1<x_2,y_1<y_2$，有不等式成立
    
    $$
    F(x_2,y_2) - F(x_2,y_1) + F(x_1,y_1) - F(x_1,y_2) \ge 0
    $$
    

### 二维离散型随机变量

#### 定义

若二维随机变量 $(X,Y)$ 的取值为有限个或可列个，记为 $(x_i,y_i)$，则称 $(X,Y)$ 为二维离散随机变量并称 $P\{X=x_i,Y=y_i\} = p_{ij}$ 为 $(X,Y)$ 的分布律或 $X,Y$ 的联合分布律 


\[
\begin{array}{c|c|c|c|c|c}
Y | X & x_1 & x_2 & \cdots & x_i & \cdots \\
\hline
y_1 & p_{11} & p_{21} & \cdots & p_{i1} & \cdots \\
y_2 & p_{12} & p_{22} & \cdots & p_{i2} & \cdots \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
y_i & p_{1j} & p_{2j} & \cdots & p_{ij} & \cdots \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
\end{array}
\]


#### 性质

1. $p_{ij} \ge 0$
2. $\sum_{i=1}^{\infin}\sum_{j=1}^{\infin} p_{ij} =1$
3. 分布函数 $F(x,y) = \sum_{x_i\le x}\sum_{y_j\le y} p_{ij}$

### 二维连续型随机变量

#### 定义

若对 $(X,Y)$ 存在非负可积函数 $f(x,y)$ 使得对于 $x,y$ 有

$$
F(x,y) = \int_{-\infin}^{y}\int_{-\infin}^{x} f(u,v) \mathrm{d}u\mathrm{d}v
$$

则称 $(X,Y)$ 为连续型随机变量，$F(x,y)$ 和 $f(x,y)$ 分别为 $(X,Y)$ 的分布函数和概率密度函数

#### 性质

1. $f(x,y) \ge 0$
2. $\int_{-\infin}^{+\infin}\int_{-\infin}^{+\infin} f(x,y) \mathrm{d}x\mathrm{d}y = F(+\infin,+\infin) = 1$
3. $P((X,Y) \in G) = \iint_{G} f(x,y) \mathrm{d}x\mathrm{d}y$
4. 若 $f(x,y)$ 在点 $(x,y)$ 连续，有

$$
\frac{\partial^2 F(x,y)}{\partial x\partial y} = f(x,y)
$$

!!! tip
    1. 在空间直角坐标系中，$f(x,y)$ 的图像在 $xOy$ 平面上方
    2. $xOy$ 平面与曲面 $Z = f(x,y)$ 之间的广义曲顶柱体体积为 $1$
    3. $P\{(x,y)\in G\}$ 相当于以 $G$ 为底，$Z = f(x,y)$ 为顶的曲顶柱体的体积
    4. $f(x,y)$ 刻画了 $(X,Y)$ 取值在 $f(x,y)$ 连续为 $(x,y)$ 附近的概率大小
    5. $(X,Y)$ 取值在任何一条直线上均为 $0$


### 常见连续型随机变量的分布

#### 均匀分布

- 定义：设 $xOy$ 平面上一有界区域 $G$，面积为 $A$，若二维随机变量的概率密度为

$$
f(x,y) = \left\{
\begin{array}{l}
\frac{1}{A},(x,y)\in G \\
0,\quad \text{otherwise} 
\end{array}
\right.
$$

则称 $(X,Y)$ 服从区域 $G$ 的均匀分布

!!! tip
    - 本质含义：$(X,Y)$ 取值在 $G$ 的任意小区域的概率与小区域的面积成正比，与小区域的位置及形状无关
    - 背景：平面上的几何概型


#### 二维正态分布

- 定义：设二维随机变量 $(X, Y)$ 有概率密度函数为

$$
f(x, y) = \frac{1}{2 \pi \sigma_1 \sigma_2 \sqrt{1 - \rho^2}} \exp \left\{ -\frac{1}{2(1 - \rho^2)} \left( \frac{(x - \mu_1)^2}{\sigma_1^2} + \frac{(y - \mu_2)^2}{\sigma_2^2} - \frac{2 \rho (x - \mu_1)(y - \mu_2)}{\sigma_1 \sigma_2} \right) \right\}
$$

其中 $\mu_1,\mu_2,\sigma_1,\sigma_2,\rho$ 均为常数，且 $\sigma_1>0,\sigma_2>0,-1<\rho<1$，我们的 $(X,Y)$ 为服从参数为 $\mu_1,\mu_2,\sigma_1,\sigma_2,\rho$ 的二维正态分布，记为 $(X,Y) \sim N(\mu_1,\mu_2,\sigma_1^2,\sigma_2^2,\rho)$

## 边缘分布

### 边缘分布函数

#### 定义

设 $(X,Y)$ 为二维随机变量，称 $F_X(x) = P\{X\le x,y<+\infin\} = F(x,+\infin) = \lim_{y\to +\infin} F(x,y)$ 为随机变量 $X$  的边缘分布函数. 随机变量 $Y$ 的边缘分布函数同理.

### 离散型随机变量的边缘分布律

#### 定理

设 $(X,Y)$ 为离散型随机变量，其分布律为 $P\{X=x_i,Y=y_i\} \stackrel{\wedge}{=} p_{ij} (i,j=1,2,\cdots)$，则关于 $X$ 和关于 $Y$ 的边缘分布律分别为

$$
\begin{array}{l}
P\{X = x_i\} = \sum_{j=1}^{\infin} p_{ij} = p_{i\cdot} \\
P\{Y = y_j\} = \sum_{i=1}^{\infin} p_{ij} = p_{\cdot j}
\end{array}
$$

### 连续型随机变量的边缘分布

#### 定理

设 $(X,Y)$ 为连续型随机变量，其概率密度函数为 $f(x,y)$，则 $X,Y$ 均为连续型随机变量，则关于 $X$ 和关于 $Y$ 的边缘概率密度分别为

$$
\begin{array}{l}
f_X(x) = \int_{-\infin}^{+\infin} f(x,y) \mathrm{d}y \\
f_Y(y) = \int_{-\infin}^{+\infin} f(x,y) \mathrm{d}x
\end{array}
$$

!!! tip
    - $F_X(x) = F(x,+\infin)$
    - $F_{Y}(y) = F(+\infin,y)$


## 条件分布

$$
P\{Y=y_i\} > 0 \\P\{X\le x|Y = y_i\} = F(x|Y = y_i)
$$

### 二维离散型随机变量的条件分布律

#### 定义

设 $(X,Y)$ 为离散型随机变量，其分布律为 $P\{X=x_i,Y=y_i\} = p_{ij} (i,j=1,2,\cdots)$.

- 对固定的 $j$，若 $P\{Y=y_j\} > 0$，则称 $P\{X=x_i|Y = y_j\} = \frac{P\{X=x_i,Y=y_j\}}{P\{Y = y_j\}} = \frac{p_{ij}}{p_{\cdot j}} (i=1,2,\cdots)$ 为 $X$ 在 $Y=y_j$ 条件下的条件分布律
- 对固定的 $i$，若 $P\{X=x_i\} > 0$，则称 $P\{Y=y_j|X = x_i\} = \frac{P\{X=x_i,Y=y_j\}}{P\{X = x_i\}} = \frac{p_{ij}}{p_{i\cdot}} (j=1,2,\cdots)$ 为 $Y$ 在 $X=x_i$ 条件下的条件分布律

!!! tip
    1. 条件分布的本质就是条件概率，离散型随机变量 $X$ 在 $Y = y_j$ 条件下的条件分布律就是将 $X$ 取每个值的事件 $X = x_i$ 在 $Y = y_j$ 发生条件下的条件概率列出来
    2. 条件分布律的计算即条件概率的计算
    3. 满足分布律的充要条件
        - $P\{X = x_i | Y= y_j\} = \frac{p_{ij}}{p_{\cdot j}} \ge 0$
        - $\sum_{i=1}^{\infin} P\{X = x_i | Y= y_j\} = \sum_{i=1}^{\infin} \frac{p_{ij}}{p_{\cdot j}} = 1$


### 二维连续型随机变量的条件概率密度

#### 定义

- 给定 $y$， $\forall \varepsilon > 0$，设 $P\{y < Y \le y + \varepsilon\} > 0$，则有

$$
\begin{align*}
P\{X \le x \mid y < Y \le y + \varepsilon \} 
&= \frac{P\{X \le x, y < Y \le y + \varepsilon\}}{P\{y < Y \le y + \varepsilon\}} \\
&= \frac{\int_{-\infin}^{x}[\int_{y}^{y+\varepsilon}f(x,y)\mathrm{d}y]\mathrm{d}x}{\int_{y}^{y+\varepsilon}f_Y(y)\mathrm{d}y}\\
&\approx \frac{\int_{-\infin}^{x}\varepsilon f(x,y)\mathrm{d}x}{\varepsilon f_Y(y)} = \int_{-\infin}^{x}  \frac{f(x,y)}{f_Y(y)} \mathrm{d}x
\end{align*}
$$

- 称 $F_{X|Y}(x|y) = \int_{-\infin}^{x}  \frac{f(x,y)}{f_Y(y)} \mathrm{d}x$
 为随机变量 $X$ 在条件 $Y = y$ 下的条件分布函数
- 称 $f_{X|Y}(x|y)= \frac{f(x,y)}{f_Y(y)}$ 为随机变量 $X$ 在条件 $Y = y$ 下的条件概率密度

#### 条件概率密度性质

1. $f_{X|Y}(x|y) \ge 0$
2. $\int_{-\infin}^{x}  f_{X|Y}(x|y) \mathrm{d}x = 1$

## 相互独立的随机变量

### 定义

设二维随机变量的联合分布函数为 $F(x,y)$，边缘分布函数为 $F(x),F(y)$，若对所有 $x,y$，有 $F(x,y) = F_X(x)\cdot F_Y(y)$，则称 $X$ 和 $Y$ 是相互独立的

!!! tip
    1. 对于离散型随机变量 $(X,Y)$，有 $X$ 与 $Y$ 相互独立 $\Leftrightarrow P\{X = x_i| Y = y_j\} = P\{X=x_i\}P\{Y=y_j\}$，即 $p_{ij} = p_{i\cdot}\cdot p_{\cdot j}$
    2. 对于连续型随机变量 $(X,Y)$，有 $X$ 与 $Y$ 相互独立 $\Leftrightarrow f(x,y) = f_X(x)\cdot f_Y(y)$
    3. 对于二维正态分布的 $(X,Y)$，有 $X$ 与 $Y$ 相互独立 $\Leftrightarrow \rho = 0$
    4. 若 $X,Y$ 相互独立，则 $f(X)$ 与 $g(Y)$ 也相互独立


## 两个随机变量的函数的分布

### 离散型随机变量函数的分布

#### 结论

- 若二维离散型随机变量 $(X,Y)$ 的分布律为 $P\{X=x_i,Y=y_j\} = p_{ij} (i,j=1,2,\cdots)$，则随机变量 $(X,Y)$ 的函数 $Z=g(X,Y)$ 的分布律为

$$
P\{Z = Z_k\} = P\{g(X,Y)=Z_k\} = \sum_{Z_k = g(x_i,y_j)} p_{ij} (i,j=1,2,\cdots)
$$

- 若 $X \sim P(\lambda_1),Y\sim P(\lambda_2)$ 且 $X,Y$ 相互独立  $\Rightarrow X + Y \sim P(\lambda_1+\lambda_2)$
    - 推广：若 $X_1 \sim P(\lambda_1),X_2\sim P(\lambda_2),\cdots,X_n\sim P(\lambda_n)$ 且 $X_1,X_2,\cdots,X_n$ 相互独立 $\Rightarrow X_1 + X_2 + \cdots + X_n \sim P(\lambda_1+\lambda_2+\cdots+\lambda_n)$
    - 证明：可知 $P\{X=i\} = \frac{\lambda_1^ie^{-\lambda_1}}{i!},P\{Y = j\} = \frac{\lambda_2^je^{-\lambda_2}}{j!}$，则

$$
\begin{align*}
P\{Z=k\} &= P\{X+Y=k\} = \sum_{i=1}^k P\{X=i,Y=k-i\} = \sum_{i=1}^k P\{X=i\}P\{Y=k-i\}\\
&= \sum_{i=1}^k \frac{\lambda_1^ie^{-\lambda_1}}{i!} \cdot\frac{\lambda_2^{k-i}e^{-\lambda_2}}{(k-i)!} = \frac{e^{-(\lambda_1+\lambda_2)}}{k!} \sum_{i=1}^k \frac{\lambda_1^i\lambda_2^{k-i}k!}{i!(k-i)!} = \frac{e^{-(\lambda_1+\lambda_2)}}{k!} \sum_{i=1}^k \binom{k}{i} \lambda_1^{i} \cdot \lambda_2^{k-i} \\ &= \frac{(\lambda_1+\lambda_2)^ke^{-(\lambda_1+\lambda_2)}}{k!}
\end{align*}
$$

- 若 $X \sim B(n_1,p),Y\sim B(n_2,p)$ 且 $X,Y$ 相互独立  $\Rightarrow X + Y \sim P(n_1+n_2)$
    - 推广：若 $X_1 \sim B(n_1,p),X_2\sim P(n_2,p),\cdots,X_n\sim B(n_k,p)$ 且 $X_1,X_2,\cdots,X_k$ 相互独立 $\Rightarrow X_1 + X_2 + \cdots + X_k \sim B(n_1+n_2+\cdots+n_k,p)$
    - 特别的，当 $n_1=n_2=\cdots=n_k=1$，即 $X_i \sim B(1,p)$ 时，$X_1,X_2,\cdots,X_k$ 独立同分布服从 $B(1,p)$，则 $\sum_{i=1}^{k} X_i \sim B(n,p)$，即服从 $B(k,p)$ 的随机变量可作为 $k$ 个 $0-1$ 分布随机变量的和
    - 证明：可知 $P\{X=i\} = \binom{n_1}{i}p^iq^{n_1-i}(i=1,2,\cdots),P\{Y = j\} = \binom{n_2}{j}p^jq^{n_2-j}(j=1,2,\cdots)$，则

$$
\begin{align*}
P\{Z=k\} &= P\{X+Y=k\} = \sum_{i=1}^k P\{X=i,Y=k-i\} = \sum_{i=1}^k P\{X=i\}P\{Y=k-i\}\\
&= \sum_{i=0}^{k}\binom{n_1}{i}p^iq^{n_1-i} \binom{n_2}{k-i}p^{k-i}q^{n_2-k+i} = \sum_{i=0}^{k} \binom{n_1}{i}\binom{n_2}{k-i} p^kq^{n_1+n_2-k}\\
&= \binom{n_1+n_2}{k} p^kq^{n_1+n_2-k}
\end{align*}
$$

### 连续型随机变量函数的分布

- $Z = X +Y$ 的分布

设 $(X,Y)$ 的概率密度为 $f(x,y)$，则 $Z = X+Y$ 的概率分布函数为

$$
\begin{align*}
F_Z(z) &= P\{Z \le z\} = P\{X+Y \le z\} = \iint_{X+Y\le Z} f(x,y) \mathrm{d}x\mathrm{d}y\\
&= \int_{-\infin}^{+\infin}(\int_{-\infin}^{z-y}f(x,y)\mathrm{d}x)\mathrm{d}y \stackrel{u=x+y}{=} \int_{-\infin}^{+\infin}(\int_{-\infin}^{z}f(u-y,y)\mathrm{d}u)\mathrm{d}y\\ 
&= \int_{-\infin}^{z}(\int_{-\infin}^{+\infin}f(u-y,y)\mathrm{d}y)\mathrm{d}u
\end{align*}
$$

固 $f_Z(z) = \int_{-\infin}^{+\infin}f(z-y,y)\mathrm{d}y = \int_{-\infin}^{+\infin} f(x,z-x)\mathrm{d}x$. 若 $X,Y$ 相互独立时，$f(x,y) = f_X(x)f_Y(y)$，则

$$
\begin{align*}
f_Z(z) &= \int_{-\infin}^{+\infin}f(z-y,y)\mathrm{d}y = \int_{-\infin}^{+\infin}f_X(z-y)f_Y(y)\mathrm{d}y \\&= \int_{-\infin}^{+\infin} f(x,z-x)\mathrm{d}x  = \int_{-\infin}^{+\infin}f_X(x)f_Y(z-x)\mathrm{d}x
\end{align*}
$$

- 设 $M = max\{X,Y\}$，$N = min\{X,Y\}$，$X,Y$ 相互独立，则

$$
\begin{align*}
F_{max}(z) &= P\{M \le z\} = P\{X\le z,Y \le z\} = F_X(z)F_Y(z)\\
F_{min}(z) &= P\{N \le z\} = 1 - P\{N > z\} = 1 - P\{X > z,Y>z\}\\
&= 1 - P\{X>z\}P\{Y > z\} = 1 - (1-P\{X\le z\})(1-P\{Y \le z\}) \\
&= F_X(z) + F_Y(z) - F_X(z)F_Y(z)
\end{align*}
$$

!!! tip
    推广：设 $X_1,X_2,\cdots,X_n$ 为 $n$ 个相互独立的随机变量，它们的分布函数为 $F_{X_i}(x_i)(i=\overline{1,n})$ 则 $M = max\{X_1,X_2,\cdots,X_n\},N=min\{X_1,X_2,\cdots,X_n\}$,则

    $$
    \begin{align*}
    F_{max}(z) &=  F_{X_1}(z)F_{X_2}(z)\cdots F_{X_n}(z)\\
    F_{min}(z) &= 1 - (1-F_{X_1}(z))(1-F_{X_2}(z))\cdots(1-F_{X_m}(z))
    \end{align*}
    $$

    若 $X_1,X_2,\cdots ,X_n$ 独立同分布，还可得

    $$
    \begin{align*}
    F_{max}(z) &=  F_{X}^n(z) \\
    F_{min}(z) &= 1 - (1-F_{X}(z))^n
    \end{align*}
    $$