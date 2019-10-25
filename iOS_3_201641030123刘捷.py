import requests
from bs4 import BeautifulSoup
#h = {User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36}
r = requests.get('http://2.guitarworld.com.cn/?mod=list_sell&goods_type_id=0&new_level=2&province=0&city=0&sort=&sub_key=&price_select=2&have_pic=0&tran_type=0&page=2')
c = r.content
soup = BeautifulSoup(c,"html.parser")
guitars = []
pageNum = 20
for pageNum in range(1,7):
    url = 'http://2.guitarworld.com.cn/?mod=list_sell&goods_type_id=0&new_level=2&province=0&city=0&sort=&sub_key=&price_select=2&have_pic=0&tran_type=0&page='+str(pageNum)
    p_r = requests.get(url)
    p_c = p_r.content
    p_soup = BeautifulSoup(p_c,'html.parser')

    a = p_soup.find('div',{'class':'info-list'})
    imgs = a.find_all('tr')


for img in imgs:
    build = {}
    build['img'] = img.find('img')['src']
    build['name'] = img.find('h2').text
    guitars.append(build)
import os
path='图片5'
try:
    os.mkdir(path)
except FileExistsError:
    print(path+'已经存在')

for (i,item) in enumerate(guitars):
    img_r=requests.get(item['img'])
    imgdata=img_r.content
    imgpath=path+'/'+str(i)+'_'+item['name']+'.jpg'
    if os.path.exists(imgpath)==False:
        with open(path + '/' + str(i) + '_' + item['name'] + '.jpg','wb') as f:f.write(imgdata)
    else:
        print(item['name']+'已存在')
