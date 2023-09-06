---
stas: True
---

# 前言

## Installation

由于我是Win,直接在官网下载rustup就行，然后打开后一路弄下去就行

卸载、更新、检查
~~~
rustup update
rustup self uninstall
rustc --version
~~~
## rustc

Rust代码的后缀名是**.rs**，通过`rustc code.rs`来编译再运行
## Cargo
通过rustup安装后自带cargo，可以通过`cargo --version`检查

各种命令

- cargo new 新建项目
- cargo build 编译
- cargo run 运行
- cargo check 检查是否编译成功
- cargo build --release 高性能编译
  
## Hello world!

~~~ Rust
fn main() {
    println!("Hello, world!");
}
~~~

## Rust所需要注意的特性
- 控制流：for 和 continue 连在一起使用，实现循环控制。
- 方法语法：由于 Rust 没有继承，因此 Rust 不是传统意义上的面向对象语言，但是它却从 OO 语言那里偷师了方法的使用 record.trim()，record.split(',') 等。
- 高阶函数编程：函数可以作为参数也能作为返回值，例如 .map(|field| field.trim())，这里 map 方法中使用闭包函数作为参数，也可以称呼为 匿名函数、lambda 函数。
- 类型标注：if let Ok(length) = fields[1].parse::<f32>()，通过 ::<f32> 的使用，告诉编译器 length 是一个 f32 类型的浮点数。这种类型标注不是很常用，但是在编译器无法推断出你的数据类型时，就很有用了。
- 条件编译：if cfg!(debug_assertions)，说明紧跟其后的输出（打印）只在 debug 模式下生效。
- 隐式返回：Rust 提供了 return 关键字用于函数返回，但是在很多时候，我们可以省略它。因为 Rust 是 基于表达式的语言。

## 