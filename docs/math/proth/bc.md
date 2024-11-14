---
stas: true
comment: True
---

# 基本概念

## 引入

- 确定性现象(必然现象)
    - 在一定条件下，事情没发生前就清楚结果
    - 特征：条件完全决定结果
- 不确定性现象(随机现象)
    - 具有多种可能结果，但事先不能确定哪一种
    - 特征：条件无法完全决定结果

### 随机试验

定义：如果对随机现象的试验具有以下三个特点

1. 可以在相同条件下重复进行
2. 试验可能结果不唯一，并且事先明确试验的所有可能结果
3. 试验前不能知道哪种结果会出现

则称这种试验为随机试验，记为 $E$

## 样本空间 随机事件

### 样本空间

定义：

- 随机试验的 $E$ 的所有可能结果组成的集合称为 $E$ 的样本空间，记为 $S$
- 样本空间的元素，称为样本点，记为 $Q$

!!! tip
    1. 试验不同，样本空间一般不同
    2. 同一试验若目的不同，样本空间也不一定相同


### 随机事件

定义：样本空间 $S$ 点子集称为试验 $E$ 的随机事件，简称事件。通常使用大写字母表示

### 事件分类

1. 基本事件：只含一个样本点的单点集
2. 复合事件：由多个基本事件复合而成的集合
3. 必然事件：在每次试验中一定发生的事件，即样本空间 $S$
4. 不可能事件：在每次试验中都不发生的事件，即 $\varnothing$

### 事件的关系与运算

1. 包含：记作 $A \subset B$， $A$ 发生必定使 $B$ 发生
2. 相等：记作 $A = B$， 即 $(A\subset B)\cap(B\subset A)$
3. 和事件
    1. $A \cup B := \{x|(x\in A)\vee(x\in B)\}$ ，即 $A$ 与 $B$ 至少有一个发生
    2. 有限： $\bigcup_{i=1}^n A_i = A_1 \cup A_2 \cup \cdots \cup A_n$ 
    3. 可列： $\bigcup_{i=1}^{\infin} A_i = A_1 \cup A_2 \cup \cdots$
4. 积事件
    1. $A \cap B := \{x|(x\in A)\wedge(x \in B)\}$ ， 即 $A$ 与 $B$ 同时发生，可记作 $A \cdot B$ 或 $AB$
    2. 有限： $\bigcap_{i=1}^n A_i = A_1 \cap A_2 \cap \cdots \cap A_n$ 
    3. 可列： $\bigcap_{i=1}^{\infin} A_i = A_1 \cap A_2 \cap \cdots$
5. 差事件
    1. $A - B = \{x|(x\in A) \wedge (x \notin B)\}$
    2. 差补转化： $A-B = A \cap \overline{B}$
6. 互斥
    1. $A \cap B = \varnothing$
    2. 两两互斥： $\forall i \neq j (A_i \cap A_j = \varnothing) (i,j = 1,2,\cdots)$
7. 逆事件
    1. $A \cup B = S \wedge (A\cap B) = \varnothing$，记作 $\overline{A}$
    2. $\overline{A} = S - A$

## 频率与概率

### 频率

#### 定义

在相同条件下，进行了 $n$ 次试验，在这 $n$ 次试验中，事件 $A$ 发生的次数 $n_A$ 称为事件 $A$ 发生的频数，比值 $n_A / n$ 称为 $A$ 发生的频率，并记成 $f_n(A)$

!!! tip
    频率描述了事件的频繁程度


#### 性质

1. $0 \le f_n(A) \le 1$
2. $f_n(S) = 1$
3. 对 $k$ 个两两互不相容事件 $A_1,A_2,\cdots,A_k$ 有 $f_n(A_1\cup A_2\cup \cdots \cup A_k) = f_n(A_1) + f_n(A_2) + \cdots + f_n(A_k)$

!!! tip
    1. 频率在一定程度上反映了事件 $A$ 发生的可能性大小，但在一定事件下做多次重复试验，其结果是不一样的，因此不能用频率代替概率，但由大数定律得到频率总能稳定在某个固定数 $P(A)$ 周围，即 $f_n(A) \xrightarrow{n \rightarrow \infin} P(A)$
    2. 不能将概率作为频率的极限

