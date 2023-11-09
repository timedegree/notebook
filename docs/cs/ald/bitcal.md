---
stas: true
---

# 位运算

## 基础运算

|  与   |  或   |   非   | 异或  | 左移  | 右移  |
| :---: | :---: | :----: | :---: | :---: | :---: |
| and,& | or,\| | not,\~ | xor,^ |  <<   |  >>   |

---

## 快速幂

### 普通快速幂

我们可知任意一个正整数可以唯一表示为若干个指数不重复的二进制数,写为十进制下的多项式即为:

$$
b = c_{k-1}2^{k-1}+c_{k-2}2^{k-2}+ ...+c_02^0
$$

若我们要计算 $a^b$ ,则可化为:

$$
a^b = a^{c_{k-1}\cdot 2^{k-1}}\cdot a^{c_{k-2}\cdot 2^{k-2}}\cdot ...\cdot a^{c_0*2^0}
$$

于是,代码如下:

```cpp
long long quick_power(long long a,long long b)
{
    long long power=1;
    for(;b;b>>=1)
    {
        if(b&1) power*=a;
        a*=a;
    }
    return power;
}
```

### 模重复平方法

与上述类似,但所需计算的值改为 $a^b\mathrm{mod} p$ .此时我们只需在每次做乘运算时对结果取模即可.

```cpp
long long quick_power(long long a,long long b,long long p)
{
    long long power=1%p;
    for(;b;b>>=1)
    {
        if(b&1) power = (power*a)%p;
        a = a*a%p;
    }
    return power;
}
```

### 矩阵快速幂

> 求斐波那契数列的第 $n$ 项.

我们可知斐波那契数列的递推公式为

$$
\begin{align*}
F_{n+2} =& F_{n+1} + F_n\\
F_{n} =& F_n
\end{align*}
$$

将其转化为矩阵就是

$$
\begin{bmatrix}
F_{n+2}\\
F_{n+1}
\end{bmatrix} =
\begin{bmatrix}
F_{n+1}+F_{n}\\
F_{n+1}
\end{bmatrix} =
\begin{bmatrix}
1&1\\
1&0
\end{bmatrix}
\begin{bmatrix}
F_{n+1}\\
F_{n}
\end{bmatrix}
$$

于是 $F_n$ 可由有限次的矩阵的乘法表示出来

$$
\begin{bmatrix}
F_{n}\\
F_{n-1}
\end{bmatrix} =
{\begin{bmatrix}
1&1\\
1&0
\end{bmatrix}}^{n-2}
\begin{bmatrix}
F_{2}\\
F_{1}
\end{bmatrix}
$$

代码如下:

```cpp

struct Matrix{
    int value[3][3];

    Matrix() { memset(value,0,sizeof value); }

    Matrix operator*(const Matrix &b) const {
        Matrix res;
        for(int i=1;i<=2;i++)
        {
            for(int j=1;j<=2;j++)
            {
                for(int k=1;k<=2;k++)
                {
                    res.value[i][j] = (res.value[i][j] + value[i][k] * b.value[k][j]);
                }
            }
        }
        return res;
            
    }
}ans,base;

void init() {
  base.value[1][1] = base.value[1][2] = base.value[2][1] = 1;
  ans.value[1][1] = ans.value[1][2] = 1;
}

void quick_power(int x)
{
    for(;x;x>>=1)
    {
        if(x&1) ans = ans * base;
        base = base * base;
    }
}

int main()
{
    int n;
    scanf("%d",&n);
    if(n<=2)
    {
        puts("1");
        return 0;
    }
    init();
    quick_power(n-1);

    printf("%d",ans.value[2][1]);
    return 0;
}

```

### 在乘法中使用快速幂思想

假如我们现在需要计算 $a\cdot b\mod p$.

#### 方法一

使用快速幂的思想，把b用二进制表示,那么:

$$
a =  c_{k-1}\cdot a \cdot 2^{k-1} + c_{k-2}\cdot a \cdot 2^{k-2} + ... + c_0\cdot a\cdot 2^0
$$

