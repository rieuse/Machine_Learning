import json
import re
import requests
import time
from lxml import  etree


headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://bj.5i5j.com/ershoufang/chaoyangqu/n5/',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    # 'Cookie': 'acw_tc=AQAAAKSlm1lS3gMAV7Hzcq1u5ds9qEfQ; PHPSESSID=s4nsqnh1q915qjiqk5oebs9ane; domain=bj; yfx_c_g_u_id_10000001=_ck18012923175312917768627129657; yfx_mr_n_10000001=baidu%3A%3Amarket_type_cpc%3A%3A%3A%3Abaidu_ppc%3A%3A%25e6%2588%25bf%25e4%25bb%25b7%3A%3A%3A%3A%25E5%258C%2597%25E4%25BA%25AC%25E6%2588%25BF%25E4%25BB%25B7%3A%3Awww.baidu.com%3A%3A60921349053%3A%3A%3A%3A%25E4%25BA%258C%25E6%2589%258B%25E6%2588%25BF%25E9%2580%259A%25E7%2594%25A8%25E8%25AF%258D%3A%3A%25E4%25BA%258C%25E6%2589%258B%25E6%2588%25BF%25E6%2588%25BF%25E6%25BA%2590%3A%3A36%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2Fershoufang%2F; yfx_mr_f_n_10000001=baidu%3A%3Amarket_type_cpc%3A%3A%3A%3Abaidu_ppc%3A%3A%25e6%2588%25bf%25e4%25bb%25b7%3A%3A%3A%3A%25E5%258C%2597%25E4%25BA%25AC%25E6%2588%25BF%25E4%25BB%25B7%3A%3Awww.baidu.com%3A%3A60921349053%3A%3A%3A%3A%25E4%25BA%258C%25E6%2589%258B%25E6%2588%25BF%25E9%2580%259A%25E7%2594%25A8%25E8%25AF%258D%3A%3A%25E4%25BA%258C%25E6%2589%258B%25E6%2588%25BF%25E6%2588%25BF%25E6%25BA%2590%3A%3A36%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2Fershoufang%2F; yfx_key_10000001=%25e6%2588%25bf%25e4%25bb%25b7; _ga=GA1.2.1876173498.1517239082; _gid=GA1.2.1494669946.1517239082; yfx_f_l_v_t_10000001=f_t_1517239073286__r_t_1517239073286__v_t_1517242906771__r_c_0'
}

def get_house_data():
    for num in range(1, 307):
        url = f'https://bj.5i5j.com/ershoufang/chaoyangqu/n{num}/'
        print(url)
        s = requests.session()
        html = s.get(url, headers=headers).text
        content = etree.HTML(html).xpath('//*[@class="listCon"]')
        for item in content:
            desc = item.xpath('./div[1]/p[1]/text()')[0].replace(' ','')
            price = item.xpath('./div[1]/div[1]/p[1]/strong/text()')[0]
            unit_price = item.xpath('./div[1]/div[1]/p[2]//text()')[0][2:-4]
            rooms = desc[:1]
            halls = desc[2:3]
            size = re.search(r'(?<=·).+(?=平米·)', desc)[0]
            direction = re.search(r'(?<=平米·).{1,2}(?=·)', desc)
            if not direction:
                direction = ''
            else:
                direction = direction[0]
            height = re.search(r'(?<=·).{1}(?=楼层)', desc)[0]
            if '装' in desc:
                decoration = desc[-2:-1]
            else:
                decoration = ''
            data = {
                'rooms': rooms,
                'halls': halls,
                'size': size,
                'direction': direction,
                'height': height,
                'decoration': decoration,
                'unit_price': unit_price,
                'price': price
            }
            print(data)
            # data = json.dumps(data, ensure_ascii=False)
            with open('house_price.json', 'a',encoding='utf-8') as f:
                f.write(rooms + ',' + halls + ',' + size + ',' + direction + ',' + height + ',' + decoration + ',' + unit_price + ',' + price + '\n')
        time.sleep(3)

if __name__ == '__main__':
    get_house_data()


