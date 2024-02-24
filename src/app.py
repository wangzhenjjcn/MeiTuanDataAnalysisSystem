#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('美团经营数据读取软件')
        self.master.geometry('1163x687')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('FrameLog.TLabelframe',font=('宋体',9))
        self.FrameLog = LabelFrame(self.top, text='运行日志', style='FrameLog.TLabelframe')
        self.FrameLog.place(relx=0.186, rely=0.023, relwidth=0.792, relheight=0.945)

        self.style.configure('FrameChromeOptions.TLabelframe',font=('宋体',9))
        self.FrameChromeOptions = LabelFrame(self.top, text='浏览器操作', style='FrameChromeOptions.TLabelframe')
        self.FrameChromeOptions.place(relx=0.021, rely=0.023, relwidth=0.152, relheight=0.945)

        self.ListLogVar = StringVar(value='')
        self.ListLogFont = Font(font=('宋体',9))
        self.ListLog = Listbox(self.FrameLog, listvariable=self.ListLogVar, font=self.ListLogFont)
        self.ListLog.place(relx=0.026, rely=0.049, relwidth=0.948, relheight=0.912)

        self.style.configure('CommandSaveData.TButton',font=('宋体',9))
        self.CommandSaveData = Button(self.FrameChromeOptions, text='保存数据', command=self.CommandSaveData_Cmd, style='CommandSaveData.TButton')
        self.CommandSaveData.place(relx=0.136, rely=0.468, relwidth=0.729, relheight=0.063)

        self.style.configure('CommandHeadlessChrome.TButton',font=('宋体',9))
        self.CommandHeadlessChrome = Button(self.FrameChromeOptions, text='隐藏浏览器', command=self.CommandHeadlessChrome_Cmd, style='CommandHeadlessChrome.TButton')
        self.CommandHeadlessChrome.place(relx=0.136, rely=0.123, relwidth=0.729, relheight=0.063)

        self.style.configure('CommandReadFromCurrent.TButton',font=('宋体',9))
        self.CommandReadFromCurrent = Button(self.FrameChromeOptions, text='从当前页读取', command=self.CommandReadFromCurrent_Cmd, style='CommandReadFromCurrent.TButton')
        self.CommandReadFromCurrent.place(relx=0.136, rely=0.382, relwidth=0.729, relheight=0.063)

        self.style.configure('CommandReadData.TButton',font=('宋体',9))
        self.CommandReadData = Button(self.FrameChromeOptions, text='读取经营数据', command=self.CommandReadData_Cmd, style='CommandReadData.TButton')
        self.CommandReadData.place(relx=0.136, rely=0.296, relwidth=0.729, relheight=0.063)

        self.style.configure('CommandCheckStatus.TButton',font=('宋体',9))
        self.CommandCheckStatus = Button(self.FrameChromeOptions, text='检查登录状态', command=self.CommandCheckStatus_Cmd, style='CommandCheckStatus.TButton')
        self.CommandCheckStatus.place(relx=0.136, rely=0.21, relwidth=0.729, relheight=0.063)

        self.style.configure('CommandOpenChrome.TButton',font=('宋体',9))
        self.CommandOpenChrome = Button(self.FrameChromeOptions, text='打开浏览器', command=self.CommandOpenChrome_Cmd, style='CommandOpenChrome.TButton')
        self.CommandOpenChrome.place(relx=0.136, rely=0.037, relwidth=0.729, relheight=0.063)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def CommandSaveData_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def CommandHeadlessChrome_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def CommandReadFromCurrent_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def CommandReadData_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def CommandCheckStatus_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def CommandOpenChrome_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def log(self,msg):
        print(msg)
        
        pass







if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass
