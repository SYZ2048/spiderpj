#! python3
# -*- coding: utf-8 -*-
import os, codecs
import jieba
from collections import Counter
 
def get_words(txt):
    seg_list = jieba.cut(txt)   #对文本进行分词
    c = Counter()
    for x in seg_list:          #进行词频统计
        if len(x)>1 and x != '\r\n':
            c[x] += 1
    print('常用词频度统计结果')
    for (k,v) in c.most_common(50):      #遍历输出高频词
        print('%s%s %s  %d' % ('  '*(5-len(k)), k, '*'*int(v/2), v))

def frequency():
    with codecs.open('../bilibili.txt', 'r', 'utf8') as f:
        txt = f.read()
    get_words(txt)
