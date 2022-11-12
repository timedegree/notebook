# 通用概念

## 逻辑符号

|符号|含义|解释|
|--|--|--|
|$\neg$|非|$\neg p$,表示$p$的否命题|
|$\wedge$|与|$p\wedge q$,表示$p$与$q$同时成立|
|$\vee$|或|$p \vee q$,表示$p$与$q$至少一个成立|
|$\Rightarrow$|蕴含|$p \Rightarrow q$,表示$p$为$q$的充分条件|
|$\Leftrightarrow$|等价|$p \Leftrightarrow q$,表示$p$等价于$q$|

## 集合

### 性质
1. 集合可由任何有区别的对象组成
2. 集合由其组成对象整体唯一确定
3. 任何性质都确定一个具有该性质的对象的集合

### 表示
- $x$为一个对象，$P(x)$示$x$具有性质$P$,则用$\{x|P(x)\}$表示集合
- 用$\{x_1,x_2,...,x_n\}$表示集合
- 单元素集合$\{a\}$在不引起歧义时，可用$a$表示

### 包含关系
|符号|含义|
|--|:--:|
|$x \in X$|x属于X|
|$x \notin X$|x不属于X|
|$A = B$|A等于B.即$\forall x((x \in A) \Leftrightarrow(x \in B))$或$(A \subset B)\wedge(B \subset A)$|
|$A \subset B$|A包含于B.即$\forall x ((x \in A)\Rightarrow(x \in B))$|

注:空集可表示为 $\emptyset := \{x \in M|x \neq x\}$

### 集合运算
|运算|符号|含义|
|--|--|:--:|
|并集|$A \cup B$|$A \cup B := \{(x \in A)\vee (x \in B)\}$|
|交集|$A \cap B$|$A \cap B := \{(x \in A)\wedge (x \in B)\}$|
|差集|$A \backslash B$|$A \backslash B := \{(x \in A)\wedge (x \notin B)\}$|

### 笛卡尔积
集合$X \times Y := \{(x,y)|(x\in X)\wedge(y \in Y)\}$称为集合$X$，$Y$的笛卡尔积或直积，其中形如$(x,y)$的二元组称为序偶。$X \times X$简记为$X^2$。

设序偶$(x_1,x_2)$为集合$X_1$与$X_2$的直积$Z = X_1 \times X_2$的元素。$x_1$称为序偶$z$的第一投影$pr_1 z$,$x_2$称为序偶$z$的第二投影$pr_2 z$.同时称为序偶$z$的坐标
