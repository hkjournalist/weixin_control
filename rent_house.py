#test works
import requests
import re
import os
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

print('data:',data)
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
for each in data_list:
  print(each)