### 概率

$A$ 的概率记为  $P(A)$，描述 $A$ 在一次试验中发生可能性的大小的数

#### 统计学定义

当 $n \rightarrow \infin$ 时， $f_n(A) = \frac{n_A}{n}$ 趋于稳定值 $P(A)$，称 $P(A)$ 为 $A$ 的概率

#### 公理化定义

对于 $E$ 的每一个事件 $A$ 赋一个实数值 $P(A)$ 满足：

1. 非负性： 对任一事件 $A$， $P(A) \ge 0$
2. 规范性： $P(S) =1$ 
3. 可列可加性：设 $A_1,A_2,\cdots$ 是两两互不相容的事件，即对于 $\forall A_iA_j = \varnothing (i\neq j),P(A_1 \cup A_2 \cup \cdots) = P(A_1) + P(A_2) + \cdots$

则称 $P(A)$  为 A 的概率

#### 性质

1. $P(\varnothing) = 0$
2. (有限可加性) 若 $A_1,A_2\cdots A_n$ 为两两互不相容的事件，则有

$$
P(\bigcup_{i=1}^{n}A_i) = \sum_{i=1}^{n}P(A_i)
$$

1. 若 $A \subset B$，则 $P(B-A) = P(B) - P(A)$  且 $P(B) \ge P(A)$。而一般情况下， $P(B-A) = P(B) - P(A\cap B)$
2. $P(A) \le 1$
3. $P(\overline{A}) = 1 - P(A)$
4. (加法公式) $P(A\cup B) = P(A) + P(B) - P(AB)$
    1. $P(A_1\cup A_2 \cup A_3) = P(A_1) + P(A_2) + P(A_3) - P(A_1A_2) - P(A_1A_3) - P(A_2A_3) + P(A_1A_2A_3)$
    2. $P(\bigcup_{i=1}^{n}A_i) = \sum_{i=1}^{n}P(A_i) - \sum_{1\le i < j \le n}P(A_iA_j) + \sum_{1\le i < j < k \le n}P(A_iA_jA_k) + \cdots + (-1)^{n-1} P(A_1A_2\cdots A_n)$

## 古典概型

### 古典概型

定义：具有以下特点的试验称为古典概型

1. 样本空间只包含有限个元素
2. 每个基本事件发生的可能性相同

即：设 $S = \{e_1,e_2\cdots e_n\}$ 有 $P(\{e_1\}) = P(\{e_2\}) = \cdots = P(\{e_n\}) = \frac{1}{n}$

### 概率计算

假设事件包含 $k$ 个样本点， $A = \{e_{i_1}\} \cup \{e_{i_2}\} \cup \cdots \cup \{e_{i_k}\}$,则 $P(A) = \frac{k}{n}$

### 摸球问题

将 $n$ 个球放入 $N(N\ge n)$  个盒子中

- $A = \{指定 n 个 盒子中各有一球\},P(A) = \frac{A_n^n}{N^n}$
- $B=\{某一指定盒子中有一球\},P(B)=1-\frac{(N-1)^n}{N^n}$
- $C = \{某一指定盒子中有 k 个球\}，P(C)=\frac{C_n^k\cdot(N-1)^{n-k}}{N_n}$
- $D=\{每盒至多一球\},P(D)=\frac{A_N^n}{N^n}$

### 超几何概型

$N$ 件产品，其中 $D$ 件次品，从中任取 $n$ 件，设 $A$ 为恰有 $k$ 件次品，则

$$
P(A) = \frac{C_D^k\cdot C_{N-D}^{n-k}}{C_N^n}
$$

### 几何概型

定义：随机试验的样本空间为某个区域，随机实验为向区域 $D$ 投点，如果投中 $D$  的任意区域 $A$ 的可能性大小与子区域 $A$ 的度量 $S(A)$ 成正比，与 $A$ 的形状和位置无关，称为几何概型

$$
P(A) = \frac{S(A)}{S(n)}
$$

