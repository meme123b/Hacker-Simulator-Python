from tkinter import *
from tkinter import messagebox
from random import randint
from threading import Thread
from Toolkit import Input_Toolkit
import sys
import os

class Main:
    def __init__(self):
        self.master = Tk()
        self.master.title("Hacker Simulator")
        self.master.geometry("300x300")
        self.master.resizable(False, False)

        self.AllIPAndComputerName = {}
        self.IPVAR = StringVar()
        self.IP = ''

        self.master.wm_protocol('WM_DELETE_WINDOW', self.closing)
    
    def closing(self):
        messagebox.showinfo('tip', '程序不允许直接点击叉键关闭\n请使用exit命令退出程序')

    def NewIP(self):
        for i in range(4):
            self.IP += str(randint(0, 255))
            if i != 3:
                self.IP += '.'
        self.AllIPAndComputerName[self.IP] = 'Hacker Administrator'

    def InterFacer(self):
        self.IPLabel = Label(self.master, textvariable = self.IPVAR, font = ('微软雅黑', 20))
        self.IPLabel.pack()

    def AllLabelUpdate(self):
        self.IPVAR.set(f'IP:{self.IP}')

        self.master.after(10, self.AllLabelUpdate)

    def StartInputAndIf(self):
        while True:
            if self.IP != '未连接':
                UserInput = Input_Toolkit(f'{self.IP}/>')

            else:
                UserInput = Input_Toolkit('/>')

            if UserInput == 'clear':
                os.system('cls')

            elif UserInput == 'dc' or UserInput == 'disconnect':
                self.IP = '未连接'

            elif UserInput == 'exit':
                self.master.quit()
                sys.exit()
            
            elif UserInput == 'help':
                print('-----帮助栏-----\nclear: 清屏\ndc 或 disconnect: 断开对IP地址的连接\nexit退出程序\nhelp: 帮助\nconnect [IP]: 连接到IP地址')
            
            elif UserInput == 'nmap' or UserInput == 'probe':
                if self.IP != '未连接':
                    print('Probeing... Open ports:')

            elif 'connect' in UserInput:
                if UserInput.startswith('connect ') and UserInput != 'connect ':
                    if UserInput.split(' ')[1] in self.AllIPAndComputerName:
                        self.IP = UserInput.split(' ')[1]
                        print('Connecting Complete.')
                        print(f'IP连接成功 计算机名称: {self.AllIPAndComputerName[self.IP]}')
                    else:
                        print(f'Connect错误: " {UserInput.split(' ')[1]} " 不是一个有效的IP地址')

                elif UserInput == 'connect' or UserInput == 'connect ':
                    print(f'Connect错误: 无给予IP地址')

                else:
                    print(f'命令错误: " {UserInput} " 并不是一个有效的命令')
            
            elif UserInput.strip() == '':
                continue

            else:
                if ' ' not in UserInput:
                    print(f'命令错误: " {UserInput} " 并不是一个有效的命令')
                else:
                    if UserInput.split(' ')[0] != '':
                        print(f'命令错误: " {UserInput.split(" ")[0]} " 并不是一个有效的命令')
                    else:
                        print(f'命令错误: " {UserInput} " 并不是一个有效的命令')

    def Run(self):
        self.NewIP()
        Thread(target = self.StartInputAndIf).start()
        self.InterFacer()
        self.AllLabelUpdate()
        self.master.mainloop()

if __name__ == '__main__':
    Main().Run()
