import matplotlib.pyplot as plt

# 平滑函数，通过近似拟合将折线图处理成平滑的图像
def smooth_curve(points, factor=0.8):
    smoothed_points = []
    for point in points:
        if smoothed_points:
            previous = smoothed_points[-1]
            # 通过权重对上一个点和当前点做线性组合，factor是可自定义的权重
            smoothed_points.append(previous * factor + point * (1 - factor))
        else:
            smoothed_points.append(point)
    return smoothed_points

# 处理初始弹幕txt文件，从中提取出弹幕发送的时刻，放入time数组中
def gettime():
    doc = open("output/bilibili.txt", "r", encoding='utf-8')
    time=[]
    done = 0
    while not done:
        line = doc.readline()
        if(line != ''):
            s = line.split(' ', -1)[::-1][1] # 以空格分割，倒序第二个即为弹幕发送时刻
            time.append(int(s))
        else:
            done = 1
    doc.close()
    return time

def getcount(duration, time):
    count=[] # 存储每秒发出的弹幕数量
    for i in range(duration):
        count.append(time.count(i))  # 统计每秒发出的弹幕数量
    return count

def draw(duration):
    count = getcount(duration, gettime()) # 获得统计结果count
    smooth_count = smooth_curve(count, 0.98) # 平滑处理

    # 绘制图像
    plt.figure(figsize=(8,8))
    plt.plot(range(duration), smooth_count , 'm-', linewidth=3, alpha=0.8)
    plt.xlabel('time')
    plt.ylabel('scalar')
    plt.title('Progress Bar')
    plt.fill_between(x=range(duration), y1=0, y2=smooth_count, facecolor='m', alpha=0.4)

    plt.savefig('output/ProgressBar.png', dpi=100) # "高能进度条"图像会存储为ProgressBar.png



