#TF-IDF提取关键词
import jieba.analyse as analyse
import jieba

def extract(outputdoc, flag=()):
    f=open("output/bilibili.txt", "rb").read()
    f_c=" ".join(jieba.cut(f))
    tl=analyse.extract_tags(f_c,
    topK=100, #选取的关键词数量
    withWeight=False, #是否自己设置权重
    allowPOS=flag)

    ft=open(outputdoc,"w")
    ft.write(str(tl))
    ft.close()
    return outputdoc


