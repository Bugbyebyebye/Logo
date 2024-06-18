# Logo语法测试用例
## 变量
#### 测试语句
`make n 100` 
#### 效果
![img.png](img/img.png)

## 数学函数
#### 开方
`sqrt 100 | sqrt :n`
#### 效果
![img_1.png](img/img_1.png)
#### 求平方
`power 2 3 | power :n 2`
#### 效果
![img_2.png](img/img_2.png)
#### 求对数
`ln 100 | ln :n | log10 :n | exp 2`
#### 效果
![img_3.png](img/img_3.png)
#### 随机数
`random 100`
#### 效果
![img.png](img/img9.png)

## 画图
#### 测试语句
`repeat 4 [fd 100 rt 90] | repeat 4 [repeat 4 [fd 100 rt 90] rt 90] |repeat 8 [repeat 4 [fd 100 rt 90] rt 45]`
#### 效果
![img_4.png](img/img_4.png)
#### 测试语句
`repeat 8 [repeat 4 [fd 100 rt 90] rt 45]`
#### 效果
![img.png](img/img_5.png)
#### 抬起放下笔
`fd 80 rt 90 fd 80 rt 90 fd 80 rt 90 fd 80 |
pu bk 20 rt 90 fd 20 pd |
fd 40 rt 90 fd 40 rt 90 fd 40 rt 90 fd 40`
#### 效果
![img.png](img/img6.png)
#### 清空屏幕
`repeat 4 [fd 100 rt 90]` and `ct`
#### 效果
![img.png](img/img7.png)
#### 标签
`make s "hello logo!" | setpensize 1 | label :s`
#### 效果
![img.png](img/img8.png)

## 条件语句
`make n 100 | if :n > 50 [fd 100]`
#### 效果


## 函数
#### 测试语句

#### 效果
