# Logo 语言基本语法
Logo 是一种图形编程语言，它使用命令来描述图形的绘制。以下是 Logo 语言的基本语法：

### 控制画笔
* `fd n`：向前移动 n 个单位。
* `bk n`：向后移动 n 个单位。
* `lt n`：向左旋转 n 个度。
* `rt n`：向右旋转 n 个度。
* `ct` ：清除画布。
* `pu` ：抬起画笔。
* `pd` ：放下画笔。
* `ht` ：隐藏画笔。
* `dt` : 显示画笔。
* `setpensize n` ：设置画笔大小为 n 个单位。
* `setpencolor color` ：设置画笔颜色为 color。
* `home` ：将画笔移动到画布的左上角。
* `label text` ：在当前位置绘制文本。
* `setxy x y` ：将画笔移动到坐标 (x, y)。

### 变量
* `make variable value` ：定义一个变量。
* `print variable` ：打印变量的值。
* 取值 `:variable` ：获取变量的值。

### 字符串
* `"string"` ：定义一个字符串。

### 整数
* `n` ：定义一个整数。

### 算数运算符
* `sqrt n` ：计算 n 的平方根。
* `power n m` ：计算 n 的 m 次方。
* `ln n` ：计[logo.md](logo.md)算 n 的对数。
* `log10 n` ：计算 n 的以 10 为底的对数。
* `exp n` ：计算 e 的 n 次方。

### 重复
* `repeat n [commands]` ：重复执行命令 n 次。

### 循环
* `while condition [commands]` ：重复执行命令，直到条件变为 false。

### 条件判断
* `if condition [commands] else [commands] end` ：如果条件为 true，执行第一组命令，否则执行第二组命令。


### 随机数
* `random n` ：生成一个随机数，范围为 0 到 n。

### 程序
* `to functionName [arguments] [commands] end` ：定义一个函数。

### 递归调用
```
to recur:n
    if :n < 1[stop]
    fd :n
    rt 90
    recur : 0.95 * :n
end
```
