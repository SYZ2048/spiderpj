import os
import csv

source_path = './Bigdata/2022-03-20-cloudbed1/istio/'
save_path = './csv_data/2022_03_20_cloudbed1/istio/'
CsvFile = os.listdir(source_path)


if not os.path.exists(save_path):
    os.mkdir(save_path)

for leng in range(len(CsvFile)):
    times, devices, kpi_names, values = [], [], [], [] # 初始化两个list数组分别存放csv文件里图片路径和标签
    with open(source_path+CsvFile[leng]) as f: # 读入原来的csv文件
        reader = csv.reader(f)
        for row in reader:
            time, device, kpi_name, value = row    # 将每行读入的内容分别赋给新的变量
            if time == "timestamp":
                time = "Time"
            if device == "cmdb_id":
                device = "Device"
            if value == "value":
                value = "value(DOUBLE)"

            times.append(time)  # 将读入的图片路径加到list数组中
            devices.append(device)    # 将读入的标签加到list数组中
            kpi_names.append(kpi_name)
            values.append(value)

    for i in range(1, len(times)):
        times[i] = str(int(times[i])*1000)
    for i in range(1, len(devices)):
        devices[i] = "root.2022_03_20_cloudbed1.istio." + devices[i] + '.' + kpi_names[i]
        devices[i] = devices[i].replace('-', '_')
        devices[i] = devices[i].replace('/', '_')
        # devices[i] = devices[i].replace('.0', '_0')
        # devices[i] = devices[i].replace('.1', '_1')
        # devices[i] = devices[i].replace('.2', '_2')
        # devices[i] = devices[i].replace('.3', '_3')
        # devices[i] = devices[i].replace('.4', '_4')
        # devices[i] = devices[i].replace('.5', '_5')
        # devices[i] = devices[i].replace('.6', '_6')
        # devices[i] = devices[i].replace('.7', '_7')
        # devices[i] = devices[i].replace('.8', '_8')
        # devices[i] = devices[i].replace('.9', '_9')
        devices[i] = devices[i].replace('.0', '.p0')
        devices[i] = devices[i].replace('.1', '.p1')
        devices[i] = devices[i].replace('.2', '.p2')
        devices[i] = devices[i].replace('.3', '.p3')
        devices[i] = devices[i].replace('.4', '.p4')
        devices[i] = devices[i].replace('.5', '.p5')
        devices[i] = devices[i].replace('.6', '.p6')
        devices[i] = devices[i].replace('.7', '.p7')
        devices[i] = devices[i].replace('.8', '.p8')
        devices[i] = devices[i].replace('.9', '.p9')


    with open(save_path+CsvFile[leng], 'w', newline='') as csvfile: # 重新写入csv文件
        writer = csv.writer(csvfile)
        # for col, hist in zip(column, hist_column):
        for tm, dev, val in zip(times, devices, values):
            writer.writerow([tm, dev, val])
        csvfile.close()
    print(str(leng) + ': Finished')
