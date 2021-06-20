请参考 WSM_crawler代码学习，

# selenium 爬虫学习

## 爬拉勾网 b站视频

5：52位置处用到了模拟按键。

## selenium入门讲解

教了如何找到元素，比如搜索框，按钮，找到后如何在搜索框内输入，再点击按钮。如何回退。

## Selenium六 find_element_by_xpath()的几种方法

https://blog.csdn.net/u012941152/article/details/83011110 

元素的值  \<a >  some value\<\\a\> 用 element.text 得到

所以这么搜索 driver.find_element_by_xpath('//*[contains(text(),"hao123")]' ) 这个方法是最靠谱的！用//\*的方法！

或者中括号里 [text()="testsaveas.pdf"] 也是可以的，不是一定行！

## 下载

## 元素显示源代码

ele = self.find_element_by_id("id")
ele.get_attribute("innerHTML")

outerHTML是整个标签包括内部所有标签，innerHTML是只有内部所有标签

# Parsel

xpath 的用法，//是全局的，要相对于前面的selector就得加. 

![image-20210615205328110](C:\Users\47219\AppData\Roaming\Typora\typora-user-images\image-20210615205328110.png)

```python
selector.css("#samples a")
```

#samples相当于是id的意思，然后 空格连a是指下面的所有子标签里a的标签

# HTML知识

在网页head里面，会有meta标签，方便爬虫使用的，里面可能会有想要的信息。
