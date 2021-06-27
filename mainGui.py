
from tkinter import filedialog
import os,sys

from tkinter import *
from fencitools import createFCpng
class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name
        
    def set_init_window(self):
        self.init_window_name.title("词云图片生成器")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('800x400+300+100')
        self.init_window_name["bg"] = '#%02x%02x%02x'%(2,3,25)                                   #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
       
       
        #选择词云分析文件
        self.init_data_label = Label(self.init_window_name, text="  词云分析文件路径：")
        self.init_data_label.grid(row=1, column=2,padx=15)
        
        self.chooseFilePath = StringVar(self.init_window_name)
        self.entry_chooseFilePath = Entry(self.init_window_name,textvariable=self.chooseFilePath, width=66)  
        self.entry_chooseFilePath.grid(row=1, column=3,  columnspan=10,pady=15,padx=6)
        
        self.str_trans_to_md5_button = Button(self.init_window_name, text="选择文件", bg="lightblue", width=10,command=self.chooseFile)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=16,pady=15,padx=15)
        
        #选择词云模型图片
        self.init_data_label = Label(self.init_window_name, text="  模型图片路径：")
        self.init_data_label.grid(row=2, column=2,padx=15)
        
        self.choosePicturePath = StringVar(self.init_window_name)
        self.entry_choosePicturePath = Entry(self.init_window_name,textvariable=self.choosePicturePath, width=66)  
        self.entry_choosePicturePath.grid(row=2, column=3,  columnspan=10,pady=15,padx=6)
        
        self.str_trans_to_md5_button = Button(self.init_window_name, text="选择模型图片", bg="lightblue", width=10,command=self.choosePicture)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=2, column=16,pady=15,padx=15)
        
    
        #或者自定义分词
        self.log_label = Label(self.init_window_name, text="自定义分词内容：\n(自定义分词内容时上面路径不需选择)")
        self.log_label.grid(row=13, column=2)
       
        self.contain_data_Text = Text(self.init_window_name, width=66, height=9)  
        self.contain_data_Text.grid(row=13, column=3, columnspan=10,pady=15,padx=6)
       
        
        #选择保存路径
        self.init_data_label = Label(self.init_window_name, text="  选择保存路径：")
        self.init_data_label.grid(row=14, column=2,padx=15)
        
        self.set_saveFilePath = StringVar(self.init_window_name)   #动态赋值
        self.enry_saveFilePath = Entry(self.init_window_name,textvariable=self.set_saveFilePath, width=66)  
        self.enry_saveFilePath.grid(row=14, column=3,  columnspan=10,pady=15,padx=6)
        
        self.str_trans_to_md5_button = Button(self.init_window_name, text="选择保存路径", bg="lightblue", width=10,command=self.saveFile)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=14, column=16,pady=15,padx=15)
        
        
        #按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="生成词云图片", bg="lightblue", width=10,command=self.generatePicture)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=15, column=4)
        self.str_trans_to_md5_button = Button(self.init_window_name, text="预览", bg="lightblue", width=10,command=self.generatePicture)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=15, column=8)
        
        
        
    def generatePicture(self):
         filePath = self.entry_chooseFilePath.get()
         picturePath = self.entry_choosePicturePath.get()
         context = self.contain_data_Text.get(1.0,END).strip().replace("\n","")
         savePath = self.enry_saveFilePath.get()
         if context:
            self.createFCpng = createFCpng(OneWords=context,maskPicture=picturePath,savePath=savePath)
            self.createFCpng.starter()
         if filePath:
            self.createFCpng = createFCpng(filePath=filePath,maskPicture=picturePath,savePath=savePath)
            self.createFCpng.starter()

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
    
    def del_object(self):
        sys.exit(0)
        
        
def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()


    init_window.protocol("WM_DELETE_WINDOW",ZMJ_PORTAL.del_object)
    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示
    
    
    


gui_start()