import requests
import time
import json

def fetchURL(url, retry_times=5):#下载页面
	headers = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
	}
	
	try:
		html = requests.get(url,headers=headers)
		r= json.loads(html.text)
		return r
	except (requests.RequestException,requests.HTTPError) as e:
		print("Download Error !")
		time.sleep(5)
		if retry_times>0:
			return fetchURL(url,retry_times=retry_times-1)
	except:
		print("Unknown Error !")
		time.sleep(5)
		if retry_times>0:
			return fetchURL(url,retry_times=retry_times-1)