#############################################
#           Data:2021/12/7                  #
#           owner:19307130359               #
#############################################
from snownlp import SnowNLP


# 只删除弹幕中的空格，方便split()删词
# 输入一个string 返回一个string
# 例如 “哔哩哔哩 (゜-゜)つロ 干杯~-bilibili 1158 19:18”会变成“哔哩哔哩(゜-゜)つロ干杯~-bilibili 1158 19:18”
def del_space(strs):
    str_nonspace = ""
    for index in range(len(strs)-1):
        if not strs[index] == ' ':
            str_nonspace = str_nonspace + strs[index]
        else:
            if strs[index+1].isdigit():
                str_nonspace = str_nonspace + strs[index]
    # str_nonspace = str_nonspace + strs[len(strs)-1]
    return str_nonspace


# 获取列表的第二个元素，排序的时候使用
def sort_by_time(elem):
    # return float(elem[0])
    return float(elem[0])

def genersentiment():
    seg_bili = []
    summ = 0.0
    average = 0.0
    num = 0.0
    summ_per_min = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    num_per_min = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    negative_num = 0
    positive_num = 0
    neutral_num = 0

    f1 = open('output/bilibili.txt', 'r', encoding="utf-8")
    f2 = open("output/bilibili_timerank.txt", 'w', encoding="utf-8")
    f3 = open("output/result.txt", 'w', encoding="utf-8")

    line = f1.readline()

    line = del_space(line)
    while line:
        a = line.split()
        content = ' '.join(a[0:1])
        # time = ' '.join(a[1:2])
        time = int(' '.join(a[1:2]))
        if content != "":
            c = SnowNLP(content)
            single_bili = [time, round(c.sentiments, 4), content]
            if round(c.sentiments, 4) < 0.5:
                negative_num = negative_num + 1
            elif round(c.sentiments, 4) > 0.5:
                positive_num = positive_num + 1
            else:
                neutral_num = neutral_num + 1
            seg_bili.append(single_bili)
            summ = summ + round(c.sentiments, 4)
            summ_per_min[int(time/60)] = summ_per_min[int(time/60)] + round(c.sentiments, 4)
            num_per_min[int(time/60)] = num_per_min[int(time/60)] + 1

        line = f1.readline()
        num = num + 1
        line = del_space(line)

    seg_bili.sort(key=sort_by_time)
    for i in seg_bili:
        f2.write(str(i))
        f2.write('\n')

    f3.write("total number:")
    f3.write(str(num))
    f3.write("\n")
    f3.write("total sentiment number:")
    f3.write(str(round(summ, 4)))
    f3.write("\n")
    f3.write("average sentiment number:")
    f3.write(str(round(summ/num, 4)))
    f3.write("\n")
    f3.write("positive sentiment number:")
    f3.write(str(positive_num))
    f3.write("\n")
    f3.write("negative sentiment number:")
    f3.write(str(negative_num))
    f3.write("\n")
    f3.write("neutral sentiment number:")
    f3.write(str(neutral_num))
    f3.write("\n")
    for i in range(0, 20):
        f3.write("第")
        f3.write(str(i+1))
        f3.write("分钟的情感总值为")
        f3.write(str(round(summ_per_min[i], 4)))
        f3.write("\t第")
        f3.write(str(i+1))
        f3.write("分钟的弹幕平均情感值为")
        f3.write(str(round(summ_per_min[i]/num_per_min[i], 4)))
        f3.write("\n")

    f1.close()
    f2.close()