!!! tip
    古典概型与几何概型的异同

    古典概型：

    - 样本有限
    - 等可能， $P(\{e_i\}) = \frac{1}{n}$

    几何概型：

    - 样本点连续无限
    - 等可能， $P(\{e_i\}) = 0$

## 条件概率

### 定义

设 $A,B$ 为两个事件，且 $P(A) > 0$ ，称

$$
P(B|A) = \frac{P(AB)}{P(A)} = \frac{AB}{A}
$$

为 $A$  发生的条件下 $B$ 发生的条件概率

### 乘法定理

设 $P(A) > 0$ ，则

$$
P(AB) = P(B|A)P(A)
$$

一般的，

$$
P(A_1A_2\cdots A_n)=P(A_n|A_1A_2\cdots A_{n-1}) P(A_{n-1}|A_1A_2\cdots A_{n-2})\cdots P(A_1)
$$

### 样本空间的划分

设 $S$ 为试验 $E$ 的样本空间，$B_1,B_2,\cdots,B_n$ 为 $E$ 的一组事件，若

1. $B_iB_j \neq \varnothing(i\neq j)$
2. $B_1 \cup B_2 \cup \cdots \cup B_n =S$

则称 $B_1,B_2,\cdots,B_n$ 为样本空间的一个划分或完备事件组

### 全概率公式

$$
P(A) = \sum_{i=1}^n P(A|B_i)P(B_i)
$$

### 贝叶斯公式

$$
P(B_i | A) = \frac{P(AB_i)}{P(A)} = \frac{P(B_i)P(A|B_i)}{\sum_{i=1}^{n}P(B_i)P(A|B_i)}
$$

## 独立性

### 定义

设 $A,B$ 是两事件，如果满足

- $P(AB) = P(A)P(B)$

则称事件 $A,B$ 相互独立，简称 $A,B$ 独立

!!! tip
    1. 若 $A$  与 $B$  独立，则 $\overline{A}$ 与 $B$， $A$ 与 $\overline{B}$， $\overline{A}$  与 $\overline{B}$ 相互独立
    2. 若 $P(A) > 0$，则 $A,B$ 独立 $\Leftrightarrow P(B|A) = P(B)$
    3. 若 $0 < P(A) < 1$，则 $A,B$ 独立 $\Leftrightarrow P(B|A) = P(B|\overline{A})$
    4. 若 $P(A)>0,P(B)>0$，则 $A,B$ 相互独立与 $A,B$ 互不相容不能同时成立
    5. 存在既独立又互斥的事件

### 多个事件的相互独立性

- $A,B,C$ 相互独立当且仅当

$$
\left\{
\begin{array}{l}
P(AB) = P(A)P(B) \\ 
P(AC) = P(A)P(C) \\ 
P(BC) = P(B)P(C) \\ 
P(ABC) = P(A)P(B)P(C)
\end{array}
\right.
$$

- 设 $A_1,A_2,\cdots,A_n$  为 $n$ 个事件，若等式

$$
\forall k \in \{2,3,\cdots,n\}\forall 1\le i_1 < i_2 < \cdots < i_k <n,P(A_{i_1}A_{i_2}\cdots A_{i_k}) = P(A_{i_1})\cdot P(A_{i_2})\cdots P(A_{i_k})
$$

均成立，则称 $A_1,A_2,\cdots,A_n$ 相互独立

### 推广

- 若 $n$ 个事件 $A_1,A_2,\cdots,A_n$ 相互独立，则其中任意 $k(2\le k \le n)$ 个事件也独立
- 若 $n$ 个事件 $A_1,A_2,\cdots,A_n$ 相互独立，则将其中任意多事件换成它们各自对应的对立事件，所得 $n$ 个事件仍独立

### 试验的独立性

- 两个试验 $E_1,E_2$ 相互独立，当且仅当 $E_1$ 中任一事件与 $E_2$ 中任一事件相互独立
- $n$ 个试验 $E_1,E_2,\cdots,E_n$ 相互独立，当且仅当 $E_1, E_2, \cdots, E_n$ 各任一事件之间相互独立，若 $n$ 个试验相同，则称为 $n$ 重独立重复试验