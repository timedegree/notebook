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

## 3.5 控制

### 3.5.1 条件码

- 是一位寄存器
- 描述最近的算术或逻辑运算属性
- 常用于执行条件分支指令

#### 常用条件码

- CF 进位标志： 运算使得最高位产生进位，可检测无符号操作的溢出
- ZF 零标志：运算结果为 0 
- SF 符号标志：运算结果为负数
- OF 溢出标志：运算使得补码溢出，负溢出和正溢出均可

#### 特殊情况

1. leaq 指令不改变条件码
2. xor 指令会将 CF 和 OF 置为 0
3. 移位运算会将 CF 置为最后一个被移出的位，OF 置为 0
4. inc 和 dec 不会改变 CF 但会设置 ZF 和 OF

#### CMP 与 TEST 指令

除算术或逻辑运算外，存在 CMP 与 TEST 两类指令也会**设置条件码**，但它们**不改变寄存器的值**。

| Instruction    | Based on   | Description         |
| -------------- | ---------- | ------------------- |
| CMP $S_1,S_2$  | $S_2-S_1$  | Compare             |
| cmpb           |            | Compare byte        |
| cmpw           |            | Compare word        |
| cmpl           |            | Compare double word |
| cmpq           |            | Compare quad word   |
| TEST $S_1,S_2$ | $S_1\&S_2$ | Test                |
| testb          |            | Test byte           |
| testw          |            | Test word           |
| testl          |            | Test double word    |
| testq          |            | Test quad word      |

### 3.5.2 访问条件码

除了自己读去条件码，还有三种使用条件码的一般方式

1. 根据一些条件码的混合来设置单独一位 0 或 1
2. 条件跳转到程序的其他部分
3. 条件传输

SET 指令常用以实现第一种使用方式，表如下

| Instruction | Synonym | Effect                                                               | Set condition                   |
| ----------- | ------- | -------------------------------------------------------------------- | :------------------------------ |
| sete $D$    | setz    | $D\leftarrow\mathrm{ZF}$                                             | Equal / zero                    |
| setne $D$   | setnz   | $D\leftarrow\ \sim\mathrm{ZF}$                                       | Not equal / not zero            |
| sets $D$    |         | $D\leftarrow\mathrm{SF}$                                             | Negative                        |
| setns $D$   |         | $D\leftarrow\ \sim\mathrm{SF}$                                       | Nonnegative                     |
| setg $D$    | setnle  | $D\leftarrow\ \sim(\mathrm{SF\text{\text{\textasciicircum}} OF})\&\sim\mathrm{ZF}$ | Greater (signed $>$)            |
| setge $D$   | setnl   | $D\leftarrow\ \sim (\mathrm{SF\text{\textasciicircum} OF})$                 | Greater or equal (signed $\ge$) |
| setl $D$    | setnge  | $D\leftarrow\mathrm{SF\text{\textasciicircum} OF}$                          | Less (signed <)                 |
| setle $D$   | setng   | $D\leftarrow(\mathrm{SF\text{\textasciicircum} OF})\mid\mathrm{ZF}$         | Less or equal (signed $\le$)    |
| seta $D$    | setnbe  | $D\leftarrow\ \sim\mathrm{CF}\&\sim\mathrm{ZF}$                      | Above (unsigned >)              |
| setae $D$   | setnb   | $D\leftarrow\ \sim\mathrm{CF}$                                       | Above or equal (unsigned $\ge$) |
| setb $D$    | setnae  | $D\leftarrow\mathrm{CF}$                                             | Below (unsigned <)              |
| setbe $D$   | setna   | $D\leftarrow\mathrm{CF}\mid\mathrm{ZF}$                              | Below or equal (unsigned $\le$) |

### 3.5.3 条件跳转

在一般的程序执行中，指令以列出的顺序来运行。jump 指令可以使程序切换到一个全新的位置执行。
跳转的目的地一般在汇编代码中以 **label** 的形式显式的标出。但在 **jmp** 指令时，可不使用 label 而通过 **oprand** 来进行**间接跳转**。
表如下：

|  Instruction   | Synonym | Jump condition                                          | Description                     |
|:--------------:| ------- | ------------------------------------------------------- |:------------------------------- |
|  jmp $Label$   |         | 1                                                       | Direct jump                     |
| jmp $*Operand$ |         | 1                                                       | Indirect jump                   |
|   je $Label$   | jz      | $\mathrm{ZF}$                                           | Equal / zero                    |
|  jne $Label$   | jnz     | $\sim\mathrm{ZF}$                                       | Not equal / not zero            |
|   js $Label$   |         | $\mathrm{SF}$                                           | Negative                        |
|  jns $Label$   |         | $\sim\mathrm{SF}$                                       | Nonnegative                     |
|   jg $Label$   | jnle    | $\sim(\mathrm{SF\text{\textasciicircum} OF})\&\sim\mathrm{ZF}$ | Greater (signed >)              |
|  jge $Label$   | jnl     | $\sim (\mathrm{SF\text{\textasciicircum} OF})$                 | Greater or equal (signed $\ge$) |
|   jl $Label$   | jnge    | $\mathrm{SF\text{\textasciicircum} OF}$                        | Less (signed <)                 |
|  jle $Label$   | jng     | $(\mathrm{SF\text{\textasciicircum} OF})\mid\mathrm{ZF}$       | Less or equal (signed $\le$)    |
|   ja $Label$   | jnbe    | $\sim\mathrm{CF}\&\sim\mathrm{ZF}$                      | Above (unsigned >)              |
|  jae $Label$   | jnb     | $\sim\mathrm{CF}$                                       | Above or equal (unsigned $\ge$) |
|   jb $Label$   | jnae    | $\mathrm{CF}$                                           | Below (unsigned <)              |
|      jbe       | jna     | $\mathrm{CF}\mid\mathrm{ZF}$                            | Below or equal (unsigned $\le$) |

