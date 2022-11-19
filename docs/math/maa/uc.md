# 通用概念

## 1. 逻辑符号

|符号|含义|解释|
|--|--|--|
|$\neg$|非|$\neg p$,表示$p$的否命题|
|$\wedge$|与|$p\wedge q$,表示$p$与$q$同时成立|
|$\vee$|或|$p \vee q$,表示$p$与$q$至少一个成立|
|$\Rightarrow$|蕴含|$p \Rightarrow q$,表示$p$为$q$的充分条件|
|$\Leftrightarrow$|等价|$p \Leftrightarrow q$,表示$p$等价于$q$|

## 2. 集合

### 2.1 性质
1. 集合可由任何有区别的对象组成
2. 集合由其组成对象整体唯一确定
3. 任何性质都确定一个具有该性质的对象的集合

### 2.2 表示
- $x$为一个对象，$P(x)$示$x$具有性质$P$,则用$\{x|P(x)\}$表示集合
- 用$\{x_1,x_2,...,x_n\}$表示集合
- 单元素集合$\{a\}$在不引起歧义时，可用$a$表示

### 2.3 包含关系
|符号|含义|
|--|:--:|
|$x \in X$|x属于X|
|$x \notin X$|x不属于X|
|$A = B$|A等于B.即$\forall x((x \in A) \Leftrightarrow(x \in B))$或$(A \subset B)\wedge(B \subset A)$|
|$A \subset B$|A包含于B.即$\forall x ((x \in A)\Rightarrow(x \in B))$|

注:空集可表示为 $\emptyset := \{x \in M|x \neq x\}$

### 2.4 集合运算
|运算|符号|含义|
|--|--|:--:|
|并集|$A \cup B$|$A \cup B := \{(x \in A)\vee (x \in B)\}$|
|交集|$A \cap B$|$A \cap B := \{(x \in A)\wedge (x \in B)\}$|
|差集|$A \backslash B$|$A \backslash B := \{(x \in A)\wedge (x \notin B)\}$|

### 2.5 笛卡尔积
集合$X \times Y := \{(x,y)|(x\in X)\wedge(y \in Y)\}$称为集合$X$，$Y$的笛卡尔积或直积，其中形如$(x,y)$的二元组称为序偶。$X \times X$简记为$X^2$。

设序偶$(x_1,x_2)$为集合$X_1$与$X_2$的直积$Z = X_1 \times X_2$的元素。$x_1$称为序偶$z$的第一投影$pr_1 z$,$x_2$称为序偶$z$的第二投影$pr_2 z$.同时称为序偶$z$的坐标

## 3. 函数

### 3.1 概念
如果集合$X$中每个元素$x$都按照某规律$f$与集合$Y$的元素$y$相对应，我们就说有一个函数，它定义于$X$并取值于$Y$。
其中$X$称为定义域，$x$的具体值$x_0$所对应的具体值$y_0$称为$x_0$上或$x=x_0$时的函数值。量$y=f(x)$称为自变量。

$$
f(X) := \{y \in Y|\exist x((x\in X)\wedge(y = f(x)))\}
$$

称为函数的值域

### 3.2 符号

1. $f:X \rightarrow Y,X \stackrel{f}{\rightarrow} Y,x\mapsto f(x),y=f(x)$ 函数$f$，定义于$X$并取值于$Y$
2. $f_1=f_2$ 函数相同或相等
3. $f|A，f|_A$ 函数$f$在集合A上的收缩，相反，$f$为函数$f|_A$在集合$X$上的延拓

### 3.3 映射的简单分类
当函数$f:X\rightarrow Y$称为映射时，它在$x \in X$上的值$f(x) \in Y$通常称为元素$x$的像。而集合$A \subset X$中各种像的集合

$$
f(A) := \{y\in Y|\exist x((x \in A)\wedge(y = f(x)))\}
$$

称为集合$A$的像。而集合$X$中以集合$B \subset Y$中各元素为像的元素的集合

$$
f^{-1}(B):=\{x \in X|f(x) \in B\}
$$

称为集合B的原像。

|分类|解释|
|--|--|
|满射|$f(X)=Y$，即值域等于到达域|
|单射|对于集合$X$中的任何元素$x_1,x_2$有$(f(x_1)=f(x_2))\Rightarrow (x_1=x_2)$|
|双射|既是满射也是双射|

如果存在映射$f:X\rightarrow Y$为双射，自然存在一个映射

$$
f^{-1} : Y \rightarrow X
$$

称为原映射$f$的逆映射。

### 3.4 函数的复合与互逆映射
如果在映射$f:X\to Y$与映射$g:Y\to Z$中，$g$定义于$f$的值域，就可以构造一个新的映射，称为映射$f$与$g$的复合映射

$$
g \circ f:X \to Z
$$

在集合X的元素上的值为

$$
(g \circ f)(x) := g(f(x))
$$

