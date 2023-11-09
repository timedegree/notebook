---
stas: true
---

# 二分

## 整数集合上的二分

### 在单调递增序列寻找某数或其后继

```cpp
int binary_search(int l,int r,int x)
{
    while(l < r)
    {
        int mid = (l + r) >> 1;
        if(a[mid] >= x) r = mid;
        else l = mid + 1;
    }
    return a[l]
}
```

### 在单调递增序列寻找某数或其前驱

```cpp
int binary_search(int l,int r,int x)
{
    while(l<r)
    {
        int mid = (l + r) >> 1;
        if(a[mid] <= x) l = mid;
        else r = mid - 1;
    }
    return a[l]
}
```

## 实数域上的二分

### 方法一

确定所需的精度 $eps$ ,以 $l+eps<r$ 为循环边界,接着内容与整数域的二分相同.

```cpp
while(l + eps < r)
{
    double mid = (l+r)/2
    if(calc(mid)) r = mid;
    else l = mid;
}
```

### 方法二

若精度 $eps$ 难以确定,则可尝试固定循环次数,此方法精度通常比手动设定 $eps$ 高.

```cpp
for(int i = 0;i < times;i++)
{
    double mid = (l+r)/2
    if(calc(mid)) r = mid;
    else l = mid;
}
```

