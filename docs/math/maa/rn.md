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

!!! Note "($\mathrm{I}$,$\mathrm{II}$) 加法与乘法的联系"
    乘法相对于加法满足分配律,即$\forall x,y,z\in\R$,
    
    $$
        (x+y)\cdot z = x\cdot z +y\cdot z
    $$

如果在某集合$G$上定义了满足上述全部公理的两种运算,则$G$称为**代数域**,简称**域**.

!!! Note "($\mathrm{III}$) 序公理"
    $\R$的元素之间存在关系$\le$,即对于$\R$的元素$x,y$,可以确定$x\le y$是否成立.此时,以下条件成立:

    0. $\forall x \in \R \ (x\le x)$
    1. $(x \le y)\wedge(y\le x)\Rightarrow(x=y)$
    2. $(x\le y)\wedge(y\le z)\Rightarrow(x\le z)$
    3. $\forall x \in \R \ \forall y \in \R\ (x\le y)\vee (y \le x)$
    
    $\R$中的关系$\le$称为不等关系.

如果一个集合某些元素之间的关系，满足公理$0_\le,1_\le,2_\le$,则该集合就称为**偏序集**;如果除此之外还满足公理$3_\le$,即集合的任何两个元素都是可比较的,该集合就称为**线性序集**

!!! Note "($\mathrm{I}$,$\mathrm{III}$) 加法和序关系的联系"
    如果$x,y,z$是$\R$的元素,则
    
    $$
        (x\le y) \Rightarrow (x+z\le y+z)
    $$

!!! Note "($\mathrm{II}$,$\mathrm{III}$) 乘法和序关系的联系"
    如果$x,y,z$是$\R$的元素,则

    $$
        (0\le x)\wedge (0\le y)\Rightarrow(0 \le x\cdot y)
    $$

!!! note "($\mathrm{IIII})$ 完备性公理"
    如果$X$与$Y$是$\R$的非空子集,并且对于任何元素$x\in X,y\in Y$有$x\le y$,则存在$c\in \R$,使得对于任何元素$x\in X,y\in Y$有$x\le c \le y$.

可以认为满足这些公理的任何集合$\R$是实数的一种表示,即通常所说的**实数模型**

### 1.2 实数的某些一般的代数性质

以下将说明如何从上述公理得到数的那些众所周知的性质

!!! note "a.加法公理的推论"
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
    
    表达式$b+(-a)$也可写为$b-a$的形式

!!! note "b.乘法公理的推论"
    1. 在实数集中只有唯一的单位元素
    2. 每个数$x\neq0$只有唯一的逆元素(倒数)$x^{-1}$
    3. 方程
    
    $$
        a\cdot x =b
    $$

    在$a\in \R\backslash 0$时有唯一解
    
    $$
        x = b\cdot a^{-1}
    $$

!!! note "c.加法和乘法联系公理的推论"
    1. 对于任何$x\in\R$
    
    $$
        x\cdot 0 = 0\cdot x = x
    $$

    ??? Abstract "证明"
        
        $$
            (x\cdot 0 = x\cdot (0+0)=x\cdot 0+x\cdot 0)\Rightarrow (x\cdot 0 = x\cdot 0+(-(x\cdot 0))=0)
        $$
    
    可以看出,若$x\in \R\backslash0$,则$x^{-1}\in \R\backslash0$.
    
    2. $(x\cdot y=0)\Rightarrow(x=0)\vee(y=0)$
    
    ??? Abstract "证明"
        例如,如果$y\neq0$,则根据关于$x$的方程$x\cdot y =0$的解的唯一性,我们求出$x=0\cdot y^{-1}=0$.
    
    3. 对于任何$x\in\R$,
    
    $$
        -x=(-1)\cdot x
    $$

    ??? Abstract "证明"
        $x+(-1)\cdot x = (1+(-1))x=0\cdot x = x\cdot 0 =0$,再由相反元素的唯一性得出结论.
    
    4. 对于任何$x\in\R$,
    
    $$
        (-1)(-x) = x
    $$
    
    ??? Abstract "证明"
        得自3.和$-x$的相反元素唯一性.
    
    5. 对于任何$x\in\R$,
    
    $$
        (-x)(-x) = x\cdot x
    $$

    ??? Abstract "证明"
        $$
        \begin{equation*}
	        \begin{split}
		        (-x)(-x)
                & = ((-1)\cdot x)(-x) --推论3\\
                & = (x\cdot(-1))(-x)--交换律\\
                & = x((-1)(-x))--结合律\\
                & = x\cdot x -- 推论4
	        \end{split}
        \end{equation*}
        $$

!!! note "d.序公理的推论"
    关系$x\le y$也可写为$y \ge x$;当$x\neq y$时,关系$x\le y$写为$x<y$,称为**严格不等式**.

    1. 对于任何$x,y\in\R$，在以下关系中恰好只有一个关系成立:
    
    $$
        x<y,x>y,x=y.
    $$

    ??? Abstract "证明"
        得自严格不等式的定义以及公理$1_\le$,$3_\le$.

    2. 对于$\R$中的任何数$x$,$y$,$z$,

    $$
        \begin{array}{c}
            (x<y)\wedge(y\le z)\Rightarrow(x<z)\\
            (x\le y)\wedge(y<z)\Rightarrow(x<z)
        \end{array}
    $$

    ??? Abstract "证明"
        根据不等关系的传递性公理$2_{\le}$,我们有

        $$  
            (x\le y)\wedge(y<z)\Leftrightarrow(x\le y)\wedge(y\le z)\wedge(y\neq z)\Rightarrow(x\le z)
        $$

        剩余任务是验证$x\neq z$,但在相反情况下,

        $$
            (x\le y)\wedge(y < z)\Leftrightarrow(z\le y)\wedge(y<z)\Leftrightarrow(z\le y)\wedge(y\le z)\wedge(y\neq z)
        $$
        
        根据公理$1_{\le}$,由此可知

        $$
            (y=z)\wedge(y\neq z)
        $$
        
        这是矛盾.

!!! note "加法和乘法与序关系的联系公理的推论"
    
    1. 对于$\R$中的任何数$x$,$y$,$z$,$w$,

    $$
        \begin{array}{c}
        (x<y) \Rightarrow (x+z)<(y+z)\\
        (0<x) \Rightarrow (-x<0)\\
        (x)
        \end{array}
    $$