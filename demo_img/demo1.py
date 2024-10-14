# -*- encoding: utf-8 -*-
'''
@时间 ： 2024/8/13 14:21
@作者 ： WangQitao
@名称 ： get_img_netnr.py
@描述 ：
'''
import re
import sys
import os
import time
from urllib.parse import urlparse, parse_qs
import requests
import concurrent.futures
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))


"""
https://ss.netnr.com/wallpaper
"""

options_dict = {
    "": "最新壁纸",
    "36": "4K专区",
    "6": "美女模特",
    "30": "爱情美图",
    "9": "风景大片",
    "15": "小清新",
    "26": "动漫卡通",
    "11": "明星风尚",
    "14": "萌宠动物",
    "5": "游戏壁纸",
    "12": "汽车天下",
    "10": "炫酷时尚",
    "22": "军事天地",
    "16": "劲爆体育",
    "32": "纹理",
    "35": "文字控",
    "29": "月历壁纸",
    "7": "影视剧照",
    "13": "节日美图",
    "18": "BABY秀"
}


def download_image(img_url, filename):
    """下载图片到本地"""
    parsed_url = urlparse(url)    # 解析获得cid参数
    query_params = parse_qs(parsed_url.query)
    cid = str(query_params.get('cid', [None])[0])
    if cid in options_dict:
        directory = fr'T:\爬虫\img\Netnr\{options_dict[cid]}'
        file_path = os.path.join(directory, filename + '.jpg')
        if not os.path.exists(directory):   # 判断文件夹是否存在
            os.makedirs(directory)
        if os.path.exists(file_path):   # 判断图片是否存在
            print(f"该照片存在，跳过:   {file_path}")
        else:
            response = requests.get(img_url, stream=True, timeout=10)
            if response.status_code == 200:
                with open(file_path, 'wb') as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                print(f"下载成功:   {file_path}")
            else:
                print(f"下载失败:   {cid}")


def get_img_parameter():
    """获取图片的参数，url中count表示照片数量"""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
                for data in response.json()['data']:
                    # print(f"图片名称：{data['utag']}")
                    # print(f"分辨率：{data['resolution']}")
                    # print(f"图片链接：{data['url']}")
                    if 'utag' not in data:
                        exclude_words = {'全部'}
                        pattern = re.compile(r'[\u4e00-\u9fff]+')
                        matches = pattern.findall(data['tag'])
                        filtered_matches = [match for match in matches if match not in exclude_words]
                        chinese_fields = ' '.join(filtered_matches)
                        download_image(data['url'], data['resolution'] + '_' + re.sub(r'[ <>:"/\\|?*]', '_', chinese_fields))
                        time.sleep(0.1)
                    else:
                        download_image(data['url'], data['resolution'] + '_' + re.sub(r'[ <>:"/\\|?*]', '_', data['utag']))
                        time.sleep(0.1)
        else:
            print(f"请求失败，状态码: {response.status_code}")
    except requests.exceptions.Timeout:
        print(f"{url} 请求超时")
    except Exception as e:
        print(f"异常错误{e}")


if __name__ == '__main__':
    # 要想下载不同的照片，修改cid参数
    # int_list = [36, 6, 30, 9, 15, 26, 11, 14, 5, 12, 10, 22, 16, 32, 35, 7, 13, 18]
    # for i in range(len(int_list)):
    url = f"http://wallpaper.apc.360.cn/index.php?c=WallPaper&start=0&count=100&from=360chrome&a=getAppsByCategory&cid=36"
    get_img_parameter()