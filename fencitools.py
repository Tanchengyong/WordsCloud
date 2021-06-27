import os,sys   # 轻量级数据库

import jieba         #分词python库
from matplotlib import pyplot    #python画图库
# from wordcloud import STOPWORDS as stop
from wordcloud import WordCloud  #python词云库
from PIL import Image    # 图形处理，图形序化、验证码
import numpy  as np      #矩阵数据处理



class createFCpng():
    def __init__(self, filePath=None, maskPicture=None,savePath=None,OneWords = None):
        self.filePath = filePath
        self.maskPicture = maskPicture
        self.savePath = savePath
        self.OneWords = OneWords
        self.wcConfig = {
            "background_color" : "white",
                    "contour_width" :  0,
                    "font_path" :   "STSONG.TTF",
                    "contour_color" : 'steelblue',
                    "repeat"  :   True
        }
    def getWords(self):
        with open(self.filePath,"r",encoding="UTF-8") as reader:
            self.text  =  reader.read()      
    def getOneWords(self):
             self.text = str(self.OneWords)*300
    def cutWords(self):
        self.cutWords =" ".join( jieba.cut(self.text)) 
    def getMaskPicture(self):
        
        maskPicture = Image.open(self.maskPicture)
        self.maskPictureArray = np.array(maskPicture)
    def generateWC(self):
            # stopwordss = set(stop)
            # stopwordss.add("said")
            self.wcConfig["mask"] = self.maskPictureArray
            # self.wcConfig["stopwords"] = stopwordss
            self.wc = WordCloud(
                    **self.wcConfig
                )
            self.wc.generate_from_text(self.cutWords)
    def drawPinture(self):
        # pyp = pyplot.figure(1)

        pyplot.imshow(self.wc)

        pyplot.axis("off")

        pyplot.show()
        pyplot.imshow(self.wc)
        pyplot.axis("off")
        pyplot.savefig(self.savePath + self.fileName,dpi=300)
    
    def  starter(self):
        
        if self.OneWords:
            self.fileName = "FenCi.png"
            self.getOneWords()   
        if self.filePath:
            self.fileName = "\\" + self.filePath.split(".")[0].split("/")[-1:][0] + ".png"
            print(self.fileName)
            self.getWords()
        self.cutWords()    
        self.getMaskPicture()    
        self.generateWC()    
        self.drawPinture()    
        
# createFCpng("text.txt","xin.png",r".\ciyu_ma.png").starter()