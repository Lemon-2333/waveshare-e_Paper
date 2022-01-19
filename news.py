import requests
import bs4
import re
import qrcode
import random


def get():
    print('开始获取新闻')
    url_1 = r"https://s.weibo.com/top/summary?cate=realtimehot"  # 热搜
    url_3 = r"https://s.weibo.com/top/summary?cate=socialevent"  # 要闻
    url_2 = r"https://s.weibo.com/"

    headers = {
        'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': r'__guid=162520830.1282114399446370000.1611893501570.244; _s_tentry=www.so.com; UOR=www.so.com,s.weibo.com,www.so.com; Apache=1804726746613.3188.1611893502740; SINAGLOBAL=1804726746613.3188.1611893502740; ULV=1611893502912:1:1:1:1804726746613.3188.1611893502740:; WBStorage=8daec78e6a891122|undefined; monitor_count=4',
        'Host': 's.weibo.com',
        'Referer': r'https://s.weibo.com/top/summary?cate=socialevent',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }
    temp = random.randint(0, 1)
    temp = 1
    if random.randint(0, 1) == 0:
        print('选择热搜')
        res = requests.get(url_1, headers=headers)
        res = re.findall(
            '<a href="(\S+Refer=top)"\starget="_blank">(\S+)</a>', res.text)
        come_from='来自微博热搜'
    else:
        print('选择要闻')
        res = requests.get(url_3, headers=headers)
        res = re.findall(
            '<a href="(\S+)"\starget="_blank">(\S+)</a>', res.text)
        come_from = '来自微博要闻'
    # print(res.text)
    # soup=bs4.BeautifulSoup(res.text,"html.parser")

    # print(res)
    num = random.randint(0, len(res))
    # print(num)
    #print(res)
    #print(num)
    try:
        temp = url_2+str(res[num][0])
    except IndexError:
        num=num-1
        temp = url_2+str(res[num][0])
    '''
    print(temp)
    print(1111111111)
    print(temp[0])
    '''
    qr = qrcode.make(temp)
    qr.thumbnail((71, 71))
    # qr.show()
    print('新闻获取成功')
    return qr, res[num][1].replace('#',''),'——'+come_from


if __name__ == '__main__':
    times = 0
    while True:
        times = times+1
        qr, new = get()
        print('times:')
        print(times)
