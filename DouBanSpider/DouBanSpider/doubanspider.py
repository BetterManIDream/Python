# -*- coding: utf-8 -*-

#爬取豆瓣《后来的我们》影评，并生成词云

#载入模块
import random
import time
import codecs
from downfile import download
from commeneprase import movieparser
from rendercloud import draw

#主函数入口
if __name__ == '__main__':
    
    #豆瓣评论页地址
    templateurl = 'https://movie.douban.com/subject/26683723/comments?sort=time&status=P'
    #开始爬取
    with codecs.open('later.txt', 'a', encoding='utf-8') as f:
        #50*20共计一千条
        for i in range(50):
            print ('开始爬取第',i,'页评论...')
            targeturl = templateurl.format(i * 20)
            res = download.download_page(targeturl)
            f.writelines(movieparser.get_douban_comments(res))
            #设置爬虫工作间隔时间
            time.sleep(1 + float(random.randint(1, 5)) / 10)
    draw.draw_wordcloud()