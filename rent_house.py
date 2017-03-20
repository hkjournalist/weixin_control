#不要乱改
import requests
import re
import os
import itchat, time
key_word=['仰山公园','安立路','大屯路','北苑路','亚运村']
page = 3#抓取页面数量
#total_page = re.findall('<span class="thispage" '
#                        'data-total-page="(.*?)">1</span>',
#                         html.text,re.S)
page_num = 50#每页数量
data_list = []
author_list =[]
#if os.path.exists('house_rent.txt'):
#  with open('house_rent.txt','r') as f:
#    data=f.readlines()
#else:
#    f=open('house_rent.txt','w')
#    data=[]


#itchat.auto_login()


#print('data:',data)
for j in key_word:
 for i in range(page):
  url = 'https://www.douban.com/group/search?start='+str(i*page_num)+\
      '&cat=1013&group=26926&q='+j+\
      '&sort=time'#按发布时间排序
  #print(url)
  html = requests.get(url)

  #print('b')
  #out = re.findall('href="https://www.douban.com/group/topic/(.*?)/" title="(.*?)"> .*<td nowrap="nowrap" class="time">(.*?)</td>',html.text,re.S)
  out0 = re.findall('<tr class="pl">(.*?)</tr>',html.text,re.S)
  #print('c')
  for each in out0:#遍历所有信息，剔除不已出租和求租信息
        if ('地铁' or '号线' in each) \
           and ('已' not in each) \
           and('限男' not in each)\
           and ('求租' not in each):
              link = re.findall('<td class="td-subject"><a class="" href="(.*?)"',each,re.S)
              html2 = requests.get(link[0])
              author = re.findall('<span class="from">来自: <a href="https://www.douban.com/people/[0-9a-zA-Z]+/">(.*?)</a>',html2.text,re.S)
              try:
                if author[0] not in author_list:
                  author_list.append(author[0])
                  word = re.findall('/" title="(.*?)"',each,re.S)
                  date = re.findall('<td class="td-time" title="(.*?)"',each,re.S)
                  tmp=link+word+date+author
              #print(tmp)

                  if '2017-03' in date[0] and word not in data_list:
                    data_list.append(tmp)#需发送信息
                    print(tmp)
              except:print('{0}:{1}'.format('wrong in:',link[0]))
              finally:time.sleep(1)
                #print(date[0][0])
              #with open('house_rent.txt','a') as f:#需写入信息
              #      f.write(each[0]+'\n')


