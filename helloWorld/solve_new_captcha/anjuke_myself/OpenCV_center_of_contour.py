# -*- coding:utf-8 -*-


import imutils
import cv2
import numpy
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
file_name ="captcha_img.jpg"
# file_name ="captcha_img.png"
img = cv2.imread(file_name)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# ====================================================================================
# step2:用Sobel算子计算x，y方向上的梯度，之后在x方向上减去y方向上的梯度，通过这个减法，我们留下具有高水平梯度和低垂直梯度的图像区域。
# gradX = cv2.Sobel(gray, cv2.CV_32F, dx=1, dy=0, ksize=-1)
# gradY = cv2.Sobel(gray, cv2.CV_32F, dx=0, dy=1, ksize=-1)
#
# # subtract the y-gradient from the x-gradient
# gradient = cv2.subtract(gradX, gradY)
# gradient = cv2.convertScaleAbs(gradient)
# # show image
# cv2.imshow("img", gradient)
# cv2.waitKey()


# step3：去除图像上的噪声。首先使用低通滤泼器平滑图像（9 x 9内核）,这将有助于平滑图像中的高频噪声。
# 低通滤波器的目标是降低图像的变化率。如将每个像素替换为该像素周围像素的均值。这样就可以平滑并替代那些强度变化明显的区域。
# 然后，对模糊图像二值化。梯度图像中不大于90的任何像素都设置为0（黑色）。 否则，像素设置为255（白色）。
# blur and threshold the image
# blurred = cv2.blur(gradient, (9,9))
# _, thresh = cv2.threshold(blurred, 51, 255, cv2.THRESH_BINARY)
# # SHOW IMAGE
# cv2.imshow("img", thresh)
# cv2.waitKey()
# # ====================================================================================

# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# ret, binary = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
ret, binary = cv2.threshold(gray, 51, 255, cv2.THRESH_BINARY)


# 找出轮廓：
# findContours()函数接受的参数为二值图，即黑白的（不是灰度图）
# findContours()这个函数实际上返回了三个值：
# 第一个，也是最坑爹的一个，它返回了你所处理的图像
# 第二个，正是我们要找的，轮廓的点集
# 第三个，各层轮廓的索引
img,contours,hierarchy=cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# OpenCV中通过cv2.drawContours在图像上绘制轮廓。
# 第一个参数是指明在哪幅图像上绘制轮廓
# 第二个参数是轮廓本身，在Python中是一个list,这个list中每个元素都是图像中的一个轮廓，用numpy中的ndarray表示
# 第三个参数指定绘制轮廓list中的哪条轮廓，如果是-1，则绘制其中的所有轮廓
# 第四个参数是轮廓线条的颜色
# 第五个参数是轮廓线条的粗细
cv2.drawContours(img,contours,0,(0,0,255),1)
cv2.imshow("img", img)
cv2.imwrite("1_"+file_name, img)
cv2.waitKey(0)
