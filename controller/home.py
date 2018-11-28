# -*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
from view.home import Ui_Form as home
from controller.terminal import Terminal
from model.model import Server
from controller.dialog import showdialog
import websocket
import json
def run_async(func):
    from threading import Thread
    from functools import wraps
    @wraps(func)
    def async_func(*args, **kwargs):
        func_hl = Thread(target = func, args = args, kwargs = kwargs)
        func_hl.setDaemon(True)
        func_hl.start()
        return func_hl
    return async_func
class Home(QWidget,home):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.QSERVER = Server()
        self.login_btn.clicked.connect(self.login_f)
        self.ter = Terminal()
        for i in self.findChildren(QWidget):
             i.setAttribute(Qt.WA_StyledBackground)
        self.exit_btn.clicked.connect(QApplication.exit)
        self.ter.ext_btn.clicked.connect(QApplication.exit)
        self.ter.log_out.clicked.connect(self.log_out)

        self.ter.next_btn.clicked.connect(self.next_)
        self.ter.call_btn.clicked.connect(self.call_cust)
    def on_message(self,ws, message):
        print("message .....",message)
    def on_error(self,err):
        print("error",err)
    def call_num(self,num,term):
        self.WS.send(json.dumps({"num":num,"terminal":term}))
    def save(self):
        ip = self.tableWidget.item(0, 1).text()
        ter_id = self.tableWidget.item(1, 1).text()
        self.db.set_settings(ip,ter_id)
        if not self.db.db_connect():
            showdialog(u'الاعدادات غير صحيحة',u'يرجى مراجعة عنوان الخادم')
        else:
            showdialog(u'تم الاتصال بنجاح','')

    def log_out(self):
        self.ter.hide()
        self.showNormal()
        self.raise_()
        self.activateWindow()
    def login_f(self):
        '''login function'''
        uname= self.user_edt.text()
        passw = self.pass_edt.text()
        if self.QSERVER.login(uname,passw):
            self.user_edt.clear()
            self.pass_edt.clear()
            terminal = self.user_edt_2.text()
            if terminal:
                self.QSERVER.terminal_user_edt(terminal)
            self.hide()
            self.next_step()
        else:
            QSound('fault.wav').play()
    @run_async
    def WS_OPEN(self):
        self.WS = websocket.WebSocketApp("ws://192.168.42.228:8000/call/",
                                         on_message=self.on_message,
                                         on_error=self.on_error)
        while True:
            self.WS.run_forever()
    def next_step(self):
        self.ter.showNormal()
        self.ter.raise_()
        self.ter.activateWindow()
        self.ter.terminal_lbl.setText(str(self.QSERVER.terminal))
        screen_resolution = QApplication.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()
        self.ter.resize(width,10)
        self.ter.move(0,height-90)
        self.ter.status_btn.setStyleSheet("background:#42f445;border:0;")
        self.ter.status_btn.setToolTip('server connection done.')
        self.WS_OPEN()
    def next_(self):
        '''call next customer'''
        x = self.QSERVER.next_cust()
        if x:
            self.ter.current_lbl.setText(str(self.QSERVER.current))
            self.ter.waiting_lbl.setText(str(self.QSERVER.length))
            self.call_num(self.QSERVER.current,self.QSERVER.terminal)
        else:
            self.ter.current_lbl.setText('error ...')
            self.ter.waiting_lbl.setText('error ...')

    def call_cust(self):
        '''call customer'''
        self.call_num(self.QSERVER.current,self.QSERVER.terminal)