复合运算满足结合律，即:$h \circ (g \circ f) = (h \circ g) \circ f$

如果复合映射$f_1\circ f_2 \circ ... \circ f_n$中所有项都相同并等于$f$，则简记为$f^n$

即使$f \circ g$与$g \circ f$都有定义，一般也不相等，即不满足交换律:$g \circ f = f \circ g$

使集合$X$的每个元素与自身相对应的映射$f: X \to X$，即映射$x \stackrel{f}{\mapsto} x$,记作$e_X$并称为集合$X$的恒等映射。

#### 引理 3.4.1
$$
(g \circ f = e_X) \Rightarrow (g为满射)\wedge(f为单射)
$$

#### 命题 3.4.1
映射$f:X \to Y,g:Y\to X$当且仅当$g \circ f = e_X,f \circ g = e_Y$时，才为互逆的双射

### 3.5 作为关系的函数·函数的图像

#### 3.5.a 关系
序偶$(x,y)$的任何集合称为关系$R$。第一个元素$x$的集合$X$称为关系$\mathcal R$的定义域，第二个元素$y$的集合$Y$称为关系$\mathcal R$的值域。

常把$(x,y)\in \mathcal R$写作$x\mathcal Ry$,并$x$与$y$之间的关系为$\mathcal R$。

如果$\mathcal R \subset X^2$，就说在X上给定了关系$\mathcal R$。

偏序关系: 记为$a \preceq b$

性质：

1. $a \preceq a$ (自反性)
2. $(a \preceq b) \wedge (b \preceq c) \Rightarrow a \preceq c$ (传递性)
3. $(a \preceq b) \wedge (b \preceq a) \Rightarrow
a = b$ (反对称性)

序关系: 记为$a \le b$

性质：

1. 同偏序
2. 同偏序
3. 同偏序
4. $\forall a \forall b ((a\le b)\vee(b \le a))$

#### 3.5.b 函数与函数图像
满足$(xRy_1)\wedge(xRy_2) \Rightarrow (y_1=y_2)$的关系$R$称为函数关系，亦称函数。
对于按照最初描述来理解的函数$f:X \to Y$,由一切形如$(x,f(x))$的元素形成的集合$\Gamma$称为该函数的图像。

$$
\Gamma := \{(x,y)\in X \times Y|y = f(x)\}
$$

## 4. 补充

### 4.1 集合的势(基数类)
如果集合$X$到集合$Y$的双射存在，则称集合X与集合Y等势。
记为$X \sim Y$，称为等价关系。

集合$X$所在的类称为集合$X$的势或基数类，记为$card\ X$。如果$X \sim Y$,即可以写出$card\ X = card\ Y$。

如果集合$X$和集合$Y$的某个子集等式，我们就说集合$X$的基数类不大于集合$Y$的基数类，并记为$card\ X \le card\ Y$。于是:

$$
(card\ X \le card\ Y) := (\exist Z \subset Y|card\ X = card\ Y)
$$

如果集合$X \subset Y$,则显然$card\ X \le card\ Y$。然而，结果表明，关系$X \subset Y$并不影响$card\ Y \le card\ X$，即使$X$是$Y$的真子集也如此。

一个集合能够和自己的一部分等势，就称为无限集，否则为有限集。

性质:

1. $(card\ X \le card\ Y) \wedge (card\ Y \le card \ Z) \Rightarrow (card\ X \le card\ Z)$
2. $(card\ X \le card\ Y) \wedge (card\ Y \le card \ X) \Rightarrow (card\ X = card\ Y)$ (施罗德-伯恩斯坦定理)
3. $\forall X \forall Y(card\ X \le card\ Y) \vee (card\ Y \le card\ X)$ (康托尔定理)

可知基数类是线性有序的。

如果$card\ X \le card\ Y$，同时$card\ X \ne card\ Y$，就说集合$X$的势小于集合$Y$的势，并记为$card\ X < card\ Y$。于是，

$$
(card\ X < card\ Y) := (card\ X \le card\ Y) \wedge (card\ X \ne card\ Y )
$$

定理:

$$
card\ X  < card\ \mathcal{P}(X) \ (\mathcal{P}(X)表示集合X的一切子集的集合)
$$

### 4.2 公理化集合论

1. 外延公理. 集合$A$和集合$B$相等，当且仅当它们所具有的各元素是相同的。

$$
(A = B) \Leftrightarrow (\forall x (x \in A) \Leftrightarrow (x \in B))
$$

2. 分离公理. 任何集合$A$和性质$P$都对应一个集合B，其元素仅是$A$中具有性质$P$的各元素。

即:如果$A$是一个集合,则$B = \{x\in A|P(x)\}$也是一个集合。

由分离公理可知空集$\emptyset$唯一。

还可知，如果$A$和$B$为一个集合，则集合$A\backslash B = \{x \in A|x \notin B\}$也为一个集合。$M$为一个集合，A为它的子集，则$C_M A$也为一个集合。