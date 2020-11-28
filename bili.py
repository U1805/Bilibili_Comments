import random
from getHTML.fetch import fetchURL
from putCSV.write import writePage
from getComment.get import parserHtml,isEmpty,getPage
from tqdm import *


def hlist():
	commentlist = []
	hlist = []

	hlist.append("用户名")
	hlist.append("性别")
	hlist.append("时间")
	hlist.append("评论")
	hlist.append("点赞数")
	hlist.append("回复数")
	hlist.append("av号")

	commentlist.append(hlist)
	writePage(commentlist)

def Bv2Av(bv):
	url = "https://api.bilibili.com/x/web-interface/view?bvid=" + bv
	s = fetchURL(url)
	return s["data"]["aid"]

def Av2Bv(av):
	url = "https://api.bilibili.com/x/web-interface/view?bvid=" + av
	s = fetchURL(url)
	return s["data"]["bvid"]

n=20000

if __name__ == '__main__':
	num = 0
	hlist()
	av = random.sample(range(26600000,91000000),n)
	for i in tqdm(range(n)):
		url = 'https://api.bilibili.com/x/v2/reply?type=1&oid=' + str(av[i]) + '&pn=1'
		print('\n')	
		if isEmpty(url) == 1:
			print('av'+ str(av[i])+'下载失败×')	
		else:
			page = getPage(str(av[i]))
			
			for page in range(1,page+1):
				url = 'https://api.bilibili.com/x/v2/reply?type=1&oid=' + str(av[i]) + '&pn=' + str(page)
				parserHtml(url,av[i])
			num = num +1
			print('av'+ str(av[i])+'下载成功○' + "\t下载数：" + str(num))
		print('---'*20)
	print("下载率："+num/n*100+"%")
	
