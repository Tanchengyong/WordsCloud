import os,sys ,time,re
from tkinter import messagebox
import jieba         #分词python库
from matplotlib import pyplot    #python画图库
import collections
from wordcloud import WordCloud,STOPWORDS #python词云库
from PIL import Image    # 图形处理，图形序化、验证码
import numpy  as np      #矩阵数据处理
import cipin


class createFCpng():
    def __init__(self,window, log_text,filePath=None, maskPicture=None,savePath=None,OneWords = None):
        self.filePath = filePath
        self.maskPicture = maskPicture
        self.savePath = savePath
        self.OneWords = OneWords
        self.log_text = log_text
        self.window = window
        self.wcConfig = {
            "background_color" : "white",
                    "contour_width" :  0,
                    "font_path" :   "STSONG.TTF",
                    "contour_color" : 'steelblue',
                    "repeat"  :   True
        }
        
    def insertLog(self,msg):
        self.log_text.config(state="normal")
        self.log_text.insert("end",msg)
        self.log_text.config(state="disabled")
        self.window.update() 
        
        
    def del_words(self):
        
        words = ['的','地','要','和','它','与',"一"]
        self.cipinWords = [ i for i in self.cutWordsAll if i not in words and len(i) >= 2]
        self.cutWords = " ".join(self.cipinWords)
        print(self.cutWords)
        
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time
    
    def getWords(self):
        with open(self.filePath,"r",encoding="UTF-8") as reader:
            text  =  reader.read()
            self.text = re.sub(r"\t|\n|\。|\、|\，|-|:|\（|\{|\}|\）|\?|\“|\”|\]|\[","",text)
            
    def getOneWords(self):
             self.text = str(self.OneWords)*500
             
             
    def cutWords(self):
        msg = str(self.get_current_time()) +" " + str("正在进行分词,马上就好*_*-0.0 ....") + "\n"      #换行
        self.insertLog(msg) 
        
        self.cutWordsAll =jieba.cut(self.text) # 没有去掉无用的词
        print("dsadadddddddddddd")
        self.del_words()
        cipin.ciping = collections.Counter(self.cipinWords).most_common(10)
        
        msg = str(self.get_current_time()) +" " + str("分词成功！") + "\n"      #换行
        self.insertLog(msg) 
        
    def getMaskPicture(self):
        msg = str(self.get_current_time()) +" " + str("正在处理图片,马上就好*_*-0.0 ....") + "\n"      #换行
        self.insertLog(msg) 
        maskPicture = Image.open(self.maskPicture)
        self.maskPictureArray = np.array(maskPicture)
        msg = str(self.get_current_time()) +" " + str("图片处理成功！") + "\n"      #换行
        self.insertLog(msg)
        
    def generateWC(self):
            stopwordss = set(STOPWORDS)
            stopwordss.add("said")
            self.wcConfig["mask"] = self.maskPictureArray
            self.wcConfig["stopwords"] = stopwordss
            self.wc = WordCloud(
                    **self.wcConfig
                )
            self.wc.generate_from_text(self.cutWords)
            
    def drawPinture(self,saveFlag=None):
        # pyp = pyplot.figure(1)

        if saveFlag:
            if self.savePath:
                msg = str(self.get_current_time()) +" " + str("正在保存词云图片,马上就好 *_*-0.0  ....") + "\n"      #换行
                self.insertLog(msg)
                pyplot.imshow(self.wc)
                pyplot.axis("off")
                pyplot.savefig(self.savePath + self.fileName,dpi=300)
                msg = str(self.get_current_time()) +" " + str("保存成功：保存路径：{}".format(self.savePath + self.fileName)) + "\n"*2      #换行
                self.insertLog(msg)
                messagebox.showinfo("提示","保存成功，路径为{}".format(self.savePath + self.fileName))  
            else:
                messagebox.showinfo("提示","保存路径不能为空")
                
        else:
            try:
                msg = str(self.get_current_time()) +" " + str("正在生成预览图片,马上就好*_*-0.0 ....") + "\n"      #换行
                self.insertLog(msg)
                pyplot.imshow(self.wc)

                pyplot.axis("off")

                pyplot.show()
                msg = str(self.get_current_time()) +" " + str("预览图片生成 成功！") + "\n"*2      #换行
                self.insertLog(msg)

            except Exception as e:
                msg = str(self.get_current_time()) +" " + str("预览图片生成 失败！：：{}".format(e)) + "\n"*2      #换行
                self.insertLog(msg)

    
    def  starter(self,saveFlag=None):
        
        if self.OneWords:
            self.fileName = r"/FenCi.png"
            self.getOneWords()   
        if self.filePath:
            self.fileName = "/" + self.filePath.split(".")[0].split("/")[-1:][0] + ".png"
            print(self.fileName)
            self.getWords()
        self.cutWords()    
        self.getMaskPicture()    
        self.generateWC()    
        self.drawPinture(saveFlag)
    
    
    def setCiPin(self):
        if self.OneWords:
            self.fileName = r"/FenCi.png"
            self.getOneWords()   
        if self.filePath:
            self.fileName = "/" + self.filePath.split(".")[0].split("/")[-1:][0] + ".png"
            print(self.fileName)
            self.getWords()
        self.cutWords() 
        
        
