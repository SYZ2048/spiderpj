import requests # 发送请求模块
import re 
import json
import time

def spider():
    # 接受用户输入的bv号
    bv = input('请输入一个bv号：\n')
    bv = str(bv)
    # 构建请求头（这里只需要浏览器信息）
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }  #这里采用直接请求url获得弹幕文件，因此也不需要cookie
    # 根据bv号去寻找目标视频
    url = "https://api.bilibili.com/x/player/pagelist?bvid=" + bv + '&jsonp=jsonp'
    response = requests.get(url = url, headers = headers).content.decode('utf-8') #注意网页的编码格式
    # 此时传回的是json结构，将它转变为字典形式
    r_dict = json.loads(response)
    # cid位于字典data字段下的列表中的又一个字典，接下来获取cid
    values = r_dict['data']  # 先拿到列表
    for mem in values:
        cid = mem.get('cid') # 找到cid对应值（comment id）
        cid = str(cid)
    # 得到cid后用cid找到b站提供的最近弹幕xml的文件接口（url形式）
    url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=' + cid
    time.sleep(0.5)
    response = requests.get(url = url, headers = headers).content.decode('utf-8') # 重新请求，转码
    patten = r'<d p=.*?>(.*?)</d>' #用正则去获得实际弹幕内容，这里格式比较整齐单一，因此泛化即可
    b_list = re.findall(patten, response,re.S) #re.S代表在整体字符串中匹配，不做换行考虑
    # 这里要提取出p标签的第一个参数，采用先正则分组，再依次划分,这里采用去尾法保留单位到秒
    patten2 =  r'<d (.*?)</d>'
    p_list = re.findall(patten2, response,re.S)
    t_list = []
    for v in p_list:
        v = v.split('.')[0]
        v = v.split('\"')[1]
        v = int(v)
        t_list.append(v)
    i = 0
    # 针对于p标签中的第一个出现时间参数，
    for comment in b_list:
        with open('output/bilibili.txt', mode ='a', encoding ='utf-8') as f: # 用with open打开文件并将编码格式设置为utf-8,mode = a表示追加，每次写入从文本最后开始
            f.write(comment.strip())
            f.write(' ')
            f.write(str(t_list[i]))
            f.write(' ')
            hour = int(t_list[i] / 60)
            sec = t_list[i] % 60
            if sec >= 10:
                time_p = str(hour) + ':' + str(sec)
            else:
                time_p = str(hour) + ':' + '0' + str(sec)
            f.write(time_p)
            i = i + 1
            f.write('\n')

    # b_list中为实际弹幕，与之索引位相同的在t_list中为它的出现秒数
