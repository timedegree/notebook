---
stas: true
---
# 前缀和与差分

## 前缀和

### 一维前缀和

对于一个数列 $A$ ,它的前缀和定义为:

$$
S_i = \sum_{j=1}^i A_j
$$

部分和,即某区间内数列 $A$ 的和,可表示为前缀和相减的形式:

$$
\mathrm{sum}(l,r) = \sum_{i=1}^r A_i = S_r - S_{l-1}
$$

### 二维前缀和

> 一种新型的激光炸弹,可以摧毁一个边长为 $R$ 的正方形内的所有的目标.现在地图上有 $N(N\le 10^4)$ 个目标, 用整数 $X_i,Y_i \ (0\le X_i \le Y_i\le5000)$ 表示目标在地图上的位置,每个目标都有一个价值 $W_i$.
>
> 激光炸弹的投放是通过卫星定位的,但其一个缺点,就是其爆破范围,即那个边长为 $R$ 的正方形的边必须与 $x,y$ 轴平行.若目标位于爆破正方形的边上,该目标不会被摧毁.求一颗炸弹最多能炸掉地图上总价值为多少的目标.

对于这题,我们可以建立一个二维数组 $A$ ,其中 $A[i][j]$ 就等于位置 $(i,j)$ 上所有目标的价值之和.即对于每个目标:

$$
A[i][j] = \sum_i W_i
$$

接着我们求出 $A$ 的二维前缀和 $S$, 即:

$$
S[i][j] = \sum_{x=1}^i\sum_{y=1}^j A[i][j]
$$

如图:

<!DOCTYPE html>
<html>
<head>
<style>
  .image-container {
    display: flex; /* 使用 Flex 布局将图片水平排列 */
    flex-wrap: wrap; /* 如果图片过多，换行显示 */
  }

  .image {
    margin: 5px; /* 图片之间的间距 */
  }

  .caption {
    text-align: center; /* 标识文本居中显示 */
    font-size: 8px
  }
</style>
</head>
<body>

<div class="image-container">
  <div class="image">
    <img src="../img/pnd-2dpresum1.png" height= 170px width = 170px>
    <p class="caption">S[i-1][j]</p>
  </div>

  <div class="image">
    <img src="../img/pnd-2dpresum2.png" height= 170px width = 170px>
    <p class="caption">S[i][j-1]</p>
  </div>

  <div class="image">
    <img src="../img/pnd-2dpresum3.png" height= 170px width = 170px>
    <p class="caption">S[i-1][j] + S[i][j-1]</p>
  </div>

  <div class="image">
    <img src="../img/pnd-2dpresum4.png" height= 170px width = 170px>
    <p class="caption">S[i-1][j] + S[i][j-1] - S[i-1][j-1]</p>
  </div>

  <!-- 添加更多图片和标识 -->
</div>

</body>
</html>

容易得出以下递推式:

$$
S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + A[i][j]
$$

同理,任意一个边长为 $R$ 的正方形, 我们有:

$$
\sum_{x=i-R+1}^i \sum_{y=j-R+1}^j A[x][y] = S[i][j] - S[i-R][j] - S[i][j-R] + S[i-R][j-R]
$$

因此只需 $\Omicron(n^2)$ 递推求出二位前缀和 $S$ ,然后 $\Omicron(n^2)$ 枚举边长为 $R$ 的正方形的右下角坐标 $(i,j)$ ,即可通过上式 $\Omicron(1)$ 计算出该正方形内所有目标的价值之和.这实际上为"容斥定理"的应用.

代码如下:

```cpp
int martix_pre_sum[5010][5010];

int main()
{
    int r, n;

    scanf("%d%d", &n, &r);

    r = min(r,5001);

    int x, y, w;

    for (int i = 1; i <= n; i++)
    {
        scanf("%d%d%d", &x, &y, &w);
        martix_pre_sum[++x][++y] += w;
    }

    for (int i = 1; i <= 5001; i++)
    {
        for (int j = 1; j <= 5001; j++)
        {
            martix_pre_sum[i][j] = martix_pre_sum[i - 1][j] + martix_pre_sum[i][j - 1] - martix_pre_sum[i - 1][j - 1] + martix_pre_sum[i][j];;
        }
    }

    int res = 0;
    for(int i=r;i<=5001;i++)
    {
        for(int j=r;j<=5001;j++)
        {
            res = max(res,martix_pre_sum[i][j]-martix_pre_sum[i-r][j]-martix_pre_sum[i][j-r]+martix_pre_sum[i-r][j-r]);
        }
    }

    printf("%d",res);

    return 0;
}
```

## 差分

对于一个给定的数列 $A$,它的差分序列 $D$ 定义为:

$$
\begin{align*}
    B_1 =& A_1\\
    B_i =& A_i - A_{i-1}
\end{align*}
$$

可知差分与前缀和是一对互逆运算,差分序列 $B$ 的前缀和序列就是原序列 $A$ ,前缀和 $S$ 的差分序列也是原序列 $A$.