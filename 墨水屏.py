'''
此程序及支持微雪esp32或esp8266（未经过测试）墨水屏驱动板

'''

import requests
import random
import numpy as np
from PIL import Image
import time
import re 
#import makeimg 这里是导入的外部脚本文件（暂不提供）用来制作并且返回图片的
import matplotlib.pyplot as plt

num = []
ok = []
temp = ''
ip = r'http://192.168.0.104/'  # 驱动板IP地址
txtfile = 'log.txt'  # log文件用来查看转码后的图片数据的
list_end = []
EPD = r'EPDn_'
'''
EPD这里是用来初始化墨水屏代码的（后面的n就代表黑白的4.2寸墨水屏）
如果要查找自己的墨水屏代码，请自己抓包获取
'''
NEXt = r'NEXT_'
list2 = []
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
}
file = open(txtfile, 'w')

print('开始获取图片')
#imgfile = makeimg.make_image()#利用外部库函数返回已经制作好的图片
imgfile = Image.open('/home/pi/py/python/123.png')#打开本地的图片 注意！请打开符合你墨水屏尺寸的图片
plt.imshow(imgfile)
plt.show()
print("图片获取成功")

def list_of_groups(list_info, per_list_len):  # 分割列表（用于把图片像素4个4个一组的分）
    '''
    :param list_info:   列表
    :param per_list_len:  每个小列表的长度
    :return:
    '''
    list_of_group = zip(*(iter(list_info),) * per_list_len)
    end_list = [list(i) for i in list_of_group]  # i is a tuple
    count = len(list_info) % per_list_len
    end_list.append(list_info[-count:]) if count != 0 else end_list
    return end_list


def img_handle():  # 读取图片像素
    number = 0
    print('开始把图片转换成为数组')
    try:
        img = np.array(Image.open(imgfile), 'i')  # 读取图片，转换为数组，
    except AttributeError:
        img = np.array(imgfile,'i')
    print('已把图片转换成为数组')

    print('开始把数数组二次转换')
    times_1=0
    for i in img:
        if any(i) <= 200:
            n = 0
        else:
            n = 1
            num.append(str(n))
            if number == 400:
                file.write('\n')
                number = 0
            file.write(str(n))
            number = number+1
            '''
            这里的这个过程就类型于手动把图片进行黑白处理
            而 m <= 200 中的200可以根据自己要输出的图片来进行调整
            '''
    print('已完成二次转换')
    return num



def switch():  # 将图片像素数据转换成为字符
    number = 0
    list2 = []
    ok=[]
    print('开始把数组转化成为字符数据')
    for i in list_of_groups(list_info=num, per_list_len=4):
        for n in i:
            file.write(n)
    file.write('\n')

    for i in list_of_groups(list_info=num, per_list_len=4):
        '''
        微雪是用每4位二进制合并为一个字母即0.5B
        '''
        temp = ''.join(i[0:4])

        if temp == '0000':
            temp = 'a'
        elif temp == '0001':
            temp = 'b'
        elif temp == '0010':
            temp = 'c'
        elif temp == '0011':
            temp = 'd'
        elif temp == '0100':
            temp = 'e'
        elif temp == '0101':
            temp = 'f'
        elif temp == '0110':
            temp = 'g'
        elif temp == '0111':
            temp = 'h'
        elif temp == '1000':
            temp = 'i'
        elif temp == '1001':
            temp = 'j'
        elif temp == '1010':
            temp = 'k'
        elif temp == '1011':
            temp = 'l'
        elif temp == '1100':
            temp = 'm'
        elif temp == '1101':
            temp = 'n'
        elif temp == '1110':
            temp = 'o'
        elif temp == '1111':
            temp = 'p'
            
        list2.append(temp)
        if len(list2)==2:
            list2.reverse()
            for i in list2:
                ok.append(i)
            list2=[]
        '''
        这里是把得到的数据，存入list2这个临时列表里面
        并且每2个逆序即字节流内逆序再把数据存入名为ok的临时列表里
        '''
        if number == 100:
            file.write('\n')#写入log文件
            number = 0
#下面这部分就是把ok给切片然后再存入最终列表
    for i in range(30):
        tp = i*1000
        temp = ''
        str1 = ''

        str1 = ''.join(ok[tp:tp+1000])
        list_end.append(str1)
    print('已完成转换')
    return list_end


def end():  # 完成nex通道以及show指令发送
    try:
        requests.get(url=ip+r'NEXT_', headers=headers)
    except requests.exceptions.ConnectionError:
        pass
    for i in range(30):
        try:
            requests.get(url=ip+r'ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppiodaLOAD_', headers=headers)
        except requests.exceptions.ConnectionError:
            pass
    print('第二通道发送完毕')
    try:
        requests.get(url=ip+r'SHOW_')
    except requests.exceptions.ConnectionError:
        pass
    print('全部数据已经发送完毕请检查墨水屏')


def start():  # 初始化屏幕并且发送数据
    print('开始发送')
    try:
        requests.get(url=ip+EPD, headers=headers)
    except requests.exceptions.ConnectionError:
        '''
        为什么要加入try？因为esp32或8266收到数据后闭不会返回值
        而是直接关闭链接所以要用try
        '''
        pass
    for i in list_end:
        try:
            requests.get(url=ip+i+r'iodaLOAD_', headers=headers)
        except:
            pass
    print('第一通道发送完毕')


if __name__ == '__main__':
    img_handle()
    switch()
    start()
    end()
