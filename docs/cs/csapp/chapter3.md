---
stas: true
comment: True
---
# 第三章 程序的机器级表示

## 3.1 程序编码

### 3.1.1 机器级代码

#### 计算机系统的两种抽象

- 使用 **ISA** 定义机器级程序的格式与行为
- 机器级程序使用虚拟地址，内存模型类似字节数组

#### 机器代码下可见的处理器状态

- **程序计数器** CP 给出将要执行的指令在内存中的地址
- **整数寄存器** 16 个寄存器被用来存储 64 位的值，值可以是地址或整数数据。
	- 部分用来存储参数、局部变量和函数返回值
	- 部分用来记录重要的程序状态
- **条件码寄存器** 保存最近执行的算术或逻辑指令的状态信息。通常用来实现控制流或者数据流的条件变化
- **向量寄存器** 存放一个或多个整数或浮点数

### 3.1.2 代码示例

#### 文中常用编译指令

~~~linux
linux> gcc -Og -S mstore.c # c编译器产生汇编代码，产生 mstore.s

linux> gcc -Og -c mstore.c # c编译器编译并汇编代码，产生 mstore.o

linux> objdump -d mstore.o # 查看汇编
~~~

#### x86-64 下机器码和反汇编代码特性

- x86-64 的指令长度从 1 到 15 字节不等。常用指令的字节数较少
- 从某个指定位置开始，可以将字节唯一的解码成机器指令。例如*pushq %rbx*是唯一以 53 开头的指令
- 反汇编器基于机器码文件中的字节序列来确定汇编代码
- 反汇编器与 gcc 两者产生的汇编代码略有不同

## 3.2 数据格式

### 3.2.1 C 语言数据类型在 x86-64 中的大小

| C declaration | Intel Data Type  | Assembly-code suffix | Size (bytes) |
| ------------- | ---------------- | -------------------- | ----------- |
| char          | Byte             | b                    | 1           |
| short         | Word             | w                    | 2           |
| int           | Double word      | l                    | 4           |
| long          | Quad word        | q                    | 8           |
| char *        | Quad word        | q                    | 8           |
| float         | Single precision | s                    | 4           |
| double        | Double precision | l                    | 8           |

## 3.3 访问信息

### 3.3.1 整数寄存器

| 63   | 31    | 15    | 7     | Effect        |
|:---- |:----- |:----- |:----- | ------------- |
| %rax | %eax  | %ax   | %al   | Return value  |
| %rbx | %ebx  | %bx   | %bl   | Callee saved  |
| %rcx | %ecx  | %cx   | %cl   | 4th argument  |
| %rdx | %edx  | %dx   | %dl   | 3th argument  |
| %rsi | %esi  | %si   | %sil  | 2nd argument  |
| %rdi | %edi  | %di   | %dil  | 1st argument  |
| %rbp | %ebp  | %bp   | %bpl  | Callee saved  |
| %rsp | %esp  | %sp   | %spl  | Stack pointer |
| %r8  | %r8d  | %r8w  | %r8b  | 5th argument  |
| %r9  | %r9d  | %r9w  | %r9b  | 6th argument  |
| %r10 | %r10d | %r10w | %r10b | Caller saved  |
| %r11 | %r11d | %r11w | %r11b | Caller saved  |
| %r12 | %r12d | %r12w | %r12b | Callee saved  |
| %r13 | %r13d | %r13w | %r13b | Callee saved  |
| %r14 | %r14d | %r14w | %r14b | Callee saved  |
| %r15 | %r15d | %r15w | %r15b | Callee saved  |

### 3.3.2 操作数

大多数指令有一个或多个**操作数**，用以指示一个操作中要使用的源数据值，以及放置结果的目的位置。源数据值以常数形式或是从寄存器或内存中读出。因此，操作数被分为三种类型

- **立即数** 表示常数值，格式为 $\$ Imm$ ，$Imm$ 是标准 C 语言中表示的整数。
- **寄存器** 表示某个寄存器的内容，格式为 $r_a$ 
- **内存引用** 根据计算出来的地址访问某个内存，格式为 $Imm(r_b,r_i,s)$ ，可得到多种寻址方式，$s$ 仅能为 **1，2，4，8**

#### 操作数格式

