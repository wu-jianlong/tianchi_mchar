import os
import shutil
train_image_path = './mchar_train/'#下载好的存储路径
val_image_path = './mchar_val/'
dst_image_path = '../all_images/'#文件整合后的位置
if not os.path.exists(dst_image_path):
    os.makedirs(dst_image_path)
train_image_list = os.listdir(train_image_path)
val_image_list = os.listdir(val_image_path)
for img in train_image_list:
    shutil.copy(train_image_path+img, dst_image_path+img)
for img in val_image_list:
    shutil.copy(val_image_path+img, dst_image_path+'val_'+img)
