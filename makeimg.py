from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import datetime
import time
import news
import weather

def get_week_day(date):
  week_day_dict = {
    0 : '星期一',
    1 : '星期二',
    2 : '星期三',
    3 : '星期四',
    4 : '星期五',
    5 : '星期六',
    6 : '星期天',
  }
  day = date.weekday()
  #get_week_day(datetime.datetime.now())
  return week_day_dict[day]

def strprint(str1,lenstr,x,y,draw,ttfont):
    print(str1)
    str2=''
    if len(str1) > lenstr:
        for i in range((len(str1)//lenstr)+1):
            str1=list(str1)
            str2=''
            for a in range(lenstr):
                try:
                    str2=str2+str1.pop(0)
                except IndexError:
                    pass
                #print(str2)
            str2=str2.replace('，',',')
            str2=str2.replace('。','.')
            str2=str2.replace('！','!')
            str2=str2.replace('？','?')
            print(str2)
            draw.text((x,y+i*15),str2,fill=(0,0,0),font=ttfont)
                #draw.text((x+i*15,y),str(str1[i]),fill=(0,0,0),font=ttfont)

def make_image():
    print('开始制作图片')
    qr, new,come_from = news.get()
    data = weather.get()
    #qr,new = news.get()
    smallfont = ImageFont.truetype('./图片/font.ttf', 15)
    ttfont = ImageFont.truetype('./图片/font.ttf', 15)
    nonafont = ImageFont.truetype('./图片/font.ttf', 20)
    bigfont = ImageFont.truetype('./图片/font.ttf', 35)
    img = Image.open('./图片/img.png')

    draw = ImageDraw.Draw(img)

    img.paste(qr, (0, 0), mask=None)
    draw.text((74, 5), '每日热点:', fill=(0, 0, 0), font=ttfont)
    draw.text((85, 25), str(new), fill=(0, 0, 0), font=ttfont)
    draw.text((270,45),str(come_from),fill=(0,0,0),font=ttfont)


    draw.text((170,70),time.strftime("%H:%M"),fill=(0,0,0),font=bigfont)#时间
    draw.text((135,110),str(datetime.date.today()),fill=(0,0,0),font=ttfont)#日期
    draw.text((223,109),str(get_week_day(datetime.datetime.now())),fill=(0,0,0),font=ttfont)

    img.paste(Image.open('./图片/icon/'+data['now']['icon']+'.png'), (104, 73), mask=None)
    #星期
    #draw.text((1,75),'当前城市:',fill=(0,0,0),font=smallfont)
    img.paste(Image.open('./图片/icon/1.png'), (1, 78), mask=None)
    draw.text((18,70),data['city']+'/'+data['now']['text'],fill=(0,0,0),font=nonafont)
    #draw.text((1,92),'当前温/湿度:',fill=(0,0,0),font=smallfont)
    img.paste(Image.open('./图片/icon/2.png'), (1, 97), mask=None)
    draw.text((18,90),str(data['now']['temp']+'°C/'+data['now']['humidity']+'%'),fill=(0,0,0),font=nonafont)
    draw.text((170,130),str(data['weather'][0]['tempMax'])+'°C/'+str(data['weather'][0]['tempMin'])+'°C',fill=(0,0,0),font=ttfont)

    img.paste(Image.open('./图片/icon/3.png'), (1, 117), mask=None)
    draw.text((23,110),data['now']['windScale']+'级'+data['now']['windDir'],fill=(00,0,0),font=nonafont)
    #draw.text((0,185),'当前风是'+data['now']['windDir']+',速度为'+data['now']['windSpeed']+'km/h'+'是'+data['now']['windScale']+'级风',fill=(00,0,0),font=ttfont)

    img.paste(Image.open('./图片/icon/4.png'), (1, 137), mask=None)
    draw.text((23,130),'空气'+data['air']['category'],fill=(0,0,0),font=nonafont)

    img.paste(Image.open('./图片/icon/5.png'), (1, 155), mask=None)
    draw.text((20,150),data['summary'],fill=(0,0,0),font=nonafont)

    img.paste(Image.open('./图片/icon/6.png'), (1, 178), mask=None)
    draw.text((23,172),data['weather'][0]['sunrise'],fill=(0,0,0),font=nonafont)
    img.paste(Image.open('./图片/icon/7.png'), (70, 178), mask=None)
    draw.text((90,172),data['weather'][0]['sunset'],fill=(0,0,0),font=nonafont)

    img.paste(Image.open('./图片/icon/8.png'), (1, 205), mask=None)
    draw.text((23,196),data['weather'][0]['moonrise'],fill=(0,0,0),font=nonafont)
    img.paste(Image.open('./图片/icon/9.png'), (70, 205), mask=None)
    draw.text((90,196),data['weather'][0]['moonset'],fill=(0,0,0),font=nonafont)


    draw.text((0,220),data['life']['name']+':'+data['life']['category'],fill=(0,0,0),font=ttfont)

    strprint(str1=data['life']['text'],lenstr=18,x=15,y=235,draw=draw,ttfont=ttfont)
    #strprint(str1='娃娃娃娃娃娃娃娃啊哇娃娃娃娃娃娃娃娃啊哇娃娃娃娃娃娃娃娃啊哇娃娃娃娃娃娃娃娃啊哇',lenstr=18,x=15,y=235,draw=draw,ttfont=ttfont)
    draw.text((0,280),'QQ机器人:3402963150',fill=(0,0,0),font=ttfont)

    plt.figure("img")
    print('图片制作完成')
    return img

if __name__ == '__main__':

    img = make_image()
    plt.imshow(img)
    plt.show()
'''
from PIL import Image

path = "C:/Users/Administrator/Desktop/QRCode/background.jpg"#母图详细文件名以及路径
img = Image.open(path)
# img = qr.make_image(fill_color="#555555", back_color="Red")
img = img.convert("RGBA")  # CMYK/RGBA 转换颜色格式（CMYK用于打印机的色彩，RGBA用于显示器的色彩）
# 添加子图
icon = Image.open("C:/Users/Administrator/Desktop/QRCode/zitu.png")#子图文件名
# 获取图片的宽高
img_w, img_h = img.size#获取被放图片的大小（母图）
icon_w,icon_h=icon.size#获取小图的大小（子图）
factor = 6
size_w = int(img_w / factor)
size_h = int(img_h / factor)
icon_w, icon_h = icon.size
#防止子图尺寸大于母图
if icon_w > size_w:
    icon_w = size_w
if icon_h > size_h:
    icon_h = size_h
# # 重新设置子图的尺寸
# icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
w = int((img_w - icon_w) / 2)
h = int((img_h - icon_h) / 2)
# 粘贴图片
img.paste(icon, (w, h), mask=None)
# 保存图片
img.save("C:/Users/Administrator/Desktop/QRCode/c.png")#合成后的图片路径以及文件名
'''