| Type      |       Form       |                       Operand value                       | Name                |
| --------- |:----------------:|:---------------------------------------------------------:| ------------------- |
| Immediate |     $\$Imm$      |                           $Imm$                           | Immediate           |
| Register  |      $r_a$       |                     $\mathsf{R}[r_a]$                     | Register            |
| Memory    |      $Imm$       |                     $\mathsf{M}[Imm]$                     | Absolute            |
| Memory    |     $(r_a)$      |               $\mathsf{M}[\mathsf{R}[r_a]]$               | Indirect            |
| Memory    |    $Imm(r_b)$    |             $\mathsf{M}[Imm+\mathsf{R}[r_b]]$             | Base + displacement |
| Memory    |   $(r_b,r_i)$    |       $\mathsf{M}[\mathsf{R}[r_b]+\mathsf{R}[r_i]]$       | Indexed             |
| Memory    |  $Imm(r_b,r_i)$  |     $\mathsf{M}[Imm+\mathsf{R}[r_b]+\mathsf{R}[r_i]]$     | Indexed             |
| Memory    |    $(,r_i,s)$    |           $\mathsf{M}[\mathsf{R}[r_a] \cdot s]$           | Scaled indexed      |
| Memory    |  $Imm(,r_i,s)$   |        $\mathsf{M}[Imm + \mathsf{R}[r_a] \cdot s]$        | Scaled indexed      |
| Memory    |  $(r_b,r_i,s)$   |   $\mathsf{M}[\mathsf{R}[r_b]+\mathsf{R}[r_i]\cdot s]$    | Scaled indexed      |
| Memory    | $Imm(r_b,r_i,s)$ | $\mathsf{M}[Imm+\mathsf{R}[r_b]+\mathsf{R}[r_i] \cdot s]$ | Scaled indexed      |

### 3.3.3 数据传输指令

- 分为源操作数和目标操作数
- 源操作数为一个立即数、寄存器或内存地址，目标操作数为寄存器或内存地址

数据传输指令分为三类

- 简单数据传输指令
- 零扩展数据传输指令
- 符号扩展数据传输指令

表如下：

#### 简单数据传输指令
| Instruction   | Effect           | Description             |
| ------------- | ---------------- |:----------------------- |
| MOV $S,D$     | $D \leftarrow S$ | Move                    |
| movb          |                  | Move byte               |
| movw          |                  | Move word               |
| movl          |                  | Move double word        |
| movq          |                  | Move quad word          |
| movabsq $I,R$ | $R \leftarrow I$ | Move absolute quad word |

#### 零扩展数据传输指令
| Instruction | Effect                                | Description                            |
| ----------- | ------------------------------------- | :------------------------------------- |
| MOVZ $S,D$  | $D \leftarrow \mathsf{ZeroExtend}(S)$ | Move with zero extension               |
| movzbw      |                                       | Move zero-extended byte to word        |
| movzbl      |                                       | Move zero-extended byte to double word |
| movzwl      |                                       | Move zero-extended word to double word |
| movzbq      |                                       | Move zero-extended byte to quad word   |
| movzwq      |                                       | Move zero-extended word to quad word   |

#### 符号扩展数据传输指令
| Instruction | Effect                                                 | Description                                 |
| ----------- | ------------------------------------------------------ | :------------------------------------------ |
| MOVS $S,D$  | $D \leftarrow \mathsf{SignExtend}(S)$                  | Move with sign extension                    |
| movsbw      |                                                        | Move sign-extended byte to word             |
| movsbl      |                                                        | Move sign-extended byte to double word      |
| movswl      |                                                        | Move sign-extended word to double word      |
| movsbq      |                                                        | Move sign-extended byte to quad word        |
| movswq      |                                                        | Move sign-extended word to quad word        |
| movslq      |                                                        | Move sign-extended double word to quad word |
| ctlq        | $\mathsf{\%rax}\leftarrow\mathsf{SignExtend(\%eax)}$ | Sign-extended %eax to %rax                  |

### 3.3.4 压入与弹出栈数据

#### 压栈与出栈指令

- 只有一个操作数
- push 指令的操作数可以为一个**寄存器**、**内存地址**或**立即数**
- pop 指令的操作数可以为一个**寄存器**或**内存地址**

| Instruction | Effect                                           | Description    |
| ----------- | ------------------------------------------------ | -------------- |
| pushq $S$   | $\mathsf{R[\%rsp]}\leftarrow\mathsf{R[\%rsp]}-8$ | Push quad word |
|             | $\mathsf{M[\%rsp]}\leftarrow S$                  |                |
| popq $S$    | $D \leftarrow \mathsf{M[\%rsp]}$                 | Pop quad word  |
|             | $\mathsf{R[\%rsp]}\leftarrow\mathsf{R[\%rsp]}+8$ |                |

