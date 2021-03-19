import requests
from lxml import etree
from pytypecho import Typecho,Post
import time
from datetime import datetime
import ssl
 
ssl._create_default_https_context = ssl._create_unverified_context


# 2021-03-04-11-59

# http://www.mxqe.com/bnj/54600.html
# /html/body/div[5]/div[1]/h1


def upload(title,categories_data,keywords,data):
	try:
		te = Typecho('https://anshub.top/index.php/action/xmlrpc', username='admin', password='434d58')
		# post = Post(title=title, categories = ['Test'],description=data)
		post = Post(title=title, categories = [categories_data],mt_keywords = keywords,description=data)
		te.new_post(post, publish=True) 
		print("[4/4] Data Uploaded \033[1;32mSuccessfully \033[0m")
		#time.sleep(5)#休息5秒
	except:
		print("\033[1;31mUpload failed!\033[0m")

def info():
	categories_data=''
	keywords=""
	year = datetime.now().year
	if 'qnj' in url:
		categories_data="七年级"
	if 'bnj' in url:
		categories_data="八年级"
	if 'jnj' in url:
		categories_data="九年级"
		
	if "语文" in html_title[0]:
		keywords+="语文, "
	if "数学" in html_title[0]:
		keywords+="数学, "
	if "英语" in html_title[0]:
		keywords+="英语, "
	if "科学" in html_title[0]:
		keywords+="科学, "
	if "道德与法治" in html_title[0]:
		keywords+="道德与法治, "
	if "历史与社会" in html_title[0]:
		keywords+="历史与社会, "
	try:	
		for i in range(-3,3):
			if str(year-i) in html_title[0]:
				keywords+=(str(year-i))
	except:
		print("\033[1;33mWarning! \033[0m-The Ans is Too Old or The year is not indicated\nAction-Discard year tag.")
	
	return categories_data,keywords


def get(url):
	global data,html_title
	data = ''
	down_url = 'http://pic.mxqe.com'
	header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	          'Accept-Encoding': 'gzip, deflate',
	          'Accept-Language': 'zh-cn',
	          'Host': 'www.mxqe.com',
	          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
	          }
	try:          
		html = requests.get(url, headers=header)
		html.encoding='utf-8'
		html = etree.HTML(html.text)
		html_data = html.xpath('//html/body/div[5]/div[1]/div[1]/p/img//@src')
		html_title = html.xpath('//html/body/div[5]/div[1]/h1/text()')
		print("[2/4] Data Received \033[1;32mSuccessfully \033[0m")
	except:
		print("\033[1;31m[2/4] Data receiving failed\033[0m")
		return 1
	for i in range(len(html_data)):
		if "www.mxqe.com" in html_data[i]:
			pic_url=html_data[i]
		else:
			pic_url=down_url+html_data[i]
		#print("!["+str(i)+"]("+pic_url+" '"+str(i)+"')")
		data+=("!["+str(i)+"]("+pic_url+" '"+str(i)+"')\n")
	#print(data)
	data+=('From: '+url)
	print("[3/4] Data Analysis \033[1;32mCompleted \033[0m")
	upload(str(html_title[0]),info()[0],info()[1],data)


url = input("[1/4] Input The URL: ")
get(url)