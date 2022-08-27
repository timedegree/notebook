# 语法

## 常见编程概念

### 变量

- 可变性
    - 以let直接声明变量默认为不可变变量
    - 要使用可变变量可以在变量名前加mut
~~~ Rust
let x = 5; //不可变
let mut x = 5; //可变
~~~
- 常量声明 与C/C++类似，方式为：
~~~ Rust
//const 变量名: 数据类型 = 值
const pi: f32 = 3.14159;
~~~
- 变量遮蔽 通过使用相同变量名与let来实现
~~~ Rust
fn main() {
    let x = 5;//声明变量x以及x的值为5

    let x = x + 1;//通过let将x的值变为6

    {//进入内部作用域
        let x = x * 2;//再次将x的值变为12
        println!("The value of x in the inner scope is: {}", x);//输出结果为 12
    }//离开内部作用域x的值变回6

    println!("The value of x is: {}", x);//输出结果为6
}
~~~
!!! warning
    与mut不同,通过使用 let，我们可以对一个值进行一些转换，但在这些转换完成后，变量将是不可变的
    
    第二个不同，我们在使用let关键字时，有效地创建了一个新的变量，所以我们可以改变值的类型，但重复使用相同的名称。

    !!! info "code"    
        正确：
        ~~~ Rust
        let spaces = "   ";
        let spaces = spaces.len();
        ~~~
        错误:
        ~~~ Rust
        let mut spaces = "   ";
        let spaces = spaces.len();
        ~~~

### 数据类型

#### 标量（Scalar）

##### 整型

| 长度      | 有符号 | 无符号 |
| :-------------------------: | :----------------------: |:---------------------:|
| 8-bit |i8 |u8 |
| 16-bit | i16  |u16 |
| 32-bit | i32  |u32 |
| 64-bit | i64  |u64 |
| 128-bit | i128  |u128 |
| arch | isize  |usize |


isize和usize是根据系统而定（32/64）。

同时整型的值也可以用不同进制表示（十六进制0x开头，八进制0o开头，二进制0b开头，单字节字符b开头（b’A’））。

##### 浮点型
单精度为f32,双精度为f64。

##### 布尔型
bool，值为全小写true/false。

##### 字符型
char，大小为4字节(Unicode),单引号为字符，双引号为字符串。

#### 复合类型（Compound）

##### 元组

元组内的元素类型可以不同，但元组类型及元组长度与元组内各个元素有关，如
~~~ Rust
fn main() {
    let tup: (i32, f64, u8) = (500, 6.4, 1);
}
~~~
可以通过.加索引（索引从0开始）来访问元素：
~~~ Rust
fn main() {
    let x: (i32, f64, u8) = (500, 6.4, 1);

    let five_hundred = x.0;

    let six_point_four = x.1;

    let one = x.2;
}
~~~

##### 数组
和Python的列表类似，我们用方括号内逗号分隔的形式来声明数组，但数组长度不可变。如
~~~ Rust
fn main() {
    let a = [1, 2, 3, 4, 5];
}
~~~
或是：
~~~ Rust
fn main() {
let a: [i32; 5] = [1, 2, 3, 4, 5];
}
~~~
在数组中各个元素相同时也可以这样定义
~~~ Rust
fn main() {
let a = [3; 5];
let a = [3, 3, 3, 3, 3];
//二者效果相同
}
~~~