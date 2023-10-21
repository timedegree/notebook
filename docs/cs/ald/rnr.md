---
stas: true
---

# 递推与递归

## 排列组合

### 选择

> 从 $1\sim n$ 这 $n(n<20)$ 个整数中随机选取任意多个,输出所有可能的选择方案.

每个整数只有选和不选两个情况,我们只需在每次递归时分别尝试"选"与"不选"两个分支即可.

代码如下:

```cpp
vector<int> chosen;
int n;

void calc(int x)
{
    if(x==n+1)
    {
        for(int i=0;i< chosen.size();i++)
        {
            printf("%d ",chosen[i]);
        }
        printf("\n");
        return ;
    }
    calc(x+1);
    chosen.push_back(x);
    calc(x + 1);
    chosen.pop_back();
}

int main()
{
    scanf("%d",&n);

    calc(1);

    return 0;
}
```

### 组合

> 从 $1\sim n$ 这 $n$ 个整数中随机选取 $m(0\leq m \leq n \leq 20)$ 个,输出所有可能的选择方案.

只需要修改上面选择的代码即可,添加递归边界为超过 $m$ 个数或者为加上剩余的数也不够 $m$ 个,就可以知道继续下去也无解了.

代码如下:

```cpp
vector<int> chosen;
vector<vector<int>> result;
int n,m,num=0;

void calc(int x)
{
    if(chosen.size()>m||chosen.size() + (n-x+1) < m)
    {
        return;
    }
    if(x==n+1)
    {
        result.push_back(chosen);
        num++;
        return ;
    }
    calc(x+1);
    chosen.push_back(x);
    calc(x + 1);
    chosen.pop_back();
}

int main()
{
    scanf("%d%d",&n,&m);

    calc(1);

    sort(result.begin(),result.end());

    for(int i=0;i<num;i++)
    {
        for(int j=0;j<m;j++)
        {
            printf("%d ",result[i][j]);
        }
        printf("\n");
    }

    return 0;
}
```

### 全排列

> 把 $1\sim n$ 这 $n(n<10)$ 个整数排成一行后随机打乱顺序,输出所有可能的次序.

每次递归时,我们尝试把每个可用的数作为数列中的下一个数,将问题化为更小的子问题.

代码如下:

```cpp
int order[20];
bool chosen[20];
int n;

void calc(int x)
{
    if(x == n + 1)
    {
        for(int i=1;i<=n;i++)
        {
            printf("%d ",order[i]);
        }
        printf("\n");
        return;
    }
    for(int i=1;i<=n;i++)
    {
        if(chosen[i]) continue;
        order[x] = i;
        chosen[i] = 1;
        calc(x+1);
        chosen[i] = 0; 
    }
}

int main()
{   
    scanf("%d",&n);

    calc(1);

    return 0;
}
```

## 等比数列求和

> 求 $A^B$ 的所有约数之和 $\mathrm{mod} \ 9901$ 的值.

对 $A$ 分解质因数,表示为 $p_1^{c_1}\cdot p_2^{c_2} \cdot p_3^{c_3}\cdot...\cdot p_n^{c_n}$ ,可知 $A^B$ 的质因数是 $p_1^{B\cdot c_1}\cdot p_2^{B\cdot c_2} \cdot p_3^{B\cdot c_3}\cdot...\cdot p_n^{B\cdot c_n}$ ,我们将其记作 $p_1^{k_1}\cdot p_2^{k_2} \cdot p_3^{k_3}\cdot...\cdot p_n^{k_n}$ ,其中 $0\leq k_i \leq B\cdot c_i$ .

由生成函数的技巧,我们可知 $A^B$ 的约数之和为:

$$
(1+p_1+p_1^2+...+p_1^{B\cdot c_1})\cdot (1+p_2+p_2^2+...+p_2^{B\cdot c_2})\cdot (1+p_n+p_n^2+...+p_n^{B\cdot c_n})
$$

上式中每一项都为等比数列求和,如果使用等比数列求和公式需要做除法,而 $\mathrm{mod}$ 只对加,减,乘具有分配律.于是我们可以使用递归加分治计算等比数列之和.

分治法计算 $\mathrm{sum}(p,c) = 1+p+p^2+...+p^c$

若 $c$ 为奇数:

$$
\begin{align*}
\mathrm{sum}(p,c) &= (1+p+p^2+...+p^{\frac{c-1}{2}})+(p^{\frac{c+1}{2}}+...+p^c)\\
&= (1+p+p^2+...+p^{\frac{c-1}{2}})+p^{\frac{c+1}{2}}\cdot(1+p+p^2+...+p^{\frac{c-1}{2}})\\
&= (1+p^{\frac{c+1}{2}})\cdot \mathrm{sum}(p,\frac{c-1}{2})
\end{align*}
$$

若 $c$ 为偶数,类似的:

$$
\mathrm{sum}(p,c) = (1+p^{\frac{c}{2}}) \cdot \mathrm{sum}(p,\frac{c}{2}-1) + p^c
$$

结合快速幂可在 $\Omicron(\log c)$ 的时间复杂度中求出等比数列之和.

代码如下:

```cpp
long long ans=1,divisor_count[50000010];
int mod=9901;
vector <int> prime_divisors;

void find_divisors(long long n)
{
    for(int i=2;i<=n/i;i++)
    {   
        if(n%i==0)
        {
            prime_divisors.push_back(i);
            while(n % i == 0)
            {
                divisor_count[prime_divisors[prime_divisors.size()-1]]++;
                n = n/i;
            }
        }
    }
    if(n>1)
    {
        prime_divisors.push_back(n);
        divisor_count[prime_divisors[prime_divisors.size()-1]]++;
    }
    return;
}

long long quick_power(long long a,long long b)
{   
    long long power=1;
    for(;b;b>>=1)
    {
        if(b&1) power = (power*a)%mod;
        a = (a*a)%mod;
    }
    return power;
}

long long sum(long long p,long long k)
{   
    if(k == 1) return 1;
    if(k % 2 == 0) {  
        return ((quick_power(p, k / 2) + 1) * sum(p, k / 2))% mod;
    }
    return (quick_power(p, k - 1) + sum(p, k - 1)) % mod;
}

int main()
{
    long long A,B;

    scanf("%lld%lld",&A,&B);

    find_divisors(A);

    for(int i=0;i<prime_divisors.size();i++)
    {
        long long p = prime_divisors[i],k = divisor_count[prime_divisors[i]]*B;
        ans = (ans*sum(p,k+1))%mod;
    }
    if(!A) ans = 0;

    printf("%lld",ans);
    
    return 0;
}
```