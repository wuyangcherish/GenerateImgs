## python

### 参考

[Get text of childrens in a div with BeautifulSoup](http://stackoverflow.com/questions/20889790/get-text-of-childrens-in-a-div-with-beautifulsoup)

[Find children of nodes useing BeautifulSoup](http://stackoverflow.com/questions/6287529/how-to-find-children-of-nodes-using-beautiful-soup)

[wordcloud 中文不支持的解决办法](http://python.jobbole.com/87496/)

[How to save an pic with request](https://segmentfault.com/q/1010000007024942)

[wordCloud 简书](http://www.jianshu.com/p/2c1748c69204)

[numpy](http://www.jianshu.com/p/57e3c0a92f3a)

[Methods of Flask Response ](http://www.jianshu.com/p/3c757e21e897)

[Flask  Interface response methods](http://blog.csdn.net/bestallen/article/details/53767114)

[path](http://www.cnblogs.com/dkblog/archive/2011/03/25/1995537.html)

### 遇到的问题

> 编码问题

'ascii' codec can't encode characters in position 1-2: ordinal not in range(128)

python 的编码比较的麻烦，所以使用 codecs 模块来进行编码 打开文件的时候用

```
codecs.open('filename','methods','')
```

或者直接指定编码

```
import sys
reload(sys)
sys.setdefaultencoding('utf8')
```

### 用到的知识点

#### 获取数据[beautifulSoup requests]

因为爬取的是百度百科的简介，所以输入一个可以查到的词语 --> 爬取百科这个页面的简介 --> 过滤特殊不需要的字符--> 保存为本地文件。

**requests** 爬取数据，然后用 **Beautiful ** 来获取到想要的节点的内容

读取 ``text = open(path.join('filename.txt')).read()``
获取到文字  或者  ``with open('filename.txt') as f: ....``



####  文件的读取

读取文件 

####  结巴分词

[结巴GitHub 地址](https://github.com/fxsjy/jieba)

有 全模式/精确模式/新词识别/搜索引擎模式

代码中使用的是 **精确模式** 精确模式和全模式就是一个 ``cut_all=False || True`` 的区别，试了下发现精确模式要更好一些。

当然还有类似 **基于 TF-IDF 算法的关键词抽取** 这种模式的



 全部显示

#### word_cloud [词云]

一个可以把图片转成文字的东东，[gitHub 地址](https://github.com/amueller/word_cloud/) 

首先将爬到的数据生成词云图片，--> 用图片当做 mask 背景图片作为生成词云的样子，然后按照图片的形状生成图片 --> 按照图片的颜色生成词云图片 -->完工~

词云制作的代码片段在[gist上面](https://gist.github.com/wuyangcherish/d26759eaa262a910af30d9968d9f7200)  

其中 WordCloud 的参数里面可以指定 ``background=""(default is black)`` ``min_font_size && max_font_size`` 等等


#### 显示到前端

前端使用的是 Vue 的模式，本来可以后端保存到服务器，然后返回个链接的，但是.... 木有服务器。所以直接保存到本地的一个地址。然后前端从这个地址获取图片~


#### 摆几张图哈哈

![玫瑰花生成的图](http://7xlqb6.com1.z0.glb.clouddn.com/word_cloud_1.png)
![猫咪生成的图](http://7xlqb6.com1.z0.glb.clouddn.com/word_cloud_2.png)
