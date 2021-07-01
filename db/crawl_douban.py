import requests
import lxml
from lxml import etree

listurl = ['https://movie.douban.com/subject/35356779/',
           'https://movie.douban.com/subject/35171613/',
           'https://movie.douban.com/subject/35418781/']

"""
获取该页面的如data-id="35356779",返回一个urllist列表，https://movie.douban.com/tag/#/?sort=R&range=0,10&tags=%E5%8A%A8%E7%94%BB，
如何获取？
"""
def get_url():
    url = 'https://movie.douban.com/tag/#/?sort=R&range=0,10&tags=%E5%8A%A8%E7%94%BB'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
    data = requests.get(url, headers=headers).text
    s = etree.HTML(data)
    name = s.xpath('//*[@id="db-nav-movie"]/div[2]/div/ul/li[8]/a/text()')
    name2 = s.xpath('//*[@id="app"]/div/div[1]/div[3]/a[1]/p/span[1]')
    # name3 = s.xpath('//*[@id="app"]/div/div[1]/div[3]/a[2]/p/span[1]/text()')
    print(name2)

"""
获取如href="https://movie.douban.com/subject/35356779/"后单个的名称获取函数,传入列表处理所有url并取需要的数据
"""
def douban_d(urls):
    names = []
    for url in urls:
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
        data = requests.get(url, headers=headers).text
        # print(data)
        s = etree.HTML(data)
        name = s.xpath('//*[@id="content"]/h1/span[1]/text()')
        name = ''.join(name)
        names.append(name)
    print(names)

get_url()
# douban_d(listurl)