import re
from bs4 import BeautifulSoup
import urllib.request,urllib.error
from time import sleep
from selenium import webdriver
import random
import lxml
import os
import tqdm as td
import requests


#解析特定的re返回
def reback(html,encode): 
    findre=re.compile(r'<a\s+href="([^"]+)">\s*([^<]+)\s*<time>([^<]+)</time>\s*</a>',re.S) #找到列表模块，生成一个re类，自带re模式，勿在match中重复操作
    # f=open("{}".format(file_path),encoding='{}'.format(encode))
    # data=f.read()
    result=re.findall(findre,str(html))
    # f.close
    return result
#从re中返回列表中处理数据
def get_str_list(reslist : list):
    result=[]
    listlen=len(reslist)
    for i in range(listlen):
        result.append(reslist[i][0])
    return result    
#获取taget标签(暂时无用)
def get_taget_list(reslist : list):
    result=[]
    listlen=len(reslist)
    for i in range(listlen):
        result.append(reslist[i][1]+"_"+reslist[i][2])
    return result    
#将获得的url后缀与头部前缀进行拼接，注意需传入一个url的列表
def urlcat(strlist ,strhead :str):
    strlen=len(strlist)
    findhtm=re.compile(r"[^(,'../].*htm",re.S)
    result=[]
    for i in range(strlen):
        str1=re.search(findhtm,strlist[i])  
        result.append(strhead+'/'+str1.group())
    return result #返回一个url列表                  
#遍历所有的目录页
def urlback(cnt):
    if(cnt==1):
        url="http://jwc.njnu.edu.cn/index/xstz.htm"
        return url
    elif(cnt>1 and cnt<=30):
        url="http://jwc.njnu.edu.cn/index/xstz/{}.htm".format(31-cnt)
        return url
    return "error"
#保存到mysql数据库中
def save_mysql(strlist,reslist,table):
    return 0


# #获取网页html的三种方法
# #selenium方法获取html
# def gethtml(url):
#     #f = open('TEST.html','wb')
#     driver = webdriver.Edge()
#     driver.get(url)
#     driver.implicitly_wait(10)
#     html = driver.page_source
#     cookie_dict = {}
#     print(driver.get_cookies())
#     for cookie in driver.get_cookies():
#         cookie_dict[cookie['name']] = cookie['value']

#     #f.write(html)
#     driver.close()
#     #f.close()   
#     return html

#requests方法获取html
# def gethtmlrequest(url,cookie_dict):
#    f = open('TEST.html','wb')
#     head = {  # 模拟浏览器头部信息
#         "Host": "jwc.nnu.edu.cn",
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
#     }
#     response = requests.get(url, headers=head,cookies=cookie_dict)
#     response.raise_for_status() #若状态码不是200，抛出HTTPError异常
#     response.encoding = response.apparent_encoding  #保证页面编码正确
#     html=response.text
#     f.write(html)
#     f.close()   
#     return html

# #urllib方法获取html
def gethtmlurl(url,cookies):
    head = {  # 模拟浏览器头部信息
        "Host": "jwc.nnu.edu.cn",
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
        "Cookie" : "{}".format(cookies)
    }
    #用户代理
    sleep(random.random())
    request=urllib.request.Request(url,headers=head) 
    html=""
    try:
        reponse=urllib.request.urlopen(request,timeout=10)
        html=reponse.read().decode("UTF-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

#通过BeautifulSoup库方法实现网页文本内容的爬取
def gettxt(html,save_path,taget,yesorno : bool):
    soup=BeautifulSoup(html,'lxml')
    temp1=soup.find('div', attrs={'class':'v_news_content'})
    temp2=soup.find('div', attrs={'class':'news_hd f16 tc'})
    result=""
    result+=temp2.h3.get_text(strip=True)+'\n'+temp2.p.get_text(strip=True)+'\n'
    print("当前文件名字："+result+'\n')
    for p in temp1.find_all("p"):
        result+=p.get_text(strip=True)+'\n'
    if(yesorno): #保存为
        valid_file_name = ''.join("{}.txt".format(temp2.h3.get_text(strip=True)))
        f=open(os.path.normpath(save_path+"\\"+valid_file_name),'w',encoding='utf-8')
        f.write(result)       
        f.close()     
    return result


def main(cookies,savepath):
    for i in range(1,5):
        print(i)
        url=urlback(i)
        html=gethtmlurl(url,cookies)
        firstresult=reback(html,'utf-8')
        strlist1=get_str_list(firstresult)
        strlist=urlcat(strlist1,r"http://jwc.nnu.edu.cn")
        # chart=td.tqdm(range(len(strlist))) #进度条显示 
        # chart.set_description("Processing gettxt{}".format(i))
        for urlde in strlist:
            sleep(1+random.random())
            htmltemp=gethtmlurl(urlde,cookies)
            gettxt(htmltemp,savepath,None,True)
            # chart.update(1)
        del strlist1, strlist   
    print("爬虫运行结束\n")  

#main("Ffvy8doNUuzTS=5DjG2m1otC3nvcvTiSK2e.tSEspHYilwJVfjVfPEvLCYhEbcv4XWJCXAy8KcekU5oct8pH16yPmz6v7bE0w5JVG; JSESSIONID=990DBFE178F4777F04EFC496FE3756E3; Ffvy8doNUuzTT=cw.Q9883C1PmknOKlZ5DgN3r_hF_VjWFYlo5dkiCzlzaIRsXVG1sbFQsGSZgNthOSlB8ZpQ2g65K9kebqL0USZnQBr0veLhkrqI8huMfswZ0G3__3JMMaxDuc5n1pPsBdITFfahXAAM6NmlAqwt2o0mJGpUgcPhVxy74wY4HJsRatIlyHf8SnslYyKG9OZGySzISJyP2zNef_DR0n7XOb4zVDNTpj3M4ZFUyk4xExtdrXvVrLE7wkJbKeMgRC9uTjDavy21r9TE9AcHHzVJJqyPRHLCVvo77UHrp_rgB.NLVZI06raTGHR4KHkGPvsA3DifGWFUhjKkWrxlFmsB9UX0MKvimrUVK2HTdguCt4gE","D:\\aprogamecode\\pyqt\\pyqttest\\data")


