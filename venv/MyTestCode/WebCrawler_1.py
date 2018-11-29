from requests_html import HTMLSession
import pandas as pd

# 建立一个会话（session），即让Python作为一个客户端，和远端服务器交谈
url = 'https://www.jianshu.com/p/85f4624485b9'
session = HTMLSession()

# 利用 session 的 get 功能，把这个链接对应的网页整个儿取回来
r = session.get(url)

# 打印出返回的HTML中的文字部分
# print(r.html.text)
# 打印出返回的HTML中的绝对链接部分
# print(r.html.absolute_links)

# 定位我们具体要获取的元素HTML相对位置
sel = 'body > div.note > div.post > div.article > div.show-content > div > p > a'

# 获取链接和文字的步骤， 作为一个重复性的动作通过定义一个函数来实现
def get_text_link_from_sel(sel):
    mylist = []
    try:
        results = r.html.find(sel)
        for result in results:
            mytext = result.text
            mylink = list(result.absolute_links)[0]
            mylist.append((mytext, mylink))
        return mylist
    except:
        return None

# 通过Pandas把数据转换为数据表
df = pd.DataFrame(get_text_link_from_sel(sel))
# 定义数据表的表头
df.columns = ['Text', 'Link']
# 导出到Excel文件, utf_8_sig以防中文乱码
df.to_csv('Output\Sample.csv', encoding='utf_8_sig', index=False)

