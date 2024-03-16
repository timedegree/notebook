---
stas: True
---
# x86 汇编

!!! info "Reference"
        - 汇编语言 第四版 王爽
        - [Intel Pentium Instruction Set Reference (Basic Architecture Overview)](https://faydoc.tripod.com/cpu/index.htm)

## 寄存器

8086CPU有14个16位寄存器，8个通用寄存器，4个段寄存器，2个控制寄存器

- 通用寄存器
    - 数据寄存器 ax bx cx dx，用来存放一般性数据。可分为高低八位，高八位为ah bh ch dh，低八位为al bl cl dl，只修改某个八位寄存器，则不会影响到另外一个八位寄存器。
        - ax 
        - bx
        - cx
        - dx
    - 变址寄存器
        - si
        - di
    - 指针寄存器
        - sp 堆栈指针寄存器
        - bp
    - 段寄存器
        - cs 代码段寄存器
        - ds 数据段寄存器
        - ss 堆栈段寄存器
        - es 附加数据段寄存器
    - 控制寄存器
        - ip 指令指针寄存器
        - fl 没学到