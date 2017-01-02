import requests
import re
#import you_get


class down_load_movie(object):
    def __init__(self):
      #self.movie_name = movie_name
      #电影天堂搜索页面php
      self.url='http://www.dy2018.com/e/search/index.php'

      #请求头
      self.headers = {
           'Host':'www.dy2018.com',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
           'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
           'Accept-Encoding':'gzip, deflate',
           'Cookie':'bdshare_firstime=1445867603784; CNZZDATA5524964=cnzz_eid%3D1239093655-1476426677-http%253A%252F%252Fwww.dy2018.com%252F%26ntime%3D1480959045; 91turn_1886=1; pescdlastsearchtime=1480959182; BAIDU_SSP_lcr=http://www.so.com/link?url=http%3A%2F%2Fwww.dy2018.com%2F&q=%E7%94%B5%E5%BD%B1%E5%A4%A9%E5%A0%82&ts=1480958935&t=81c0491e9520ee1e32e284eb21bd1c6&src=haosou; pescdfeedbackbid=2',
           'Connection':'keep-alive',
           'Upgrade-Insecure-Requests':'1'
            }

    def print_info(self,movie_name):
      html=self.post_movie_name(movie_name)
      print(html)
      link=re.findall('<td height="26">.*?<a href="(.*?)" '
                        'class="ulink" title="(.*?)">',html,re.S)

      i=1
      for each in link:
        print(str(i)+'.'+each[1])
        i+=1
        #从搜索结果中选出中意的
      num=input('请选择下载项:')
      movie_url='http://www.dy2018.com'+link[int(num)-1][0]

      #打开所选页面
      html2=requests.get(movie_url)
      html2.encoding='gb2312'

      try:
        down_link = re.findall('<td style="WORD-WRAP: break-word" '
                               'bgcolor="#fdfddf"><a href="'
                               '(.*?)">',html2.text,re.S)
      except:
        down_link = re.findall('<td style="WORD-WRAP: break-word" '
                               'bgcolor="#fdfddf"><font color="#ff0000"><a href="'
                               '(.*?)">',html2.text,re.S)

      #列出所有下载链接
      for each in down_link:
        download_url=each
        print(download_url)


    def post_movie_name(self,movie_name):
      #表单发送数据（form post）
      data={'show':'title,smalltext',
            'tempid': '1',
            'keyboard':movie_name.encode('gb2312'),#根据页面编码（gb2312）设置
             }

      #搜索结果页面，利用正则表达式列出所有搜索结果
      html=requests.post(self.url,headers=self.headers,data=data).text
      return html


dl=down_load_movie()
flag=True
while(flag):
  check=input('1.{0}\n2.{1}\n{2}'.format('下载电影','退出','请选择：'))
  if check=='1':
    movie_name1=input('请输入所查电影名称：')
    dl.print_info(movie_name1)
  elif check=='2':
      flag=False
  else:print('请重新选择\n')
#主函数
#功能1.从电影天堂下载电影，并下载影评、封面
#功能2.批量下载电影