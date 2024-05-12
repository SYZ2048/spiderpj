import os
import csv

source_path = './Bigdata/2022-03-20-cloudbed1/service/'
save_path = './csv_data/2022_03_20_cloudbed1/service/'
CsvFile = os.listdir(source_path)


if not os.path.exists(save_path):
    os.mkdir(save_path)

for leng in range(len(CsvFile)):
    devices, times, rrs, srs, mrts, counts = [], [], [], [], [], [] # 初始化两个list数组分别存放csv文件里图片路径和标签
    with open(source_path+CsvFile[leng]) as f: # 读入原来的csv文件
        reader = csv.reader(f)
        for row in reader:
            service, time, rr, sr, mrt, count = row    # 将每行读入的内容分别赋给新的变量
            if time == "timestamp":
                time = "Time"
            if service == "service":
                service = "Device"

            times.append(time)  # 将读入的图片路径加到list数组中
            devices.append(service)    # 将读入的标签加到list数组中
            rrs.append(rr)
            srs.append(sr)
            mrts.append(mrt)
            counts.append(count)

    for i in range(1, len(times)):
        times[i] = str(int(times[i])*1000)
    for i in range(1, len(devices)):
        devices[i] = "root.2022_03_20_cloudbed1.service." + devices[i]
        devices[i] = devices[i].replace('-', '_')
        devices[i] = devices[i].replace('/', '_')

    with open(save_path+CsvFile[leng], 'w', newline='') as csvfile: # 重新写入csv文件
        writer = csv.writer(csvfile)
        # for col, hist in zip(column, hist_column):
        for tm, dev, r, s, mr, cnt in zip(times, devices, rrs, srs, mrts, counts):
            writer.writerow([tm, dev, r, s, mr, cnt])
        csvfile.close()
    print(str(leng) + ': Finished')
