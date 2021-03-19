import requests
from lxml import etree

#获取cpolar链接

def newget():
	global html_data,html
	try:
		global html_data,html
		MySession = requests.session()
		header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			          'Accept-Encoding': 'gzip, deflate, br',
			          'Accept-Language': 'zh-cn',
			          'Host': 'dashboard.cpolar.com',
			          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
			          }
		postUrl = 'https://dashboard.cpolar.com/login'
		url = 'https://dashboard.cpolar.com/status'
		postData = {
		        "login": "2931267601@qq.com",
		        "password": "20070223cmx",
		      }
		responseRes = MySession.post(postUrl, data = postData, headers = header)
		print(f"statusCode = {responseRes.status_code}")
		html = etree.HTML(MySession.get(url, headers = header, allow_redirects = False).text)
		html_data = html.xpath('//*[@id="dashboard"]/div/div[2]/div[2]/table/tbody/tr[1]/th/a')
		#print(html_data)
		for i in html_data:
			print(i.text)
	except:
		newget()
	    
newget()