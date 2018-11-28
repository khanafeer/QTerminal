# -*- coding: utf-8 -*-
import MySQLdb
import datetime
import requests
import json
from websockets import creat_socket
class Server():
    SRV = "http://192.168.42.228:8000/"
    terminal = 0
    service_id = 0
    current = None
    length = 0
    def __init__(self):
        Server.server = requests.session()
    def login(self,username,password):
        try:
            res = Server.server.post(self.SRV+"api-token-auth/",{"username":"{}".format(username),"password":"{}".format(password)})
            if res.status_code == 200:
                self.TOKEN = json.loads(res.content)['token']
                Server.server.headers = {'Authorization': 'token {}'.format(self.TOKEN)}
                self.get_terminal()
                return True
        except Exception as ex:
            print ex
            pass
        return False

    def next_cust(self):
        try:
            res = Server.server.get(self.SRV+"queserver/call-client/")
            if res.status_code == 200:
                s = json.loads(res.content)['num']
                if s:
                    self.current = s
                ss = json.loads(res.content)['length']
                print ss
                if ss:
                    self.length = ss
            return True
        except:
            return False

    def get_terminal(self):
        res = Server.server.get(self.SRV + "queserver/get-terminal/")
        if res.status_code == 200:
            terminal = json.loads(res.content)['terminal']
            print("vvv",terminal)
            self.terminal = terminal
    def terminal_user_edt(self,terminal):
        if terminal:
            t = {"terminal":terminal}
            res = Server.server.post(self.SRV+"queserver/change-terminal/",t)
            print terminal,res.status_code
            if res.status_code == 200:
                self.terminal = terminal
        return True