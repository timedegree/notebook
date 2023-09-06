---
stas: True
---

# 语法

!!! Abstract
    重新把笔记整理了一下，文字更加简洁了。~~但是其实笔记也才刚写不久。~~

    ??? info "参考"
        - [Rust语言圣经](https://course.rs)
        - [翔哥的Rust笔记](https://note.tonycrane.cc/cs/pl/rust/basic/)


## 1 变量

### 1.1 变量命名

- 原生标识符（raw identifiers）
    - 不能使用已经存在的关键字
    - 在关键字前加r#后可以使用
- 命名规范：

|条目|惯例|
|:--------|:--------:|
|包 Crates|unclear|
|模块 Modules|snake_case|
|类型 Types|UpperCamelCase|
|特征 Traits|UpperCamelCase|
|枚举 Enumerations|UpperCamelCase|
|结构体 Structs|UpperCamelCase|
|函数 Functions|snake_case|
|方法 Methods|snake_case|
|通用构造器 General constructors|new or with_more_details|
|转换构造器 Conversion constructors|from_some_other_type|
|宏 Macros|snake_case!|
|局部变量 Local variables|snake_case|
|静态类型 Statics|SCREAMING_SNAKE_CASE|
|常量 Constants|SCREAMING_SNAKE_CASE|
|类型参数 Type parameters|	UpperCamelCase，通常使用一个大写字母: T|
|生命周期 Lifetimes|通常使用小写字母: 'a，'de，'src|
|Features|unclear but see C-FEATURE|

### 1.2 变量的绑定与可变性

在rust中我们使用let进行变量绑定，如：

```Rust
let a = 233;
```

需要注意的是，使用let绑定变量默认是不可变的（immutable），使其可变需要在let后加mut，或是再次使用let改变其绑定的值，如：

~~~Rust
let mut a =233;
a = a + 1;

let a = a + 1;
\\二者等效
~~~

若是不使变量改为可变变量，编译器会发出警告。

变量存在但没有使用也会警告，但可以在变量前加单下划线`_`来忽略警告。

### 1.3 变量解构与结构式赋值

与python中的解包类似
~~~ Rust
let (a, mut b): (bool,bool) = (true, false);// a = true,不可变; b = false，可变
let (a, b, c, d);
(a, b) = (1, 2);// a = 1;b = 2
[c, .., d, _] = [1, 2, 3, 4, 5]; // c = 1; d = 4
~~~

### 1.4 常量

常量使用const来声明，命名规则使用全大写蛇底式，且不允许在const后加mut,可以在任意作用域下声明。
~~~Rust
const PI: f32 = 3.14159;
~~~

### 1.5 变量遮蔽

Rust 允许声明相同的变量名，在后面声明的变量会遮蔽掉前面声明的变量，在可变性中已经提到过。即：
~~~Rust
let a = 233;
let a = a + 1;
~~~

## 2 基本数据类型

### 2.1 整型

i+长度（有符号）、u+长度（无符号）

- i8、i16、i32、i64、i128、u8、u16、u32、u64、u128
- isize、usize 长度由 CPU 决定，32 位 CPU 则是 32 位，64 位 CPU 则是 64 位
- 整型字面量中间可以插入 _
- 字面量结尾可以接类型，例如`#!rust 10i32, 10_i32`
- 字面量，十六进制 0x...、八进制 0o...、二进制 0b...、字节（仅 u8）b'A'
- 整型默认使用 i32 类型
- 使用 as 来转换类型，例如 `#!rust let a: u16 = 1_u8 as u16;`

debug 模式编译时产生溢出会 panic，而在 release 模式下则不会 panic，按照补码循环溢出。但不能依赖这种行为，想要这样的效果应该标准库的一些方法：

- wrapping_*\** 方法，按照补码循环溢出，例如 a.wrapping_add(1)
- checked_*\** 方法，如果产生溢出了，则会返回 None
- overflowing_*\** 方法，返回结果以及指示是否溢出的布尔值
- saturating_*\** 方法，如果会溢出则保持在最大/最小值上

#### 2.1.1 布尔型

布尔型用bool来声明，值为`true`或`false`，占用一个字节

### 2.2 浮点型

- f32为单精度浮点型，f64为双精度浮点型
- 避免在浮点数上测试相等性
- 当结果在数学上可能存在未定义时，需要格外的小心
- 可以使用`#!rust is_nan()`等方法来判断一个数值是否为NaN
- 可以直接对数值使用方法，如`#!rust 3.14_f32.round()`

### 2.3 数值运算

- `+ - * / %`：加减乘除取模
- `& | ^ ! << >>`：位运算
- 同样类型才能进行计算、类型转换必须是显式的
- 其它运算可以通过方法实现，.pow() 计算指数、.sqrt() 计算平方根、，.log() 取对数、.div_euclid() 整除、.div_floor() 等等

### 2.4 序列

Rust 提供了一个非常简洁的方式，用来生成连续的数值，但序列只允许用于数字或字符类型。
~~~ Rust
for i in 1..=5 {
    println!("{}",i);
}

for i in 'a'..='z' {
    println!("{}",i);
}
~~~

### 2.5 字符型

在Rust中字符以char声明。

- char占用4个字节内存
- 使用单引号''括单个字符，双引号""括字符串
- 直接存储Unicode，而非UTF-8

### 2.6 单元型
- 单元类型就是 ()，唯一的值也是 ()，完全不占用任何内存。
-  main 函数就返回单元类型 ()

### 2.7 语句与表达式

- 简单来说，在一行代码后带分号的就是一个语句，而不带分号的是一个表达式，
- 表达式有返回值,而语不会返回值
- 表达式可以是语句的一部分，比如 `#!rust let a = if condition {5} else {6}`; 中 `#!rust if condition {5} else {6}` 就是一个表达式，而整体是一个语句
- 函数调用是表达式，因为会有返回值，即使“无”返回值也会返回单元类型
- 用大括号包裹的返回一个值的语句块也是表达式：
~~~Rust
let a = {
    let b = 1;
    b + 1
};
~~~

### 2.8 函数

~~~Rust
fn add(i: i32, j: i32) -> i32 { //以fn声明函数,括号内写参数及其类型，后用箭头表示返回值
   i + j //与return i + j等效
 }
}
~~~

- 定义函数使用关键字 fn
- 函数名、参数名使用蛇底式命名
- 必须显式指定参数类型，除了返回 () 外要显式指定返回值类型
- 通过 ; 结尾的表达式返回一个 ()
- 中途返回可以使用 return 关键字（带不带分号均可）
- 永不返回的函数类型为 !（相当于 python 类型标注中的 NoReturn），称为发散函数，一般用于一定会抛出 panic 的函数或者无限循环：
~~~ Rust
fn dead_end() -> ! {
    panic!("...");
}
fn forever() -> ! {
    loop { /*...*/ };
}
~~~

## 3 所有权与借用
高三比较忙，暂时不更新XD