#### 指令等价

push %rbp指令可与如下指令等价

~~~asm
pushq %rbp

subq 8,%rsp
movq %rbp,(%rsp)
~~~

pop %rbp指令同理

~~~asm
popq %rbp

movq (%rsp),%rbp
addq 8,%rsp
~~~

## 3.4 算数与逻辑运算

算术和逻辑运算可分为四组：

| Instruction | Effect                    | Description              |
| ----------- | ------------------------- | :----------------------- |
| 加载有效地址      |                           |                          |
| leaq $S,D$  | $D\leftarrow \&S$         | Load Effective address   |
| 一元运算        |                           |                          |
| INC $D$     | $D\leftarrow D+1$         | Increment                |
| DEC $D$     | $D\leftarrow D-1$         | Decrement                |
| NEG $D$     | $D\leftarrow -D$          | Negate                   |
| NOT $D$     | $D\leftarrow\  \sim D$    | Complement               |
| 二元运算        |                           |                          |
| ADD $S,D$   | $D\leftarrow D+S$         | Add                      |
| SUB $S,D$   | $D\leftarrow D-S$         | Subtract                 |
| IMUL $S,D$  | $D\leftarrow D* S$        | Mutiply                  |
| XOR $S,D$   | $D\leftarrow D^{\wedge}S$ | Exclusive-or             |
| OR $S,D$    | $D\leftarrow D\mid S$     | Or                       |
| AND $S,D$   | $D\leftarrow D\&S$        | And                      |
| 移位运算        |                           |                          |
| SAL $k,D$   | $D\leftarrow D<<k$        | Left shift               |
| SHL $k,D$   | $D\leftarrow D<<k$        | Left shift (same as sal) |
| SAR $k,D$   | $D\leftarrow D>>_Ak$      | Arithmetic right shift   |
| SHR $k,D$   | $D\leftarrow D>>_Lk$      | Logical right shift      |

### 3.4.1 加载有效地址

- 源操作数是**内存地址**,目标操作数**只能为寄存器**
- 效果是**将源操作数计算出的有效地址放入目标操作数中**
- 也可以用来**描述普通的计算操作**，例如 leaq 7 (%rdx,%rdx, 5)，%rax 将寄存器 %rax 的值设置为 $5x+7$

### 3.4.2 一元和二元运算

#### 一元运算

- 只有一个操作数，同时作为源操作数和目标操作数、
- 操作数为一个**寄存器**或**内存地址**
#### 二元运算

- 有两个操作数，分为源操作数和目标数
- 源操作数为一个**寄存器**、**内存地址**或**立即数**
- 目标操作数为一个**寄存器**或**内存地址**

### 3.4.3 移位运算

- 有两个操作数
- 源操作数为一个**立即数**
- 目标操作数为一个**寄存器**或**内存地址**

### 3.4.4 特殊的算术运算

| Instruction | Effect                                                                | Description            |
| ----------- | --------------------------------------------------------------------- | ---------------------- |
| imulq $S$   | $\mathsf{R[\%rdx]:R[\%rax]}\leftarrow S\times \mathsf{R[\%rax]}$      | Signed full multiply   |
| mulq $S$    | $\mathsf{R[\%rdx]:R[\%rax]}\leftarrow S\times \mathsf{R[\%rax]}$      | Unsigned full multiply |
| cqto        | $\mathsf{R[\%rdx]: R[\%rax]}\leftarrow \mathsf{SignExtend(R[\%rax])}$ | Convert to oct word    |
| idivq $S$   | $\mathsf{R[\%rdx]}\leftarrow\mathsf{R[\%rdx]: R[\%rax]} \ mod \ S$    | Signed divide          |
|             | $\mathsf{R[\%rax]}\leftarrow\mathsf{R[\%rdx]: R[\%rax]} \div S$       |                        |
| divq $S$    | $\mathsf{R[\%rdx]}\leftarrow\mathsf{R[\%rdx]: R[\%rax]} \ mod \ S$    | Unsigned divide        |
|             | $\mathsf{R[\%rax]}\leftarrow\mathsf{R[\%rdx]: R[\%rax]} \div S$       |                        |
