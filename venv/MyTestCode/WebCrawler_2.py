# 亚马逊搜索Microservice并导出返回的书籍列表

from requests_html import HTMLSession
import pandas as pd

# 建立一个会话（session），即让Python作为一个客户端，和远端服务器交谈
session = HTMLSession()
# url = 'https://www.amazon.cn/s/ref=nb_sb_ss_sc_2_11?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Ddigital-text&field-keywords=microservice&sprefix=micro+servi%2Caps%2C179&crid=3C2UDILVF9R14'
url = 'https://www.amazon.cn/s/ref=nb_sb_noss?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Dstripbooks&field-keywords=devops'

# 利用 session 的 get 功能，把这个链接对应的网页整个儿取回来
r = session.get(url)

# 利用Chrome浏览器从页面中找到对应的元素， Copy Selector
sel = ' div > div > div > div.a-fixed-left-grid-col.a-col-right > div.a-row.a-spacing-small > div:nth-child(1) > a > h2'

# 页面上对应的元素有多个， 定义以下函数返回获取元素的列表
def get_text_link_from_sel(sel):
    mylist = []
    try:
        results = r.html.find(sel)
        for result in results:
            mytext = result.text
            mylist.append(mytext)
        return mylist
    except:
        return None

# 导出到Excel文件
df = pd.DataFrame(get_text_link_from_sel(sel))
df.columns = ['Text']
df.to_csv('Output\Amazon_Devops.csv', encoding='utf_8_sig', index=False)
