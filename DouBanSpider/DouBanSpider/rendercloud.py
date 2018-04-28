# wordcloud 生成中文词云
import jieba
from wordcloud import WordCloud
from scipy.misc import imread
from os import path
import matplotlib.pyplot as plt

# 绘制词云
class draw():  
    def draw_wordcloud():
        print('Start render word cloud')
        # 读入一个txt文件
        comment_text = open('later.txt','rb').read()
        # 结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云
        cut_text = " ".join(jieba.cut(comment_text))
        d = path.dirname(__file__) # 当前文件文件夹所在目录
        color_mask = imread("3.jpg") # 读取背景图片
        cloud = WordCloud(
            # 设置字体，不指定就会出现乱码
            font_path="STSONG.TTF",
            # 设置背景色
            background_color='white',
            # 词云形状
            mask=color_mask,
            #允许最大词汇
            max_words=2000,
            #最大号字体
            max_font_size=40
        )
        # print(cut_text)
        word_cloud = cloud.generate(cut_text) # 产生词云
        word_cloud.to_file("later.jpg") # 保存图片
        #  显示词云图片
        plt.imshow(word_cloud)
        plt.axis('off')
        plt.show()
