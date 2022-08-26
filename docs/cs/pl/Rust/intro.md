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

构建、运行、发布

- cargo build
- cargo run
- cargo check
- cargo build --release