import jieba
import re

def deal_txt(shuju):
    result_list=[]
    with open('stopwords.txt',encoding='utf-8') as f:
        con=f.readlines()
        stop_words=set()
        for i in con:
            i=i.replace("\n","")
            stop_words.add(i)
    for word in shuju:
        if word not in stop_words:
            result_list.append(word)
    result=' '.join(result_list)
    return result

def seg():
    f=open('output/bilibili_timerank.txt','r',encoding="utf-8")
    target=open("output/bilibili_seg.txt",'w',encoding="utf-8")
    line_num=1
    line=f.readline()
    while line:
        a=line.split()
        line=' '.join(a)
        line_s=''.join(re.findall('[\u4e00-\u9fa5]+',line,re.S))  # 筛选出所有中文
        line_seg=jieba.cut(line_s)  # jieba分词
        final_list = deal_txt(line_seg)  # 去除停用词
        target.writelines(final_list+' ')  # +'\n')
        line = f.readline()
        line_num =line_num+1
        #print(line_num," ")
    f.close()
    target.close()
