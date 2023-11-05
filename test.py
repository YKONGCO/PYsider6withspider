from typing import Optional
from PySide6.QtWidgets import QApplication, QMainWindow,QPushButton,QLabel,QWidget
from PySide6.QtGui import QTextCursor
from PySide6.QtCore import Qt,QThread,QTimer
import pyspiderui_ui as ui
import spider as sp
import sys
import threading

class spiderThread(QThread):
    def __init__(self, param1, param2,parent=None):
        super().__init__(parent)
        self.cookies = param1
        self.savepath = param2
        
    def run(self):
        sp.main(self.cookies,self.savepath)
        
    


class Mywindows(QMainWindow,ui.Ui_MainWindow):
    cookies=''
    savepath=''
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.providebtn.clicked.connect(self.get)
        self.startbtn.clicked.connect(self.startspider)
        sys.stdout=self
        
        

    def write(self,text):
        cursor = self.outputtext.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.outputtext.setTextCursor(cursor)
        self.outputtext.ensureCursorVisible()
    
    
    
    def get(self):
        self.cookies = self.cookielabinput.text()
        self.savepath = self.savepathline.text()
        if self.cookies == '' or self.savepath == '':
            self.state.setText("无效参数")
            return -1
        self.state.setText("传递参数成功")

    def startspider(self):
        try: 
            if self.state.text()=="无效参数" or self.state.text()=="未提交参数":
                self.outputtext.setText("运行错误,请传入参数")
                return -1
            self.outputtext.clear()
            self.outputtext.setText("爬虫开始运行\n")
            self.spt=spiderThread(self.cookies,self.savepath)
            self.spt.start()
            # self.spiderthreading=threading.Thread(target=sp.main,args=(self.cookies,self.savepath))
            # self.spiderthreading.start()
        except Exception as e:
            print("错误:",e)
            return -1     
        
if __name__ == '__main__':
        app=QApplication([])
        windows=Mywindows()
        windows.show()
        app.exec()    
    
       
        