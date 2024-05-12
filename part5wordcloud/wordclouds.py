import wordcloud #导入词云库
import jieba #导入第三方分词库


def generwordcloud(inputdoc, outputpng):
    stopwords = set()
    content = [line.strip() for line in open('stopwords.txt', encoding='UTF-8').readlines()]
    stopwords.update(content)

    f = open(inputdoc, "rb")#导入本地文本文档
    t = f.read()#读取文本内容
    f.close()#关闭文件

    ls = jieba.lcut(t)#将文本内容返回为列表类型的分词
    txt = " ".join(ls)#用空格分割返回的分词
    w = wordcloud.WordCloud(font_path="msyh.ttc", width=1000, height=700, repeat=False, background_color="white", collocations=False, stopwords=stopwords)
    w.generate(txt)#向WordCloud对象w中加载文本txt
    w.to_file(outputpng)#输出词云

