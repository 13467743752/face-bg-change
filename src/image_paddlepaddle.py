import paddlehub as hub
import os
import numpy as np
import paddle
import cv2
import face_recognition
import json
import uuid
import base64

seg = hub.Module(name='deeplabv3p_xception65_humanseg')


def img_load(obj):
    # bytearray = obj.read()
    # img = Image.open(obj.stream)
    # img = np.asarray(img)
    # img = Image.open(obj)

    result = {
        "flag": False,
        "msg": ""
    }
    img = cv2.imdecode(np.frombuffer(obj.read(), np.uint8), cv2.IMREAD_COLOR)
    # 图片数据
    rows, cols, channels = img.shape  # rows:横向像素cols:纵向像素
    # 128维的五官数据
    # face_encoding = face_recognition.face_encodings(img)
    # 人脸位置
    face_locations = face_recognition.face_locations(img)
    # 判断人脸数量
    n = len(face_locations)
    if n > 1:
        result['msg'] = "图片中只能有一张人脸"
        return result
    face_location = face_locations[0]
    top, right, bottom, left = face_location
    # # 画框             图像                  位置          颜色     粗细
    # cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
    # # 写字
    # cv2.putText(img, "test", (left, top), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0, 2))

    # img = img[int(top/2):bottom*2, int(left/2):right*2] 626×413
    w = int((right - left) / 2.5)
    left = left - w
    right = right + w

    h = int((bottom - top) / 2 * 1.3)
    top = top - h
    bottom = int(top + w * 4 * 1.4)

    if top < 0:
        top = 0
    if bottom > rows:
        bottom = rows
    if left < 0:
        left = 0
    if right > cols:
        right = cols
    img = img[top: bottom, left:right]
    img = cv2.resize(img, (413, 579), interpolation=cv2.INTER_AREA)
    img = seg.segmentation(images=[img], visualization=True,
                           output_dir='D:\\WorkSpace\\Git\\python-tool\\image-del-project\\image')
    img_path = img[0]['save_path']

    with open(img_path, 'rb') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream).decode()
    os.remove(img_path)
    result['flag'] = True
    result['msg'] = img_stream
    return result

# path = 'D://234.png'
# seg.segmentation(paths=[path], visualization=True, output_dir="D://output")
