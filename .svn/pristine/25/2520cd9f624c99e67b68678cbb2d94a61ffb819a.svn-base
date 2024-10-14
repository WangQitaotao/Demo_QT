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

from common.logger_handler import GetLogger

# 禁用 SSL 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
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

def search_kosmetika(st_filter, search_term):
    url = "https://cekbpom.pom.go.id/search_kosmetika"
    data = {
        "st_filter": st_filter,
        "input_search": search_term
    }
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

    try:  # 尝试不使用代理
        proxies = {
            "http": None,
            "https": None,
        }
        # 禁用 SSL 验证仅用于调试
        response = requests.post(url, data=data, headers=headers, verify=False, timeout=30, proxies=proxies)
        response.raise_for_status()  # Raises HTTPError for bad responses
        # 解析 JSON 数据
        return json.loads(response.text)

    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        return None

def prev_next_pagination_kosmetika(st_filter, search_term, offset, next_prev):

    url = "https://cekbpom.pom.go.id/prev_next_pagination_kosmetika"
    data = {
        "st_filter": st_filter,
        "input_search": search_term,
        "offset": offset,
        "next_prev": next_prev,
        "count_data_kosmetika": "4709",
        "marked": "next"
    }
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,en-GB;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'webreg=9ur7cjvnsskauhpphutu08aiv3nepbk3',  # 替换为实际的Cookie值
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

    try:  # 尝试不使用代理
        proxies = {
            "http": None,
            "https": None,
        }
        # 禁用 SSL 验证仅用于调试
        response = requests.post(url, data=data, headers=headers, verify=False, timeout=30, proxies=proxies)
        response.raise_for_status()  # Raises HTTPError for bad responses
        # 解析 JSON 数据
        return json.loads(response.text)

    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        return None


def get_product_details(product_id, application_id):
    url = "https://cekbpom.pom.go.id/get_detail_produk_obat"
    data = {
        "product_id": product_id,
        "aplication_id": application_id
    }
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
    # 禁用 SSL 验证仅用于调试
    response = requests.post(url, data=data, headers=headers, verify=False, timeout=30, proxies=proxies)
    response.raise_for_status()  # Raises HTTPError for bad responses
    # 解析 JSON 数据
    return parse_html(response.text)


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


def append_to_csv(csv_file, fieldnames, data_dict):
    try:
        file_exists = os.path.isfile(csv_file)
        with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(data_dict)
    except:
        pass

def append_results_to_csv(results):
    for get_product_details_data in results:
        append_to_csv(csv_file, fieldnames, get_product_details_data)


def process_page(i, start, range_size, st_filter, filter_fields):
    try:
        GetLogger().debug(f"执行第 {i+1} 页")
        random_int = random.randint(1, 10)
        time.sleep(random_int)
        range_start = start + i * range_size
        range_end = range_start + range_size - 1
        data = prev_next_pagination_kosmetika(st_filter, filter_fields, range_start, range_end)
        # print(f"data: {data}")
        results = []
        for j in range(10):
            get_product_details_data = get_product_details(data["data_kosmetika"][j]["PRODUCT_ID"], data["data_kosmetika"][j]["APPLICATION_ID"])
            # print(f"获取到html{get_product_details_data}")
            if get_product_details_data:
                results.append(get_product_details_data)
        return results
    except Exception as e:
        GetLogger().error(f"处理第 {i+1} 页数据时出错: {e}, 跳过该页...")
        time.sleep(60)
        return []


def get_csv_file_path():
    # 获取当前时间，并格式化为 YYYYMMDD_HHMMSS 格式
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # 设置默认文件路径，使用时间戳替换 "demo"
    default_path = f"D:\\{timestamp}.csv"
    # 提示用户输入路径，如果用户没有输入，则使用默认路径
    user_input = input(f"请输入存放数据的完整路径 (默认: {default_path}): ")
    # 如果用户没有输入路径，则使用默认路径
    csv_file = user_input.strip() if user_input.strip() else default_path
    return csv_file

if __name__ == '__main__':

    start = 1
    range_size = 10
    # csv_file = 'perfume.csv'  # 生成的csv地址
    # st_filter = 2   # 这里是下拉选项的内容
    # filter_fields = "perfume"   # 这里是筛选条件
    # data = search_kosmetika(st_filter, filter_fields)   # 获取有多少条数据
    print("------------------->  爬取 https://cekbpom.pom.go.id 数据  <-------------------")
    csv_file = get_csv_file_path()
    st_filter = input("""
Nomor Registrasi	1
Nama Produk         2
Merk                3
Jumlah & Kemasan	4
Bentuk Sediaan		5
Komposisi           6
Nama Pendaftar	    7

请输入下拉框中的选项(输入数字): """)
    filter_fields = input("请输入筛选条件(没有筛选条件就直接Enter): ")   # 这里是筛选条件
    data = search_kosmetika(st_filter, filter_fields)   # 获取有多少条数据
    print(f"该选项共有 {data['count_data_kosmetika']['JUMLAH']} 条数据")

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # 提交任务到线程池
        futures = [executor.submit(process_page, i, start, range_size, st_filter, filter_fields) for i in range(1, data['count_data_kosmetika']['JUMLAH']// 10)]
        # 处理每个页面的结果
        for future in concurrent.futures.as_completed(futures):
            results = future.result()
            append_results_to_csv(results)
    print("")
    print("执行完成。请点击回车或直接关闭窗口")
    print(input(""))