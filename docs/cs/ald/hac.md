---
stas: true
---
# 高精度

!!! info "Reference"
    - 教练的模板

## 高精加

### 一般高精加

```cpp
vector <int> add(vector<int>&a,vector<int>&b)
{
    vector<int> c;
    int len=max(a.size(),b.size()),t=0;
    for(int i=0;i<len;i++)
    {
        if(i<a.size()) t+=a[i];
        if(i<b.size()) t+=b[i];
        c.push_back(t%10);
        t /= 10;
    }
    if(t) c.push_back(t);

    return c;
}
```

### Base进制高精加

#### 初始化

```cpp
map<int,char>encode_map;
map<char,int>decode_map;

void init()
{
    for(int i=0;i<36;i++)
        {
            if(i<10)
            {
                encode_map[i] = '0'+i;
                decode_map['0'+i] = i;
            }
            else
            {
                encode_map[i] = 'A'+i-10;
                decode_map['A'+i-10] = i;
            }
        }
}
```

#### 主要部分

```cpp
vector <char> add(vector<char>&a,vector<char>&b,int base)
{
    vector<char> c;
    int len=max(a.size(),b.size()),t=0;
    for(int i=0;i<len;i++)
    {
        if(i<a.size()) t+=decode_map[a[i]];
        if(i<b.size()) t+=decode_map[b[i]];
        c.push_back(encode_map[t%base]);
        t /= base;
    }
    if(t) c.push_back(encode_map[t]);

    return c;
}
```

## 高精减

```cpp
bool cmp(vector<int>&a,vector<int>&b)
{
    if(a.size()!=b.size()) return a.size() > b.size();
    for(int i=a.size()-1;i>=0;i--)
    {
        if(a[i]!=b[i]) return a[i]>b[i];
    }
    return false;
}

vector<int> sub(vector<int>&a,vector<int>&b)
{
    if(cmp(b,a)) return sub(b,a);
    vector<int>c;int t=0;
    for(int i=0;i<a.size();i++)
    {
        t = a[i] - t;
        if(i<b.size()) t-=b[i];
        c.push_back((t+10)%10);
        if(t<0) t = 1;
        else t=0;
    }
    while(c.size()>1&&c.back()==0)
    {
        c.pop_back();
    }
    return c;
}
```

## 高精乘

```cpp
vector <int> mul(vector<int>&a,vector<int>&b)
{
    vector<int> c(a.size()+b.size()+7,0);
    for(int i=0;i<b.size();i++)
    {
        for(int j=0;j<a.size();j++)
        {
            c[i+j] += b[i]*a[j];
        }
    }

    for(int i=0;i<c.size();i++)
    {
        c[i+1] += c[i]/10;
        c[i] = c[i]%10;
    }

    while(c.size() > 1 && c.back() == 0)
    {
        c.pop_back();
    }

    return c;
}
```

## 高精除

```cpp
vector<int> div(vector<int> &a,int &b,int &r)
{
    vector<int>c;
    long long t=0;
    for(int i=a.size()-1;i>=0;i--)
    {
        t = t*10 + a[i];
        c.push_back(t/b);
        t%=b;
    }
    r = t%b;
    reverse(c.begin(),c.end());
    while(c.size()>1&&c.back()==0)
        c.pop_back();
    return c;
}
```