import requests
import json
import random

def get(city="", adm="重庆"):#city为城市，adm为省级
    info = {}
    city_id = ''
    key = ''#用的和风天气api，请自己获取key
    url_city = "https://geoapi.qweather.com/v2/city/lookup?location=" + \
        city+"&adm="+adm+"&key="+key+"&number=1"
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
    }
    print('开始获取城市ID')
    res=requests.get(url=url_city,headers=headers)
    res=json.loads(res.text)
    print(res)
    res=res['location'][0]
    city_id=res['lon']+','+res['lat']
    print(city_id)
    info['city']=city
    print('已经成功获取城市ID')

    print('开始获取实况天气')
    url = "https://devapi.qweather.com/v7/weather/now?location="+city_id+"&key="+key
    res = requests.get(url=url, headers=headers)
    res = json.loads(res.text)
    info['now'] = res['now']
    print('已经获取实况天气')

    print('开始获取天气预报')
    url = "https://devapi.qweather.com/v7/weather/7d?location="+city_id+"&key="+key
    res = requests.get(url=url, headers=headers)
    res = json.loads(res.text)
    info['weather'] = res['daily']
    print('已经获取天气预报')

    print('开始获取降雨预报')
    url = "https://devapi.qweather.com/v7/minutely/5m?location="+city_id+"&key="+key
    res = requests.get(url=url, headers=headers)
    res = json.loads(res.text)
    info['summary'] = res['summary']
    print('已获取降雨预报')

    print('开始获取空气质量')
    url = "https://devapi.qweather.com/v7/air/now?location="+city_id+"&key="+key
    res = requests.get(url=url, headers=headers)
    res = json.loads(res.text)
    info['air'] = res['now']
    print('已获取空气质量')

    print('开始获取生活指数')
    num=str(random.randint(1,16))
    url = "https://devapi.qweather.com/v7/indices/1d?location="+city_id+"&key="+key+"&type="+num
    res = requests.get(url=url, headers=headers)
    res = json.loads(res.text)
    info['life'] = res['daily'][0]
    print('已获取生活指数')
    return info


if __name__ == '__main__':
    data = get()
    print(json.dumps(data, indent='', ensure_ascii=False))
