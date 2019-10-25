import requests
from bs4 import BeautifulSoup
from PIL import Image,ImageTk
import tkinter as tk
import io
h = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}#加载库
r = requests.get('http://www.gugu5.com/fenlei/rexue/',headers=h)#请求网址
c = r.content#读网站
result_list=[]#建立一个空链表用来存储结果
soup = BeautifulSoup(c,'html.parser')#熬汤
pageNum = soup.find('div',{'class':'NewPages'}).find_all('li')[-3].text#找一共多少页
for i in range (1,int(pageNum)+1):#图片、标题、简介用字典储存的结果列表
    url ='http://www.gugu5.com/fenlei/rexue/'+str(i)+'.html'
    p_r =requests.get(url,headers=h)
    p_c =p_r.content
    p_soup = BeautifulSoup(p_c,'html.parser')
    all_img_list = p_soup.find('div',{'class':'cy_list_mh'}).find_all('ul')
    for item in all_img_list:
        d={}
        d['img']=item.find_all('li')[0].find('a').find('img')['src']
        d['title']=item.find('li',{'class':'title'}).text
        d['intor']=item.find('li',{'class':'info'}).text
        result_list.append(d)

def showInfo(i):#展示爬取的内容
    item = result_list[i]
    url = item['img']
    img_r = requests.get(url,headers=h)
    img_c = img_r.content
    data_stream = io.BytesIO(img_c)
    img = Image.open(data_stream)
    photo = ImageTk.PhotoImage(img)
    imgLabel.config(image=photo)
    imgLabel.image = photo

    titleLable.config(text=item['title'])
    introLable.config(text=item['intor'])
def frpic():
    global index
    index -= 1
    showInfo(index)
def nextPic():
    global index
    index += 1
    showInfo(index)

window = tk.Tk()
window.title('小说')
window.geometry('500x500')
index = 0
imgLabel = tk.Label(window,bg = 'blue')
imgLabel.pack()

titleLable = tk.Label(window,bg='green')
titleLable.pack()

introLable = tk.Label(window,bg='red')
introLable.pack()

nextBtn = tk.Button(window,text='下一个',command=nextPic)
nextBtn.pack()

frpicBtn = tk.Button(window,text='上一个',command=frpic)
frpicBtn.pack()

showInfo(index)
window .mainloop()
