from getHTML.fetch import fetchURL
from putCSV.write import writePage
import requests
import time
import json

def parserHtml(url,av):#得到评论
	s = fetchURL(url)
	
	commentlist = []
	s.setdefault('data',{'replies':'0'})
	#用户名，性别，时间，评价，点赞数，回复数
	if (s['data']['replies'] == None):
			comment = []
	else:
		for i in range(0,len(s['data']['replies'])-1):
			comment = s['data']['replies'][i]
			blist = []
			username = comment['member']['uname']
			sex = comment['member']['sex']
			ctime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(comment['ctime']))
			content = comment['content']['message']
			likes = comment['like']
			rcounts = comment['rcount']
		

			blist.append(username)
			blist.append(sex)
			blist.append(ctime)
			blist.append(content)
			blist.append(likes)
			blist.append(rcounts)
			blist.append(str(av))

			commentlist.append(blist)

	writePage(commentlist)

def getPage(av):#评论页数
	url = 'https://api.bilibili.com/x/v2/reply?type=1&oid=' + str(av) + '&pn=1'
	s = fetchURL(url)
	count = s['data']['page']['count']
	size = s['data']['page']['size']
	page = (count+(size-0.0001))//size
	return int(page)

def isEmpty(url):
    s=fetchURL(url)
    if(s['data']==None):
        return 1
    else:
        if(s['data']['replies']==None or s['data']['page']['count']== 1 ):
            return 1
        else:
            return 0