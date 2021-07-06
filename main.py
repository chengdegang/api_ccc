# This is a sample Python script.
import os

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# for i in range(3):
#
#     print("-----")#循环体代码从上往下依次执行3次
#     print("*****")

import cv2
import os

# file = '/Users/jackrechard/PycharmProjects/api_ccc/image2'

def changesize(file):
    imagedirs = []
    resultdir = f"{'/'.join(file.split('/')[:-1])}/result/"
    # print(resultdir)
    os.makedirs(resultdir)
    #找到指定路径下的所有图片文件
    for root, dirs, files in os.walk(file):
        for f in files:
            if '.jpg' in f:
                # print(f)
                #打印文件路径
                # print(os.path.join(root, f))
                imagedirs.append(os.path.join(root, f))
    #遍历所有图片并转换至当前路径
    for i in range(len(imagedirs)):
        image = cv2.imread(imagedirs[i])
        #获取图片的名称
        name = imagedirs[i].split('/')[-1].split('.')[0]
        # print(name)
        change_image = cv2.resize(image, (640,360 ))
        cv2.imwrite(f'{resultdir}{name}_cg.jpg', change_image)
        # print(imagedirs[i])
    print(f'已处理 {len(imagedirs)} 张图片')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    changesize(file = '/Users/jackrechard/PycharmProjects/api_ccc/image2')

    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