代码如下:

```cpp
long long mul(long long a,long long b,long long p)
{
    long long product=0;
    for(;b;b>>=1)
    {
        if(b&1) ans = (ans+a)%p;
        a = a*2%p;
    }
    return product;
}
```

#### 方法二

可知 $a\cdot b \mod p = a\cdot b - \left \lfloor a\cdot b /p\right \rfloor \cdot p$.

代码如下:

```cpp
#define unsigned long long ull;
ull mul(ull a,ull b;ull p)
{
    a %= p,b %= p;
    ull c = (long double) a*b/p;
    ull x = a*b,y=c*p;
    long long product = (long long)(x%p) - (long long)(y%p);
    if(ans < 0) ans += p;
    return ans;
}
```

---

## 二进制状态压缩

|                    操作                    |             运算              |
| :----------------------------------------: | :---------------------------: |
|     取出整数$n$在二进制表示下的第$k$位     |        $(n>>k)\ \&\ 1$        |
| 取出整数$n$在二进制表示下的第$0\sim k-1$位 |      $n\ \&\ ((1<<k)-1)$      |
|    把整数$n$在二进制表示下的第$k$位取反    | $n \ \mathrm{xor}\  (1 << k)$ |
|  对整数$n$在二进制表示下的第$k$位赋值$1$   |        $n\ \mid\ (1<<k)$        |
|  对整数$n$在二进制表示下的第$k$位赋值$0$   |      $n\ \& \ (~(1<<k))$      |

---

## 成对变换

- $n$ 为偶数时, $n \ \mathrm{xor}\ 1$ 等于 $n+1$.
- $n$ 为奇数时, $n \ \mathrm{xor}\ 1$ 等于 $n-1$.

---

## lowbit 运算

$\mathrm{lowbit}(n)$ 定义为**非负整数 $n$ 在二进制表示下最低位的 $1$ 及其后边所有的 $0$ 构成的数值**.例如 $n = 10$ 的二进制表示为 ${(1010)}_{2}$ ,则 $\mathrm{lowbit}(n) = 2 = {(10)}_2$.

公式推导:

设 $n>0$ , $n$ 的第 $k$ 位是 $1$ ,第 $0\sim k-1$ 位都是$0$.
为了实现 $\mathrm{lowbit}$ 运算,我们先把 $n$ 取反,再令 $n = n + 1$ ,此时因为进位,第 $k$ 位变为 $1$,第 $0\sim k-1$位都是 $0$ .

在上面的取反加 $1$ 操作后, $n$ 的第 $k+1$ 到最高位恰好与原来相反,所以 $n \& (\sim n + 1)$ 仅仅有第 $k$ 位为 $1$ ,其余位都为 $0$ .在补码表示下, $\sim n = -1-n$,因此:

$$
\mathrm{lowbit}(n) = n\ \&\ (\sim n + 1) = n \ \& \ (-n)
$$

$\mathrm{lowbit}$ 运算配合 $\mathrm{Hash}$ 可以找出整数二进制表示下所有是 $1$ 的位.为了达到这个目的,我们只需不断把 $n$ 赋值为 $n - \mathrm{lowbit}(n)$ ,直到 $n = 0$.

代码如下:

```cpp
const MAX_N = 1 << 20;
int H[MAX_N + 1];
for(int i=0;i<=20;i++) H[1<<i] = i;
while(cin>>n)
{
    while(n>0)
    {
        cout<<H[n&-n]<<" ";
        n -= n & -n;
    }
    cout<<endl;
}
```

利用 $\forall k \in [0,35]$ , $2^k \ \mathrm{mod}\ 37$ 互不相等,且恰好取遍 $1\sim 36$,可以改进代码.

修改后代码如下:

```cpp
int H[37];
for(int i = 0;i < 36;i++) H[(1ll << i) % 37] = i
while(cin>>n)
{
    while(n>0)
    {
        cout<< H[(n & -n) % 37] <<' ';
        n = n & -n;
    }
    cout << endl;
}
```