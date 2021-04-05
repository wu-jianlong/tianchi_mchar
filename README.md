# tianchi_mchar
天池学习赛——街景字符编码识别
参看天池学习赛——街景字符编码识别：https://blog.csdn.net/weixin_48994268/article/details/115442639
yolov5训练自己的数据集（一文搞定训练）：https://blog.csdn.net/weixin_48994268/article/details/115282688
1 下载官网数据集至mycoco/all_download_data/目录下   下载链接见mchar_data_list_0515.csv
2  运行merge_images.py文件（将所有数据集存放至mycoco/all_images/）
3  运行json_to_txt.py文件（制作所有图片对应的txt标签，存放至mycoco/all_labels）
4  配置yolov5环境及制作自己的数据集
4.1 配置yolov5环境
4.2 制作自己的数据集
4.2.1 运行make_txt.py文件划分数据集
4.2.2 运行train_val.py文件按照划分好的数据集准备数据
至此mycoco文件夹完成，接着转至yolov5文件夹下
5 训练train.py
6 检测detect.py(已经改好)
