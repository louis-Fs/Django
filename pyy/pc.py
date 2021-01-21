import urllib.request
import re
import random
#user-agent pools qq,firefox,chorme,ie
uapools=[
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    ]
def ua():
    opener=urllib.request.build_opener()
    this_ua=random.choice(uapools)
    u_a=('User-Agent',this_ua)
    opener.addheaders=[u_a]
    urllib.request.install_opener(opener)
def data():#爬取短新闻
    ua()
    url='http://www.scu.edu.cn/'
    date=[]
    data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
    pat='<ul class="news-list">(.*?)</ul>'
    rst=re.compile(pat,re.S).findall(data)
    pat1='<li>(.*?)</li>'
    rst1=re.compile(pat1,re.S).findall(str(rst[0]))
    pat_href='href="(.*?)"'
    pat_title='title="(.*?)"'
    pat_data='<span class="date">(.*?)</span>'
    rst_href=re.compile(pat_href,re.S).findall(str(rst1))
    rst_title=re.compile(pat_title,re.S).findall(str(rst1))
    rst_data=re.compile(pat_data,re.S).findall(str(rst1))
    for i in range(0,len(rst_href)):
        dic={}
        dic['href']=url+rst_href[i]
        dic['title']=rst_title[i]
        dic['data']=rst_data[i]
        date.append(dic)
    return date
def data1():#爬取含图片的新闻
    ua()
    url = 'http://www.scu.edu.cn/'
    date = []
    data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
    pat = '<div class="card"(.*?)</div>'
    rst1 = re.compile(pat, re.S).findall(data)
    #print(rst1)
    pat_href='href="(.*?)"'
    pat_title='title="(.*?)"'
    pat_data='data-original="/(.*?)"'
    rst_href=re.compile(pat_href,re.S).findall(str(rst1))
    rst_title=re.compile(pat_title,re.S).findall(str(rst1))
    rst_data=re.compile(pat_data,re.S).findall(str(rst1))
    for i in range(0,len(rst_href)):
        dic={}
        dic['hre_f']=url+rst_href[i]
        dic['titl_e']=rst_title[i]
        dic['pic_url']=url+rst_data[i]
        date.append(dic)
    return date
def data2():#爬取轮播图片
    ua()
    url = 'http://www.scu.edu.cn/'
    date = []
    data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
    pat = '<div class="silder-main-img">(.*?)</div>'
    rst1 = re.compile(pat, re.S).findall(data)
    #print(rst1)
    pat_href='href="(.*?)"'
    pat_title='title="(.*?)"'
    pat_data='data-org="/(.*?)"'
    rst_href=re.compile(pat_href,re.S).findall(str(rst1))
    rst_title=re.compile(pat_title,re.S).findall(str(rst1))
    rst_data=re.compile(pat_data,re.S).findall(str(rst1))
    for i in range(0,len(rst_href)):
        dic={}
        dic['hre_f']=url+rst_href[i]
        dic['titl_e']=rst_title[i]
        dic['pic_url']=url+rst_data[i]
        date.append(dic)
    return date
