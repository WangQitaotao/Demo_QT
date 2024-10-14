import datetime
import os
import random
import time
import concurrent.futures
import requests
import json
import logging
import csv
import urllib3
from bs4 import BeautifulSoup
# 禁用 SSL 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,en-GB;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'webreg=nfnuhaf6k405ekv1t6593qa6kduul6ac',  # 注意这里需要替换为您实际的Cookie值
    'Host': 'cekbpom.pom.go.id',
    'Origin': 'https://cekbpom.pom.go.id',
    'Referer': 'https://cekbpom.pom.go.id/kosmetika',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

proxies = {
    "http": None,
    "https": None,
}

fieldnames = [
    'Nomor_Registrasi',
    'Tanggal_Terbit',
    'Diterbitkan_Oleh',
    '',
    'Produk',
    'Nama_Produk',
    'Bentuk_Sediaan',
    'Merk',
    'Kemasan',
    'Pendaftar',
    '1._Industri_Kosmetika',
    '2._Industri_Kosmetika',
    '3._Industri_Kosmetika'
]
def parse_html(html):
    if html is None:
        logging.error("No HTML data to parse.")
        return {}
    soup = BeautifulSoup(html, 'lxml')  # 使用 lxml 解析器
    data = {}
    rows = soup.find_all('tr')
    for row in rows:
        caption = row.find('td', class_='form-field-caption')
        value = row.find('td', class_='form-field-input')
        if caption and value:
            key = caption.get_text(strip=True).replace(' ', '_').replace(':', '')  # 制作字段键
            value_text = value.find('span').get_text(strip=True) if value.find('span') else value.get_text(strip=True)
            data[key] = value_text
    return data

def search_kosmetika(st_filter, search_term):
    """获取数据"""
    url = "https://cekbpom.pom.go.id/search_kosmetika"
    data = {
        "st_filter": st_filter,
        "input_search": search_term
    }
    response = requests.post(url, data=data, headers=headers, verify=False, timeout=30, proxies=proxies)
    url2 = "https://cekbpom.pom.go.id/prev_next_pagination_kosmetika"
    data2 = {
        "st_filter": json.loads(response.text)["offset"],
        "input_search": json.loads(response.text)["next_prev"],
        "offset": 1,
        "next_prev": 10,
        "count_data_kosmetika": "4709",
        "marked": "next"
    }
    response2 = requests.post(url2, data=data2, headers=headers, verify=False, timeout=30, proxies=proxies)
    response2_data = json.loads(response2.text)
    print(f"该选项共有 {json.loads(response.text)['count_data_kosmetika']['JUMLAH']} 条数据")
    # for i in range(1, len(response2_data)):
    #     for j in range(10):
    #         url3 = "https://cekbpom.pom.go.id/get_detail_produk_obat"
    #         data3 = {
    #             "product_id": response2_data["data_kosmetika"][j]["PRODUCT_ID"],
    #             "aplication_id": response2_data["data_kosmetika"][j]["APPLICATION_ID"]
    #         }
    #         response3 = requests.post(url3, data=data3, headers=headers, verify=False, timeout=30, proxies=proxies)
    #         print(parse_html(response3.text))


if __name__ == '__main__':
    search_kosmetika(1, "")
