from PIL import Image
import os
import random

srcPath = 'E:\\CS182\\proj\\Training-Image-Estimators-without-Image-Ground-Truth\\compressive_sensing\\data\\imagenet\\train\\'   # 所要读取修改的文件夹
# srcPath = 'E:\\CS182\\proj\\Training-Image-Estimators-without-Image-Ground-Truth\\compressive_sensing\\my\\m_img\\'
dstPath = 'E:\\CS182\\proj\\Training-Image-Estimators-without-Image-Ground-Truth\\compressive_sensing\\my\\m_crop\\train\\'    # 修改后所存放路径
filelist = os.listdir(srcPath)

list1=[]
list2=[]
# 读取图片
for filename in filelist:
    filename1 = os.path.splitext(filename)[1]  # 读取文件后缀名
    filename0 = os.path.splitext(filename)[0]  # 读取文件名
    list1.append(filename0)
    list2.append(filename1)

for i in range(0,len(list1)):
    filea = str(srcPath+list1[i]+list2[i])
    img_1 = Image.open(filea)
    if img_1.size[0] < 363 or img_1.size[1] < 363:  continue
    # crop randomly
    x = random.randint(0,img_1.size[0]-363)
    y = random.randint(0,img_1.size[1]-363)
    # 设置裁剪的位置
    crop_box = (x,y,x+363,y+363)
    # 裁剪图片
    img_2 = img_1.crop(crop_box)
    #保存图片
    img_2.save(dstPath+list1[i]+'.JPEG')
print('已经截图成功')
