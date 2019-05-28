# -*- coding:utf-8 -*-


import imutils
import cv2
import numpy as np
# pip install --upgrade imutils
# pip install opencv-python



"""

opencv3+python3轮廓检测
https://blog.csdn.net/qq_38660394/article/details/80623280

python3+opencv3识别图片中的物体并截取
https://blog.csdn.net/qq_38660394/article/details/80609323

使用Python和OpenCV检测图像中的物体并将物体裁剪下来
https://blog.csdn.net/liqiancao/article/details/55670749

基于OpenCV-python3实现抠图&替换背景图
https://blog.csdn.net/poso123/article/details/79465577

@Function:
@File    :          OpenCV_center_of_contour.py
@Contact :          lizhou@glorypty.com
@License :          (C)Copyright 2019-2020

@Modify Time        @Author      @Version        @Desciption
------------        -------      --------        -----------
2019-5-28 11:29     lizhou         1.0

"""


# load the image, convert it to grayscale, blur it slightly,
# and threshold it
# file_name ="captcha_img.png"
file_name = r"C:\Users\Administrator\Downloads\captcha_img.png"
# file_name ="captcha_img.png"
img = cv2.imread(file_name)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 首先将读取的图像默认BGR格式转换为HSV格式，然后通过inRange函数获取背景的mask。
# HSV颜色范围参数可调节根据这篇博客: https://blog.csdn.net/taily_duan/article/details/51506776
# hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# lower_blue=np.array([78,43,46])
# upper_blue=np.array([110,255,255])
# mask = cv2.inRange(hsv, lower_blue, upper_blue)
# cv2.imshow('Mask', mask)


# step3：对模糊图像二值化。梯度图像中不大于0的任何像素都设置为0（黑色）。 否则，像素设置为255（白色）。
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)



# 通过腐蚀和膨胀操作进行消除个别点。
# 腐蚀操作将会腐蚀图像中白色像素，以此来消除小斑点， 而膨胀操作将使剩余的白色像素扩张并重新增长回去。
# 执行1次形态学腐蚀与膨胀。
erode=cv2.erode(binary,None,iterations=1)
cv2.imshow('erode',erode)
cv2.waitKey(0)
dilate=cv2.dilate(erode,None,iterations=1)
cv2.imshow('dilate',dilate)
cv2.waitKey(0)



# step6：找出昆虫区域的轮廓。
# cv2.findContours()函数
# 第一个参数是要检索的图片，必须是为二值图，即黑白的（不是灰度图），
# 所以读取的图像要先转成灰度的，再转成二值图，我们在第三步用cv2.threshold()函数已经得到了二值图。
# 第二个参数表示轮廓的检索模式，有四种：
# 1. cv2.RETR_EXTERNAL表示只检测外轮廓
# 2. cv2.RETR_LIST检测的轮廓不建立等级关系
# 3. cv2.RETR_CCOMP建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层。
# 4. cv2.RETR_TREE建立一个等级树结构的轮廓。
# 第三个参数为轮廓的近似方法
# cv2.CHAIN_APPROX_NONE存储所有的轮廓点，相邻的两个点的像素位置差不超过1，即max（abs（x1-x2），abs（y2-y1））==1
# cv2.CHAIN_APPROX_SIMPLE压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，例如一个矩形轮廓只需4个点来保存轮廓信息

# cv2.findContours()函数返回两个值，一个是轮廓本身，还有一个是每条轮廓对应的属性。
# cv2.findContours()函数返回第一个值是list，list中每个元素都是图像中的一个轮廓，用numpy中的ndarray表示。
# 每一个ndarray里保存的是轮廓上的各个点的坐标。我们把list排序，点最多的那个轮廓就是我们要找的昆虫的轮廓。

img,contours,hierarchy=cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# 计算每一条轮廓的中心点、面积、周长等信息
for cnt in contours:
    M = cv2.moments(cnt)#计算第一条轮廓的各阶矩,字典形式

    #print (M)
    #这两行是计算中心点坐标
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    #计算轮廓所包含的面积
    area = cv2.contourArea(cnt)

    #计算轮廓的周长
    # 第二参数可以用来指定对象的形状是闭合的(True),还是打开的(一条曲线)。
    perimeter = cv2.arcLength(cnt,True)

    print("当前轮廓的中心点是(x:{},y:{})，面积是{}，周长是{}".format(cx,cy,area,perimeter))





# OpenCV中通过cv2.drawContours在图像上绘制轮廓。
# 第一个参数是指明在哪幅图像上绘制轮廓
# 第二个参数是轮廓本身，在Python中是一个list,这个list中每个元素都是图像中的一个轮廓，用numpy中的ndarray表示
# 第三个参数指定绘制轮廓list中的哪条轮廓，如果是-1，则绘制其中的所有轮廓
# 第四个参数是轮廓线条的颜色
# 第五个参数是轮廓线条的粗细
cv2.drawContours(dilate,contours,0,(0,0,255),1)
cv2.imshow("img", dilate)
# cv2.imwrite("1_"+file_name, dilate)
cv2.waitKey(0)
