#coding=utf8
import itchat, time
import requests
import re
import os

#itchat.auto_login()

def search_douban():
  key_word=['仰山公园','安立路','大屯路','北苑路','亚运村']
  page = 3#抓取页面数量
  #total_page = re.findall('<span class="thispage" '
  #                        'data-total-page="(.*?)">1</span>',
  #                         html.text,re.S)
  page_num = 50#每页数量
  data_list=[]

  if os.path.exists('house_rent.txt'):
    with open('house_rent.txt','r') as f:
      data=f.readlines()
  else:
    f=open('house_rent.txt','w')
    data=[]

  #print('data:',data)
  for j in key_word:
    for i in range(page):
      url = 'https://www.douban.com/group/search?start='+str(i*page_num)+\
            '&cat=1013&group=26926&sort=relevance&q='+j+\
            '&sort=time'#按发布时间排序
      #print(url)
      html = requests.get(url)
      out = re.findall('href="https://www.douban.com/group/topic/(.*?)/" title="(.*?)">',html.text,re.S)
      for each in out:#遍历所有信息，剔除不已出租和求租信息
        if each[0]+'\n' not in data \
           and '已' not in each[1] \
           and '求租' not in each[1]:
              tmp='https://www.douban.com/group/topic/'+each[0]+each[1]
              data_list.append(tmp)#需发送信息
              with open('house_rent.txt','a') as f:#需写入信息
                    f.write(each[0]+'\n')

  if len(data_list)>0:
      return ('新房源信息',data_list)
  else:return ('无新房源信息')

while(True):
  dt = list(time.localtime())
  hour = dt[3]
  minute = dt[4]
  second = dt[5]
  #print(itchat.search_friends(name='亲爱的'))
  if hour == 15 and minute == 0 and second==0:
    out_put = search_douban()
    name=itchat.search_friends(name='亲爱的')
    itchat.send(out_put, toUserName='filehelper')
    itchat.send('%s：%s' % ('女王大人:',out_put), name[0]['UserName'])

    time.sleep(2)
itchat.run()
