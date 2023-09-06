---
stas: True
---

# 实数

## 1.实数系的公理系统和某些一般性质

### 1.1 实数集的定义

如果以下四组条件成立,则集合$\mathbb{R}$称为**实数集**,其元素称为**实数**，这些条件称为实数公理系统.

!!! note "($\mathrm{I}$) 加法公理"
    定义了一个映射(加法运算)
    
    $$
        +:\R + \R \rightarrow \R
    $$

    使得$\R$中元素$x,y$中的每个序偶$(x,y)$与某元素$x+y\in \R$相对应,后者称为$x$与$y$的和,并且以下条件成立:
    
    1. 中性元素$0$(在加法中称为零元素或零)存在,并且对于任何$x \in \R$,

    $$
        x+0=0+x=x
    $$

    2. 对于任何元素$x\in \R$,元素$-x$存在,称为$x$的相反元素,它满足,
    
    $$
        x+(-x) = (-x)+x = 0
    $$

    3. 运算$+$满足结合律,即对于$\R$中任何元素$x,y,z$满足,

    $$
        x+(y+z) = (x+y)+z
    $$

    4. 运算$+$满足交换律,即对于$R$中任何元素$x,y$满足,
    
    $$
        x+y = y+x
    $$


如果在某集合$G$上定义了满足公理$1_+,2_+,3_+$的运算,我们就说在$G$是给定了群结构,即$G$是**群**.如果称该运算为加法,就称这个群为**加法群**.如果除此之外,还知道该运算满足交换律,即条件$4_+$成立,就称这个群为**交换群**或**阿贝尔群**.所以$\R$为加法阿贝尔群.

!!! note "($\mathrm{II}$) 乘法公理"
    定义了一个映射(乘法运算)
    
    $$
        \bullet:\R \times \R \rightarrow \R
    $$

    使得$\R$中元素$x,y$中的每个序偶$(x,y)$与某元素$x·y\in \R$相对应,后者称为$x$与$y$的积,并且以下条件成立:

    1. 中性元素$1\in \R \backslash0$(在乘法中称为单位元素或一)存在,并且,
    
    $$
        \forall x \in \R ,x\cdot 1=1\cdot x = x
    $$

    2. 对于任何元素$x \in \R\backslash0$,元素$x_{}^{-1}\in \R$存在,称为$x$的逆元素,满足,

    $$
        x \cdot x_{}^{-1}  = x_{}^{-1} \cdot x = 1
    $$

    3. 运算$\bullet$满足结合律,即对于$\R$中任何元素$x,y,z$满足,
    
    $$
        x\cdot(y\cdot z) = (x\cdot y)\cdot z
    $$

    4. 运算$\bullet$满足交换律,即对于$R$中任何元素$x,y$满足,
    
    $$
        x \cdot y = y\cdot x
    $$

    于是我们可以验证集合$\R\backslash 0$对于乘法运算是群

!!! Note "($\mathrm{I}$,$\mathrm{II}$)加法与乘法的联系"
    乘法相对于加法满足分配律,即$\forall x,y,z\in\R$,
    
    $$
        (x+y)\cdot z = x\cdot z +y\cdot z
    $$

如果在某集合$G$上定义了满足上述全部公理的两种运算,则$G$称为**代数域**,简称**域**.

!!! Note "($\mathrm{III}$)序公理"
    $\R$的元素之间存在关系$\le$,即对于$\R$的元素$x,y$,可以确定$x\le y$是否成立.此时,以下条件成立:

    0. $\forall x \in \R \ (x\le x)$
    1. $(x \le y)\wedge(y\le x)\Rightarrow(x=y)$
    2. $(x\le y)\wedge(y\le z)\Rightarrow(x\le z)$
    3. $\forall x \in \R \ \forall y \in \R\ (x\le y)\vee (y \le x)$
    
    $\R$中的关系$\le$称为不等关系.

如果一个集合某些元素之间的关系，满足公理$0_\le,1_\le,2_\le$,则该集合就称为**偏序集**;如果除此之外还满足公理$3_\le$,即集合的任何两个元素都是可比较的,该集合就称为**线性序集**

!!! Note "($\mathrm{I}$,$\mathrm{III}$)加法和序关系的联系"
    如果$x,y,z$是$\R$的元素,则
    
    $$
        (x\le y) \Rightarrow (x+z\le y+z)
    $$

!!! Note "($\mathrm{II}$,$\mathrm{III}$)乘法和序关系的联系"
    如果$x,y,z$是$\R$的元素,则

    $$
        (0\le x)\wedge (0\le y)\Rightarrow(0 \le x\cdot y)
    $$

!!! note "($\mathrm{IIII})$完备性公理"
    如果$X$与$Y$是$\R$的非空子集,并且对于任何元素$x\in X,y\in Y$有$x\le y$,则存在$c\in \R$,使得对于任何元素$x\in X,y\in Y$有$x\le c \le y$.

可以认为满足这些公理的任何集合$\R$是实数的一种表示,即通常所说的**实数模型**

### 1.2 实数的某些一般的代数性质

!!! note "a.加法公理的推理"
    1. 在实数集中只有唯一的零元素.
    
    ??? Abstract "证明"
        如果$0_1$与$0_2$都是$\R$中的零,则根据零的定义
        
        $$
        0_1=0_1+0_2=0_2+0_1=0_2
        $$
    
    2. 在实数集中,每个元素有唯一的相反元素
    
    ??? Abstract "证明"
        如果$x_1$与$x_2$都是$x\in\R$的相反元素,则
        
        $$
            x_1=x_1+0=x_1+(x+x_2)=(x_1+x)+x_2=0+x_2=x_2
        $$
    
    3. 方程$a+x=b$在$\R$中有唯一解$x=b+(-a)$
    
    ??? Abstract "证明"
        得自每个元素有唯一的相反元素:
        
        $$
        \begin{equation*}
	        \begin{split}
		        (a+x = b )
		        & \Leftrightarrow ((x+a)+(-a)=b+(-a))\\
                & \Leftrightarrow (x+(a+(-a))=b+(-a))\\
                & \Leftrightarrow (x+0=b+(-a))\\
                & \Leftrightarrow x=b+(-a)\\
	        \end{split}
        \end{equation*} 
        $$
