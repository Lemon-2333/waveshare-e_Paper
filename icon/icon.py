import cv2

# 修改透明背景为白色


def transparence2white(img):
    sp = img.shape  # 获取图片维度
    width = sp[0]  # 宽度
    height = sp[1]  # 高度
    for yh in range(height):
        for xw in range(width):
            color_d = img[xw, yh]  # 遍历图像每一个点，获取到每个点4通道的颜色数据
            if(color_d[3] == 0):  # 最后一个通道为透明度，如果其值为0，即图像是透明
                img[xw, yh] = [255, 255, 255, 255]  # 则将当前点的颜色设置为白色，且图像设置为不透明
    return img


for i in [1,2,3,4,5,6,7,8,9,100, 101, 102, 103, 104, 150, 153, 154, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 350, 351, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 456, 457, 499, 500, 501, 502, 503, 504, 507, 508, 509, 510, 511, 512, 513, 514, 515, 900, 901, 999]:
    print(i)
    imgfile = './图片/icon/'+str(i)+'.png'
    img = cv2.imread(imgfile, -1)
    # img=cv2.imread(‘bar.png‘,-1)  # 读取图片。-1将图片透明度传入，数据由RGB的3通道变成4通道
    img = transparence2white(img)  # 将图片传入，改变背景色后，返回
    cv2.imwrite(imgfile, img)  # 保存图片，文件名自定义，也可以覆盖原文件

# img.save(imgfile)  # 保存图片
