# import sys #python内置库
import cv2  # 计算机视觉领域
import face_recognition  # 人脸识别库，如果读取图片的话，会是图像矩阵
import numpy as np

# 就是每个图片的rgb
# 1.人脸数据
# 2.算法
# 3.建立模型
# 4.训练模型
# 5.测试模型
# 6.上线使用

# 1读取
face_image = face_recognition.load_image_file("D://234.png")  # 读取图片
rows, cols, channels = face_image.shape  # rows:横向像素cols:纵向像素
# 2进行人脸特征提取 向量化
# 128维的五官数据
face_encoding = face_recognition.face_encodings(face_image)
# 3人脸位置
face_locations = face_recognition.face_locations(face_image)
# 判断
n = len(face_encoding)
# 如果超过连个人就退出来
if n > 2:
    print('超过两个人')
    # sys.exit()
face1 = face_encoding[0]
# face2 = face_encoding[1]
# 4比较   阈值 tolerance指定容错率，越小越严格
# result = face_recognition.compare_faces([face1], face2, tolerance=0.5)
# if result == [True]:
#     print(1)
#     name = 'Yes'
# else:
#     print(0)
#     name = 'No'
# 绘图

for i in range(len(face_encoding)):
    face_encoding = face_encoding[i]
    face_location = face_locations[i]
    top, right, bottom, left = face_location
    # 画框             图像                  位置          颜色     粗细
    cv2.rectangle(face_image, (left, top), (right, bottom), (0, 255, 0), 2)
    # 写字
    cv2.putText(face_image, "test", (left, top), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0, 2))
# face_image_rgb = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
# 灰度展示
face_image_rgb = cv2.cvtColor(face_image, cv2.COLOR_BGR2HSV)

# 图片的二值化处理
# 红底变蓝底
# 将在两个阈值内的像素值设置为白色（255），而不在阈值区间内的像素值设置为黑色（）
lower_blue = np.array([90, 70, 70])
upper_blue = np.array([110, 255, 255])
face_image_rgb = cv2.inRange(face_image, lower_red, upper_red)

cv2.imshow("output.png", face_image_rgb)

for i in range(rows):
    for j in range(cols):
        imageinfo = face_image_rgb[i][j]
        print(imageinfo)
        break;

# 展示图像
# cv2.imshow("output.png", face_image_rgb)

# 防止闪退
cv2.waitKey(0)
