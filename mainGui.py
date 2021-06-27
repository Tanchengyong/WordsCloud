
import re
from tkinter import filedialog
import os,sys,time

from tkinter import *

from matplotlib.pyplot import text
from fencitools import createFCpng
from tkinter import messagebox
import cipin

class mainGui():
    def __init__(self,window):
        self.window = window
        
    def set_init_window(self):
        self.window.title("词云图片生成器")           #窗口名
        #self.window.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.window.geometry('750x550+300+60')
        self.window["bg"] = 'green'                                   #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.window.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
       
        #选择词云分析文件
        self.init_data_label = Label(self.window, text="解析分析文件：\n(只能为txt格式)")
        self.init_data_label.grid(row=1, column=2,padx=15)
        
        self.chooseFilePath = StringVar(self.window)
        self.entry_chooseFilePath = Entry(self.window,textvariable=self.chooseFilePath, width=66)  
        self.entry_chooseFilePath.grid(row=1, column=3,  columnspan=10,pady=15,padx=6)
        
        self.str_trans_to_md5_button = Button(self.window, 
                                              text="选择文件", 
                                              bg="yellow", 
                                              activebackground = "pink",
                                              activeforeground = "blue",
                                              width=10,
                                              command=self.chooseFile)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=13,pady=15,padx=15)
        
        #选择词云模型图片
        self.init_data_label = Label(self.window, text="模型图片：")
        self.init_data_label.grid(row=2, column=2,padx=15)
        
        self.choosePicturePath = StringVar(self.window)
        self.entry_choosePicturePath = Entry(self.window,textvariable=self.choosePicturePath, width=66)  
        self.entry_choosePicturePath.grid(row=2, column=3,  columnspan=10,pady=15,padx=6)
        
        self.str_trans_to_md5_button = Button(self.window,
                                              text="选择模型图片",
                                              bg="yellow",
                                              activebackground = "pink",
                                              activeforeground = "blue",
                                              width=10,
                                              command=self.choosePicture)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=2, column=13,pady=15,padx=15)
        
    
        #或者自定义分词
        self.contain_label = Label(self.window, text="自定义分词内容：\n(自定义分词内容时\n上面路径不需选择)")
        self.contain_label.grid(row=13, column=2)
       
        self.contain_data_Text = Text(self.window, 
                                      width=66,
                                      bg="lightyellow",
                                      height=9
                                      )  
        self.contain_data_Text.grid(row=13, column=3, columnspan=10,pady=15,padx=6)
        
        self.btn_seeCiPin = Button(self.window,
                                              text="查看词频统计",
                                              bg="yellow", 
                                              activebackground = "pink",
                                              activeforeground = "blue",
                                              width=10,
                                              command=self.seeCiPin)  # 调用内部方法  加()为直接调用
        self.btn_seeCiPin.grid(row=13, column=13,pady=15,padx=15)
       
        
        #选择保存路径
        self.init_data_label = Label(self.window, text="保存路径：")
        self.init_data_label.grid(row=14, column=2,padx=15)
        
        self.set_saveFilePath = StringVar(self.window)   #动态赋值
        self.enry_saveFilePath = Entry(self.window,textvariable=self.set_saveFilePath, width=66)  
        self.enry_saveFilePath.grid(row=14, column=3,  columnspan=10,pady=15,padx=6)
        
        self.btn_saveFilePath = Button(self.window,
                                              text="选择保存路径",
                                              bg="yellow", 
                                              activebackground = "pink",
                                              activeforeground = "blue",
                                              width=10,
                                              command=self.saveFile)  # 调用内部方法  加()为直接调用
        self.btn_saveFilePath.grid(row=14, column=13,pady=15,padx=15)
        
        # 日志
        
        self.log_text = Text(self.window,width=77,height=13,bg="lightgray")
        self.log_text.insert("end","操作日志：\n")  
        self.log_text.config(state=DISABLED)
        self.log_text.grid(row=15, column=0,rowspan=2,  columnspan=13,pady=15,padx=10)
        #按钮
        
        self.str_trans_to_md5_button = Button(self.window,
                                              text="预览", 
                                              bg="lightblue",
                                              activebackground = "pink",
                                              activeforeground = "blue",
                                              width=13,
                                              height=2,
                                              command=self.generatePicture)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=15, column=13)
        
        self.str_trans_to_md5_button = Button(self.window,
                                              text="保存", 
                                              bg="lightblue",
                                              activebackground = "pink",
                                              activeforeground = "blue",
                                              width=13,
                                              height=2,
                                              command=self.savePicture,
                                              relief=GROOVE)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=16, column=13)
        
        
        
    
             
    
    
    def getValues(self):
        self.filePath = self.entry_chooseFilePath.get()
        self.picturePath = self.entry_choosePicturePath.get()
        self.context = self.contain_data_Text.get(1.0,END).strip().replace("\n","")
        self.savePath = self.enry_saveFilePath.get()
    
    def createFcPngObject(self,flag=None):
        if flag == "OneWords":
            self.createFCpng = createFCpng(self.window,
                                                self.log_text,
                                                OneWords=self.context,
                                                maskPicture=self.picturePath
                                                )
        else:
            print(self.savePath)
            self.createFCpng = createFCpng(self.window,
                                                self.log_text,
                                                filePath= self.filePath,
                                                maskPicture=self.picturePath,
                                                savePath=self.savePath)
    def generatePicture(self):
         
         self.getValues()
         if (self.context or self.filePath) and self.picturePath:
            try:
                if self.context:
                    self.createFcPngObject("OneWords")
                    self.createFCpng.starter()
                if self.filePath:
                    if ".txt" in self.filePath:
                        self.createFcPngObject()
                        self.createFCpng.starter()
                    else:
                        messagebox.showwarning("警告","解析文件目前只支持txt格式")
            except Exception as e:
                if "utf-8" in str(e):
                    msg = str(self.get_current_time()) +" " + str("发生异常,文件编码格式不对，请操作‘另存为’文件并设置编码格式为UTF8") + "\n"*3      #换行
                    self.insertLog(msg)
         else:
             messagebox.showwarning("警告","解析文件路径或者自定义词语任选其一，模板图片必填")
    
    
    def savePicture(self): 
        self.getValues()
        if (self.context or self.filePath) and self.picturePath and self.savePath:
            try:
                if self.context:
                    self.createFcPngObject("OneWords")
                    self.createFCpng.starter()
                if self.filePath:
                    self.createFcPngObject()
                    self.createFCpng.starter(saveFlag=True)
            except Exception as e:
                if "utf-8" in str(e):
                    msg = str(self.get_current_time()) +" " + str("发生异常,文件编码格式不对，请操作‘另存为’文件并设置编码格式为UTF8") + "\n"*3      #换行
                    self.insertLog(msg) 
        else:
            messagebox.showinfo("提示","解析文件路径或者自定义词语任选其一，模板图片、保存路径必填")
    
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time  
     
    def insertLog(self,msg):
        self.log_text.config(state=NORMAL)
        self.log_text.insert("end",msg)
        self.log_text.config(state=DISABLED)
        self.window.update()   
       
    def chooseFile(self):
        default_dir = r"C:\Users\lenovo\Desktop"  # 设置默认打开目录
        fname = filedialog.askopenfilename(title=u"选择文件", initialdir=(os.path.expanduser(default_dir)))
        self.chooseFilePath.set(fname)
    
    def choosePicture(self):
        default_dir = r"C:\Users\lenovo\Desktop"  # 设置默认打开目录
        fname = filedialog.askopenfilename(title=u"选择文件", initialdir=(os.path.expanduser(default_dir)))
        self.choosePicturePath.set(fname)
    
    def saveFile(self):
        default_dir = r"C:\Users\lenovo\Desktop"  # 设置默认打开目录
        fname = filedialog.askdirectory(title=u"选择文件", initialdir=(os.path.expanduser(default_dir)))
        self.set_saveFilePath.set(fname)
    
    def seeCiPin(self):
        self.getValues()
        if (self.context or self.filePath) and self.picturePath:
            try:
                if self.context:
                    self.createFcPngObject("OneWords")
                    self.createFCpng.setCiPin()
                if self.filePath:
                    if ".txt" in self.filePath:
                        self.createFcPngObject()
                        self.createFCpng.setCiPin()
                    else:
                        messagebox.showwarning("警告","解析文件目前只支持txt格式")
                ci = [str(i) for i in cipin.ciping]
                messagebox.showwarning("只展示前10个","\n".join(ci))
            except Exception as e:
                if "utf-8" in str(e):
                    msg = str(self.get_current_time()) +" " + str("发生异常,文件编码格式不对，请操作‘另存为’文件并设置编码格式为UTF8") + "\n"*3      #换行
                    self.insertLog(msg)
        else:
             messagebox.showwarning("警告","解析文件路径或者自定义词语任选其一，模板图片必填")
             
        
        
        
    
        # 
    
        
    
    def del_object(self):
        sys.exit(0)
        
        
def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = mainGui(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()


    init_window.protocol("WM_DELETE_WINDOW",ZMJ_PORTAL.del_object)
    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示
    
    
    


gui_start()