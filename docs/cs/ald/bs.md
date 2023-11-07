---
stas: true
---

# 二分

## 整数集合上的二分

### 在单调递增序列寻找某数或其后继

```cpp
int binary_search(int l,int r,int x)
{
    while(l<r)
    {
        int mid = (l+r) >> 1;
        if(a[mid] >= x) r=mid;
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
        int mid = (l+r) >> 1;
        if(a[mid] <= x) l=mid;
        else r = mid - 1;
    }
    return a[l]
}
```