### 3.5.4 使用条件控制实现条件分支

将 C 中的条件语句翻译为汇编代码的传统方法是通过**控制**的条件转移。通常汇编代码中的分支结构类似于 C 中的 goto 风格代码。C 中的 if-else 语句模板一般为：

~~~c
if(test-expr)
	then-statement
else
	else-statement
~~~

而汇编通常会将其翻译为类似如下的 C 代码形式：

~~~c
	t = test-expr
	if(!t)
		goto false;
	then-statement
	goto done;
false:
	else-statement
done:
~~~

例如：

- 原始 C 代码

```c
long lt_cnt = 0;
long ge_cnt = 0;

long absdiff_se(long x,long y)
{
	long result;
	if(x < y){
		lt_cnt++;
		result = x - y;
	}
	else {
		ge_cnt++;
		result = x - y;
	}
	return result;
}
```

- 等价的 goto 版本

~~~c
long gotodiff_se(long x,long y)
{
	long result;
	if(x >= y)
		goto x_ge_y;
	lt_cnt++;
	result = y - x;
	return result;
x_ge_y:
	ge_cnt++;
	result = x - y;
	return result;
}
~~~

- 产生的汇编代码

~~~x86-asm
absdiff_se:
	cmpq %rsi, %rdi
	jge .L2
	addq $1, lt_cnt(%rip)
	movq %rsi, %rax
	subq %rdi, %rax
	ret
.L2:
	addq $1, ge_cnt(%rip)
	movq %rdi, %rax
	subq %rsi, %rax
	ret
~~~

### 3.5.5  使用条件传送来实现条件分支

另一种替代的策略是使用数据的条件转移。通过计算一个操作的两种结果，然后再根据条件从其中选取一个。

#### 条件传送指令

- 源操作数和目的操作数可以是 16、32 或 64 位长。不支持单字节条件传送
- 汇编器通过目标寄存器推断出条件传送指令的操作数长度
- 处理器无需预测测试结果就可以执行条件传送

| Instruction  | Synonym | Move Condition                                                  | Description                     |
| ------------ | ------- | --------------------------------------------------------------- | :------------------------------ |
| cmove $S,R$  | cmovz   | $\mathsf{ZF}$                                                   | Equal / zero                    |
| cmovne $S,R$ | cmovnz  | $\sim\mathsf{ZF}$                                               | Not equal / not zero            |
| cmovs $S,R$  |         | $\mathsf{SF}$                                                   | Negative                        |
| cmovns $S,R$ |         | $\sim\mathsf{SF}$                                               | Nonnegative                     |
| cmovg $S,R$  | cmovnle | $\sim(\mathsf{SF}\text{\textasciicircum}\mathsf{OF})\&\sim\mathsf{ZF}$ | Greater (signed >)              |
| cmovge $S,R$ | cmovnl  | $\sim(\mathsf{SF}\text{\textasciicircum}\mathsf{OF})$                  | Greater or equal (signed $\ge$) |
| cmovl $S,R$  | cmovnge | $(\mathsf{SF}\text{\textasciicircum}\mathsf{OF})$                      | Less (signed <)                 |
| cmovle $S,R$ | cmovng  | $\sim(\mathsf{SF}\text{\textasciicircum}\mathsf{OF})\mid\mathsf{ZF}$   | Less or equal (signed $\le$)    |
| cmova $S,R$  | cmovnbe | $\sim\mathsf{CF}\&\sim\mathsf{ZF}$                              | Above (unsigned >)              |
| cmovae $S,R$ | cmovnb  | $\sim\mathsf{CF}$                                               | Above or equal (unsigned $\ge$) |
| cmovb $S,R$  | cmovnae | $\mathsf{CF}$                                                   | Below (unsigned <)              |
| cmovbe $S,R$ | cmovna  | $\mathsf{CF}\mid\mathsf{ZF}$                                    | Below or equal (unsigned $\le$) |
C 中的条件赋值即三目运算符，如下：

~~~c
v = test-expr ? then-expr : else-expr
~~~

使用条件转移编译会得到如下形式代码：

~~~c
	if(!test-expr)
		goto false;
	v = then-expr
	goto done;
false:
	v = else-expr;
done:
~~~

同 3.5.4 的 C 代码，使用条件传送的汇编代码如下：

~~~x86-asm
absdiff:
	movq %rsi, %rax
	subq %rdi, %rax
	movq %rdi, %rdx
	subq %rsi, %rdx
	cmpq %rsi, %rdi
	cmovge %rdx, %rax
	ret
~~~

并非所有条件表达式都可以使用条件传送来编译。由于给出的代码会对 then-expr 和 else-expr 都求值，若任意一个产生错误条件或副作用，就会产生非法的行为。

