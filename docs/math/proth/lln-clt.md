---
stas: true
comment: True
---

# 大数定律及中心极限定理

## 大数定律

### 切比雪夫不等式

设随机变量 $X$ 有 $EX = \mu,DX=\sigma^2$，则 $\forall \varepsilon > 0$ 有

$$
\begin{align*}
P\{|x-\mu|\ge\varepsilon\} \le \frac{\sigma^2}{\varepsilon}\\
P\{|x-\mu|<\varepsilon\} \ge \frac{\sigma^2}{\varepsilon}
\end{align*}
$$

!!! tip
    当知道 $X$ 的 $EX$ 和 $DX$ 时，可以计算 $X$ 留在以 $EX$ 为中心的某一区间的概率（至少为下限）


### 大数定律

#### 切比雪夫大数定律

- 设随机变量序列 $X_1,X_2\cdots X_n \cdots$ 相互独立，分别具有均值 $EX_1,EX_2\cdots$ 及方差 $DX_1,DX_2\cdots$，若存在常数 $C$ 使得 $DX_i \le C (i=1,2\cdots)$，则 $\forall \varepsilon > 0$

$$
\lim_{n \to \infin} P\{|\frac{1}{n}\sum_{i=1}^{n}X_i - \frac{1}{n}\sum_{i=1}^{n}EX_i|<\varepsilon\} = 1
$$

!!! tip
    推论：设随机变量序列 $X_1,X_2\cdots X_n \cdots$ 相互独立，有相同的期望与方差 $EX_i = \mu,DX_i = \sigma^2 (i=1,2\cdots)$，则 $\forall \varepsilon >0$

    $$
    \lim_{n \to \infin} P\{|\frac{1}{n}\sum_{i=1}^{n}X_i - \mu| < \varepsilon\} = 1, \overline{X} \xrightarrow{P} \mu
    $$

- 依概率收敛：$Y_1,Y_2\cdots Y_n\cdots$ 是一个随机变量序列，$a$ 为常数 ，若 $\forall \varepsilon > 0,\lim_{n \to \infin}P\{|Y_n -a|<\varepsilon\}=1$，则称随机变量序列 $\{Y_n\}$ 依概率收敛于 $a$，记 $Y_n \xrightarrow{P} a$

!!! tip
    定理：设 $\{X_n\},\{Y_n\}$ 均为随机变量序列，$a,b$ 为常数，若 $X_n \xrightarrow{P} a,Y_n \xrightarrow{P} b$，且函数 $g(X_n,Y_n)$ 在点 $(a,b)$ 连续，则 $g(X_n,Y_n) \xrightarrow{P} g(a,b)$

#### 伯努利大数定律

设在 $n$ 重伯努利试验中，事件 $A$ 发生的概率为 $p$，$A$ 发生的次数为 $n(A)$，则 $\varepsilon > 0$

$$
\lim_{n\to \infin} P\{|\frac{n(A)}{n}-p| < \varepsilon\} = 1
$$

#### 辛钦大数定律

设 $X_1,X_2 \cdots X_n \cdots$ 为独立同分布的随机变量序列，且具有期望 $E(X_k) = \mu(k=1,2\cdots)$，对 $\forall \varepsilon > 0$ 

$$
\lim_{n \to \infin} P\{|\frac{1}{n}\sum_{i=1}^{n}X_i - \mu|<\varepsilon\} = 1
$$

## 中心极限定理

### 林德伯格 —— 列维中心极限定理

设随机变量序列 $X_1,X_2 \cdots X_n \cdots$ 独立同分布，$EX_i = \mu,DX_i = \sigma^2 > 0 (i=1,2\cdots)$，则随机变量之和 $\sum_{k=1}^{n} X_k$ 的标准化变量

$$
Y_n = \frac{\sum_{k=1}^{n}X_k - n\mu}{\sqrt{n}\sigma}
$$

的分布函数 $F_n(x)$ 对 $\forall x \in \mathbb{R}$

$$
\lim_{n\to \infin} F_n(x) = \lim_{n \to \infin} P\{\frac{\sum_{k=1}^{n}X_k - n\mu}{\sqrt{n}\sigma} \le x\} = \int_{-\infin}^{x} \frac{1}{\sqrt{2\pi}}e^{-\frac{t^2}{2}} \mathrm{d}t = \Phi(x)
$$

即 $n \to \infin$ 时

$$
Y_n = \frac{\sum_{i=1}^{n}X_i - n\mu}{\sqrt{n}\sigma} 
$$

近似 $N(0,1)$

!!! tip
    总结：随机变量序列 $X_1,X_2 \cdots X_n \cdots$ 独立同分布，$EX = \mu,DX=\sigma^2 \neq 0 (i=1,2\cdots)$，当 $n \to \infin$ 时

    - $\sum_{i=1}^{n} X_i \sim N(n\mu,n\sigma^2)$
    - $\frac{\sum_{i=1}^{n}X_i - n\mu}{\sqrt{n}\sigma} \sim N(0,1)$
    - $\frac{1}{n}\sum_{i=1}^{n} X_i \sim N(\mu,\frac{\sigma^2}{n})$


### 李雅普诺夫定理

设随机变量序列 $X_1,X_2 \cdots X_n \cdots$ 相互独立，$EX_k = \mu_k,DX_k = \sigma_k^2 > 0 (k=1,2\cdots)$，记 $B_k^2 = \sum_{k=1}^{n} \sigma_k^2$，若存在 $\delta > 0$，使得当 $n \to \infin$ 时

$$
\frac{1}{B_n^{2+\delta}} \sum_{k=1}^{n} E\{|X_k - \mu_k|^{2+\delta}\} \to 0
$$

则随机变量之和 $\sum_{k=1}^{n} X_k$ 的标准化变量

$$
Z_n = \frac{\sum_{k=1}^nX_k - E(\sum_{k=1}^{n}X_k)}{\sqrt{D(\sum_{k=1}^{n}X_k)}} = \frac{\sum_{k=1}^nX_k - \sum_{k=1}^{n}\mu_k}{B_n}
$$

的分布函数 $F_n(x)$ 对 $\forall x \in \mathbb{R}$

$$
\lim_{n \to \infin} F_n(x) = \lim_{n \to \infin} P\{\frac{\sum_{k=1}^nX_k - \sum_{k=1}^{n}\mu_k}{B_n}\le x\} = \int_{-\infin}^{x} \frac{1}{\sqrt{2\pi}}e^{-\frac{t^2}{2}} \mathrm{d}t = \Phi(x)
$$

### 棣莫弗 —— 拉普拉斯定理

设随机变量 $Z_n$ 服从二项分布 $B_n (n,p)(0<p<1)$，则 $\forall x \in \mathbb{R}$

$$
\lim_{n \to \infin} = P\{\frac{\eta_n - np}{\sqrt{np(1-p)}}\le x\} = \int_{-\infin}^{x} \frac{1}{\sqrt{2\pi}}e^{-\frac{t^2}{2}} \mathrm{d}t = \Phi(x)
$$

即：当 $n \to \infin$

$$
\begin{align*}
\frac{Z_n-np}{\sqrt{np(1-p)}} &\sim N(0,1) \\
Z_n &\sim N(np,np(1-p))
\end{align*}
$$

!!! tip
    二项分布
    
    - 以泊松分布为近似
        - 优点： $n \ge 20$
        - 缺点：$p \le 0.05$
    - 以正态分布为近似
        - 优点：$p$ 无限制
        - 缺点：$n \ge 50$
