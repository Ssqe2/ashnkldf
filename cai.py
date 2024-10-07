import requests
import time
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Host": "www.scimeeting.cn",
}

cookies={
    "MEDCONSERVERID":"d0f0a469ab1a7b12a6a252e3bf441fed",
    "__jsluid_s":"571d3027eb4afcd68ab07e68ffa7187a"
}
for i in range(1,100):  
    r=requests.get("https://www.scimeeting.cn/cn/person-detail/380?user_id=up2zhGJYvrLdHxK_xNNRVgg_d_d#:~:text=%E8%94%A1%E8%89%AF%E8%8B%91%20%E6%B5%99%E6%B1%9F%E5%A4%A7%E5%AD%A6",cookies=cookies,headers=headers)
    print(i)
    print(r.status_code)
    time.sleep(3)