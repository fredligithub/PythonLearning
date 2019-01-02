import webbrowser
import requests
# webbrowser.open('http://www.baidu.com')

result = requests.get('http://www.baidu.com')
print(result.status_code)
print(len(result.text))
print(result.text[1:500])
