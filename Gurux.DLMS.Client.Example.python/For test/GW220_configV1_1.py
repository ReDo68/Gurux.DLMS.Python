import serial
import serial.tools.list_ports
from tkinter import *
from tkinter import ttk
import time
import math
from Crypto.Cipher import AES

class preGui:
    def __init__(self, master):
        self.master = master
        master.minsize(520, 620)

        self.label0 = Label(master, text='TAP', fg="blue")
        self.label0.place(bordermode=INSIDE, width=100, height=25, x=230, y=5, relx=0)
        self.label0.config(font=('times', 20, 'bold'))
        self.encMode = AES.MODE_ECB

        self.passVar = StringVar()
        self.passVar.set(' admintap')
        self.ekeyVar = StringVar()
        self.ekeyVar.set(' 1234567812345678')
        self.ekeyEnVar = IntVar()
        self.ekeyEnVar.set(1)

        self.label8 = Label(master, text='    Port : ')
        self.label8.place(bordermode=INSIDE, width=100, height=25, x=20, y=50, relx=0)
        self.comBox = ttk.Combobox(master, state='readonly')
        self.comBox.place(bordermode=INSIDE, width=70, height=20, x=100, y=52.5, relx=0)
        self.updatePorts()
        try:
            self.photo = PhotoImage(file=r"files/refresh.png")
            self.comBoxRefresh = Button(master, image=self.photo, command=lambda: self.updatePorts())
        except:
            self.comBoxRefresh = Button(master, text='R', command=lambda: self.updatePorts())
        self.comBoxRefresh.place(bordermode=INSIDE, width=22, height=22, x=175, y=51.5, relx=0)

        self.settingBut = Button(master, text='Setting', command=lambda: self.settingPage())
        self.settingBut.place(bordermode=INSIDE, width=100, height=25, x=375, y=50)

        self.label3 = Label(master, text='    Serial Number : ')
        self.label3.place(bordermode=INSIDE, width=90, height=25, x=0, y=100, relx=0)
        self.serialNum = Entry(master)
        self.serialNum.place(bordermode=INSIDE, width=130, height=25, x=100, y=100, relx=0)
        self.serialNum.insert(1, ' 00409900')
        self.serNumWrite = Button(master, text='Write', command=lambda: self.writeFunc(1, 1))
        self.serNumWrite.place(bordermode=INSIDE, width=60, height=25, x=240, y=100, relx=0)
        self.serNumRead = Button(master, text='Read', command=lambda: self.readFunc(1, 1))
        self.serNumRead.place(bordermode=INSIDE, width=60, height=25, x=305, y=100, relx=0)
        self.serialNumVar = StringVar()
        self.serialNum2 = Entry(master, textvariable=self.serialNumVar)
        self.serialNum2.place(bordermode=INSIDE, width=130, height=25, x=375, y=100, relx=0)

        self.label2 = Label(master, text='              Server IP : ')
        self.label2.place(bordermode=INSIDE, width=90, height=25, x=0, y=140, relx=0)
        self.ip = Entry(master)
        self.ip.place(bordermode=INSIDE, width=130, height=25, x=100, y=140, relx=0)
        self.ip.insert(1, ' 31.25.92.190')
        self.label4 = Label(master, text='                     Port : ')
        self.label4.place(bordermode=INSIDE, width=90, height=25, x=0, y=180, relx=0)
        self.port = Entry(master)
        self.port.place(bordermode=INSIDE, width=50, height=25, x=100, y=180, relx=0)
        self.port.insert(1, ' 7126')
        self.ipWrite = Button(master, text='Write', command=lambda: self.writeFunc(2, 1))
        self.ipWrite.place(bordermode=INSIDE, width=60, height=65, x=240, y=140, relx=0)
        self.ipRead = Button(master, text='Read', command=lambda: self.readFunc(2, 1))
        self.ipRead.place(bordermode=INSIDE, width=60, height=65, x=305, y=140, relx=0)
        self.ipVar = StringVar()
        self.ip2 = Entry(master, textvariable=self.ipVar)
        self.ip2.place(bordermode=INSIDE, width=130, height=25, x=375, y=140, relx=0)
        self.portVar = StringVar()
        self.port2 = Entry(master, textvariable=self.portVar)
        self.port2.place(bordermode=INSIDE, width=130, height=25, x=375, y=180, relx=0)

        self.label5 = Label(master, text='    EDB Password : ')
        self.label5.place(bordermode=INSIDE, width=90, height=25, x=0, y=220, relx=0)
        self.edbPass = Entry(master)
        self.edbPass.place(bordermode=INSIDE, width=130, height=25, x=100, y=220, relx=0)
        self.edbPass.insert(1, ' admintap')
        self.edbPassWrite = Button(master, text='Write', command=lambda: self.writeFunc(3, 1))
        self.edbPassWrite.place(bordermode=INSIDE, width=60, height=25, x=240, y=220, relx=0)
        self.edbPassRead = Button(master, text='Read', command=lambda: self.readFunc(3, 1))
        self.edbPassRead.place(bordermode=INSIDE, width=60, height=25, x=305, y=220, relx=0)
        self.edbPassVar = StringVar()
        self.edbPass2 = Entry(master, textvariable=self.edbPassVar)
        self.edbPass2.place(bordermode=INSIDE, width=130, height=25, x=375, y=220, relx=0)

        self.label5 = Label(master, text='             Enc. Key : ')
        self.label5.place(bordermode=INSIDE, width=90, height=25, x=0, y=260, relx=0)
        self.encKey_1 = Entry(master)
        self.encKey_1.place(bordermode=INSIDE, width=130, height=25, x=100, y=260, relx=0)
        self.encKey_1.insert(1, ' 1234567812345678')
        self.encKeyWrite = Button(master, text='Write', command=lambda: self.writeFunc(4, 1))
        self.encKeyWrite.place(bordermode=INSIDE, width=60, height=25, x=240, y=260, relx=0)
        self.encKeyRead = Button(master, text='Read', command=lambda: self.readFunc(4, 1))
        self.encKeyRead.place(bordermode=INSIDE, width=60, height=25, x=305, y=260, relx=0)
        self.encKeyVar = StringVar()
        self.encKey2 = Entry(master, textvariable=self.encKeyVar)
        self.encKey2.place(bordermode=INSIDE, width=130, height=25, x=375, y=260, relx=0)

        self.label5 = Label(master, text='               Enc. En : ')
        self.label5.place(bordermode=INSIDE, width=90, height=25, x=0, y=300, relx=0)
        self.ekeyEn_1 = Entry(master)
        self.ekeyEn_1.place(bordermode=INSIDE, width=130, height=25, x=100, y=300, relx=0)
        self.ekeyEn_1.insert(1, ' 1')
        self.ekeyEnWrite = Button(master, text='Write', command=lambda: self.writeFunc(8, 1))
        self.ekeyEnWrite.place(bordermode=INSIDE, width=60, height=25, x=240, y=300, relx=0)
        self.ekeyEnRead = Button(master, text='Read', command=lambda: self.readFunc(8, 1))
        self.ekeyEnRead.place(bordermode=INSIDE, width=60, height=25, x=305, y=300, relx=0)
        self.ekeyEn_2_var = StringVar()
        self.ekeyEn_2 = Entry(master, textvariable=self.ekeyEn_2_var)
        self.ekeyEn_2.place(bordermode=INSIDE, width=130, height=25, x=375, y=300, relx=0)

        self.label6 = Label(master, text='        Filters : ')
        self.label6.place(bordermode=INSIDE, width=100, x=10, y=340, relx=0)
        self.filters = Text(master, font='helvetica 9')
        self.filters.place(bordermode=INSIDE, width=130, height=100, x=100, y=340, relx=0)
        self.filtersWrite = Button(master, text='Write', command=lambda: self.writeFunc(5, 1))
        self.filtersWrite.place(bordermode=INSIDE, width=60, height=25, x=240, y=340, relx=0)
        self.filtersRead = Button(master, text='Read', command=lambda: self.readFunc(5, 1))
        self.filtersRead.place(bordermode=INSIDE, width=60, height=25, x=305, y=340, relx=0)
        self.filters2 = Text(master, font='helvetica 9')
        self.filters2.place(bordermode=INSIDE, width=130, height=100, x=375, y=340, relx=0)
        self.filters.insert("0.0", ' 1.8.1\n 1.8.2\n 1.8.3\n 1.8.0\n 01.08.01\n 01.08.02\n 01.08.03\n 01.08.00\n 1-0:1.8.1.255\n 1-0:1.8.2.255\n 1-0:1.8.3.255\n 1-0:0.0.0.255\n 1-0:1.8.0.255\n 0-0:96.1.0.255\n 00.00.00\n 00.00.01\n 96.01.00\n 0.0.0\n C.1.0')

        self.readAll = Button(master, text='Read All', command=lambda: self.readAllObises())
        self.readAll.place(bordermode=INSIDE, width=130, height=50, x=235, y=450, relx=0)
        self.writeAll = Button(master, text='Write All', command=lambda: self.writeAllObises())
        self.writeAll.place(bordermode=INSIDE, width=130, height=50, x=235, y=510, relx=0)

        self.label7 = Label(master, text='             SMS : ')
        self.label7.place(bordermode=INSIDE, width=90, height=25, x=0, y=580, relx=0)
        self.sms1 = Entry(master)
        self.sms1.place(bordermode=INSIDE, width=130, height=25, x=100, y=580, relx=0)
        self.sms1.insert(1, ' 9')
        self.smsWrite = Button(master, text='Send', command=lambda: self.writeFunc(6, 1))
        self.smsWrite.place(bordermode=INSIDE, width=100, height=25, x=250, y=580, relx=0)
        self.smsVar = StringVar()
        self.sms2 = Entry(master, textvariable=self.smsVar)
        self.sms2.place(bordermode=INSIDE, width=130, height=25, x=375, y=580, relx=0)

        self.CheckConnection = Button(master, text='Check Connection', command=lambda: self.readFunc(6, 1))
        self.CheckConnection.place(bordermode=INSIDE, width=120, height=30, x=30, y=470, relx=0)
        self.result1 = StringVar()
        self.label10 = Label(master, textvariable=self.result1)
        self.label10.place(bordermode=INSIDE, width=120, x=30, y=510, relx=0)
        self.result2 = StringVar()
        self.label11 = Label(master, textvariable=self.result2)
        self.label11.place(bordermode=INSIDE, width=120, x=30, y=530, relx=0)
        self.label12 = Label(master, text='Copyright © 2021')
        self.label12.place(bordermode=INSIDE, width=120, x=400, y=520, relx=0)
        self.label13 = Label(master, text='Tech. Art Part')
        self.label13.place(bordermode=INSIDE, width=120, x=400, y=540, relx=0)

    def settingPage(self):
        self.settingW = Toplevel(self.master)
        self.settingW.title("Setting")
        self.settingW.geometry("400x150")
        Label(self.settingW, text='Setting', font=('Calibri', 14)).place(bordermode=INSIDE, width=100, height=25, x=160, y=5)
        Label(self.settingW, text='             Password : ').place(bordermode=INSIDE, width=100, height=25, x=0, y=50)
        Entry(self.settingW, textvariable=self.passVar).place(bordermode=INSIDE, width=100, height=25, x=110, y=50)
        Label(self.settingW, text='    Encryption key : ').place(bordermode=INSIDE, width=100, height=25, x=0, y=90)
        Entry(self.settingW, textvariable=self.ekeyVar).place(bordermode=INSIDE, width=150, height=25, x=110, y=90)
        Checkbutton(self.settingW, text="Enable", variable=self.ekeyEnVar).place(bordermode=INSIDE, x=270, y=90)
    def updatePorts(self):
        try:
            temp = serial.tools.list_ports.comports(include_links=False)
            self.ports = []
            for port in temp:
                self.ports += [port.device]
            self.comBox.config(values=self.ports)
            self.comBox.current(0)
        except:
            self.comBox.config(values=[''])
            self.comBox.current(0)

    def readFunc(self, a, portState):
        if portState:
            self.openPort()
            if self.portOpenSucc == 0:
                if a == 1:
                    self.serialNumVar.set('')
                elif a == 2:
                    self.portVar.set('')
                    self.ipVar.set('')
                elif a == 3:
                    self.edbPassVar.set('')
                elif a == 4:
                    self.encKeyVar.set('')
                elif a == 5:
                    self.filters2.delete("0.0", END)
                return

        if len(self.passVar.get().replace(' ', '')) != 8:
            self.serialNumVar.set('')
            self.label10.config(fg='red')
            self.result1.set('Password length!')
            self.ser.close()
            return

        sendBuf = b'\x7E\x00\x23\x00\x03\x00\x19\xff\x23\x00\x00' + bytes(self.passVar.get().replace(' ', ''), 'utf-8') + b'R5\x02'
        if a == 1:
            self.serialNumVar.set('')
            sendBuf += b'010000()\r\n\x00\x00\x00'
            if self.ekeyEnVar.get():
                encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                sendBuf = sendBuf[:3] + encryptor.encrypt(sendBuf[3:])
            sendBuf += self.calCrc(sendBuf[3:], 32)
            sendBuf += b'\x7E'
            self.ser.write(sendBuf)
            self.ser.timeout = 0.5
            rcvMsg = self.ser.read(3)
            if rcvMsg == b'':
                self.serialNum2.config(fg='red')
                rcvMsgT = 'NO RESPONSE'
            else:
                self.ser.timeout = 3
                rcvMsg = self.ser.read(int.from_bytes(rcvMsg[1:], "big"))
                if self.ekeyEnVar.get():
                    encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                    rcvMsg = encryptor.decrypt(rcvMsg[:int(len(rcvMsg)/16)*16])

                rcvMsg = str(rcvMsg[8:])

                if rcvMsg[:15].find('ERROR') != -1:
                    self.serialNum2.config(fg='red')
                    if rcvMsg[rcvMsg.find('ERROR')+6] == 'P':
                        rcvMsgT = 'FORMAT ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR')+6] == 'Q':
                        rcvMsgT = 'PASSWORD ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'DATA ERROR'
                    else:
                        rcvMsgT = 'UNKNOWN ERROR'
                elif rcvMsg.find('CORRECT') == -1:
                    self.serialNum2.config(fg='red')
                    rcvMsgT = 'UNKNOWN ERROR'
                else:
                    rcvMsg = rcvMsg[rcvMsg.find('CORRECT'):]
                    self.serialNum2.config(fg='black')
                    rcvMsgT = rcvMsg[rcvMsg.find('(') + 1:rcvMsg.find(')')]
            rcvMsgT = ' ' + rcvMsgT
            self.serialNumVar.set(rcvMsgT)
        # IP Port
        elif a == 2:
            self.portVar.set('')
            self.ipVar.set('')
            self.ip2.config(fg='red')
            self.port2.config(fg='red')
            sendBuf += b'102025()\r\n\x00\x00\x00'
            if self.ekeyEnVar.get():
                encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                sendBuf = sendBuf[:3] + encryptor.encrypt(sendBuf[3:])
            sendBuf += self.calCrc(sendBuf[3:], 32)
            sendBuf += b'\x7E'
            self.ser.write(sendBuf)
            self.ser.timeout = 0.5
            rcvMsg = self.ser.read(3)
            if rcvMsg == b'':
                self.ip2.config(fg='red')
                self.port2.config(fg='red')
                rcvMsgT = 'NO RESPONSE'
                rcvMsgT2 = 'NO RESPONSE'
            else:
                self.ser.timeout = 3
                rcvMsg = self.ser.read(int.from_bytes(rcvMsg[1:], "big"))
                if self.ekeyEnVar.get():
                    encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                    rcvMsg = encryptor.decrypt(rcvMsg[:int(len(rcvMsg) / 16) * 16])

                rcvMsg = str(rcvMsg[8:])

                if rcvMsg[:15].find('ERROR') != -1:
                    self.ip2.config(fg='red')
                    self.port2.config(fg='red')
                    if rcvMsg[rcvMsg.find('ERROR') + 6] == 'P':
                        rcvMsgT = 'FORMAT ERROR'
                        rcvMsgT2 = 'FORMAT ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'PASSWORD ERROR'
                        rcvMsgT2 = 'PASSWORD ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'DATA ERROR'
                        rcvMsgT2 = 'DATA ERROR'
                    else:
                        rcvMsgT = 'UNKNOWN ERROR'
                        rcvMsgT2 = 'UNKNOWN ERROR'
                elif rcvMsg.find('CORRECT') == -1:
                    self.ip2.config(fg='red')
                    self.port2.config(fg='red')
                    rcvMsgT = 'UNKNOWN ERROR'
                    rcvMsgT2 = 'UNKNOWN ERROR'
                else:
                    rcvMsg = rcvMsg[rcvMsg.find('CORRECT'):]
                    self.ip2.config(fg='black')
                    self.port2.config(fg='black')
                    rcvMsgT = rcvMsg[rcvMsg.find('"') + 1:rcvMsg.find(',')-1]
                    rcvMsgT2 = rcvMsg[rcvMsg.find(',') + 1:rcvMsg.find(')')]
            rcvMsgT = ' ' + rcvMsgT
            rcvMsgT2 = ' ' + rcvMsgT2
            self.ipVar.set(rcvMsgT)
            self.portVar.set(rcvMsgT2)

        # EDB password
        elif a == 3:
            self.edbPassVar.set('')
            sendBuf += b'104305()\r\n\x00\x00\x00'
            if self.ekeyEnVar.get():
                encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                sendBuf = sendBuf[:3] + encryptor.encrypt(sendBuf[3:])
            sendBuf += self.calCrc(sendBuf[3:], 32)
            sendBuf += b'\x7E'
            self.ser.write(sendBuf)
            self.ser.timeout = 0.5
            rcvMsg = self.ser.read(3)
            if rcvMsg == b'':
                self.edbPass2.config(fg='red')
                rcvMsgT = 'NO RESPONSE'
            else:
                self.ser.timeout = 3
                rcvMsg = self.ser.read(int.from_bytes(rcvMsg[1:], "big"))
                if self.ekeyEnVar.get():
                    encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                    rcvMsg = encryptor.decrypt(rcvMsg[:int(len(rcvMsg) / 16) * 16])

                rcvMsg = str(rcvMsg[8:])

                if rcvMsg[:15].find('ERROR') != -1:
                    self.edbPass2.config(fg='red')
                    if rcvMsg[rcvMsg.find('ERROR') + 6] == 'P':
                        rcvMsgT = 'FORMAT ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'PASSWORD ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'DATA ERROR'
                    else:
                        rcvMsgT = 'UNKNOWN ERROR'
                elif rcvMsg.find('CORRECT') == -1:
                    self.edbPass2.config(fg='red')
                    rcvMsgT = 'UNKNOWN ERROR'
                else:
                    rcvMsg = rcvMsg[rcvMsg.find('CORRECT'):]
                    self.edbPass2.config(fg='black')
                    rcvMsgT = rcvMsg[rcvMsg.find('(') + 1:rcvMsg.find(')')]
            rcvMsgT = ' ' + rcvMsgT
            self.edbPassVar.set(rcvMsgT)

        # ENC key
        elif a == 4:
            self.encKeyVar.set('')
            sendBuf += b'104315()\r\n\x00\x00\x00'
            if self.ekeyEnVar.get():
                encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                sendBuf = sendBuf[:3] + encryptor.encrypt(sendBuf[3:])
            sendBuf += self.calCrc(sendBuf[3:], 32)
            sendBuf += b'\x7E'
            self.ser.write(sendBuf)
            self.ser.timeout = 0.5
            rcvMsg = self.ser.read(3)
            if rcvMsg == b'':
                self.encKey2.config(fg='red')
                rcvMsgT = 'NO RESPONSE'
            else:
                self.ser.timeout = 3
                rcvMsg = self.ser.read(int.from_bytes(rcvMsg[1:], "big"))
                if self.ekeyEnVar.get():
                    encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                    rcvMsg = encryptor.decrypt(rcvMsg[:int(len(rcvMsg) / 16) * 16])

                rcvMsg = str(rcvMsg[8:])

                if rcvMsg[:15].find('ERROR') != -1:
                    self.encKey2.config(fg='red')
                    if rcvMsg[rcvMsg.find('ERROR') + 6] == 'P':
                        rcvMsgT = 'FORMAT ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'PASSWORD ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'DATA ERROR'
                    else:
                        rcvMsgT = 'UNKNOWN ERROR'
                elif rcvMsg.find('CORRECT') == -1:
                    self.encKey2.config(fg='red')
                    rcvMsgT = 'UNKNOWN ERROR'
                else:
                    rcvMsg = rcvMsg[rcvMsg.find('CORRECT'):]
                    self.encKey2.config(fg='black')
                    rcvMsgT = rcvMsg[rcvMsg.find('(') + 1:rcvMsg.find(')')]
            rcvMsgT = ' ' + rcvMsgT
            self.encKeyVar.set(rcvMsgT)

        # Filters
        elif a == 5:
            self.filters2.delete("0.0", END)
            sendBuf += b'010009()\r\n\x00\x00\x00'
            if self.ekeyEnVar.get():
                encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                sendBuf = sendBuf[:3] + encryptor.encrypt(sendBuf[3:])
            sendBuf += self.calCrc(sendBuf[3:], 32)
            sendBuf += b'\x7E'
            self.ser.write(sendBuf)
            self.ser.timeout = 0.5
            rcvMsg = self.ser.read(3)
            if rcvMsg == b'':
                self.filters2.config(fg='red')
                rcvMsgT = 'NO RESPONSE'
            else:
                self.ser.timeout = 3
                rcvMsg = self.ser.read(int.from_bytes(rcvMsg[1:], "big"))
                if self.ekeyEnVar.get():
                    encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                    rcvMsg = encryptor.decrypt(rcvMsg[:int(len(rcvMsg) / 16) * 16])

                rcvMsg = str(rcvMsg[8:])

                if rcvMsg[:15].find('ERROR') != -1:
                    self.filters2.config(fg='red')
                    if rcvMsg[rcvMsg.find('ERROR') + 6] == 'P':
                        rcvMsgT = 'FORMAT ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'PASSWORD ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'DATA ERROR'
                    else:
                        rcvMsgT = 'UNKNOWN ERROR'
                elif rcvMsg.find('CORRECT') == -1:
                    self.filters2.config(fg='red')
                    rcvMsgT = 'UNKNOWN ERROR'
                else:
                    rcvMsg = rcvMsg[rcvMsg.find('CORRECT'):]
                    self.filters2.config(fg='black')
                    rcvMsgT = rcvMsg[rcvMsg.find('(') + 1:rcvMsg.find(')')]
            rcvMsgT = rcvMsgT.replace(',', '\n')
            self.filters2.insert(INSERT, ' ' + rcvMsgT)

        # Check Connection
        elif a == 6:
            self.result1.set('')
            self.result2.set('')
            self.edbPassVar.set('')
            sendBuf += b'010005()\r\n\x00\x00\x00'
            if self.ekeyEnVar.get():
                encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                sendBuf = sendBuf[:3] + encryptor.encrypt(sendBuf[3:])
            sendBuf += self.calCrc(sendBuf[3:], 32)
            sendBuf += b'\x7E'
            self.ser.write(sendBuf)
            self.ser.timeout = 0.5
            rcvMsg = self.ser.read(3)
            if rcvMsg == b'':
                self.label10.config(fg='red')
                self.label11.config(fg='red')
                rcvMsgT = 'NO CONNECTION'
                rcvMsgT2 = ''
            else:
                self.ser.timeout = 3
                rcvMsg = self.ser.read(int.from_bytes(rcvMsg[1:], "big"))
                if self.ekeyEnVar.get():
                    encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                    rcvMsg = encryptor.decrypt(rcvMsg[:int(len(rcvMsg) / 16) * 16])

                rcvMsg = str(rcvMsg[8:])
                if rcvMsg[:15].find('ERROR') != -1:
                    self.label10.config(fg='red')
                    self.label11.config(fg='red')
                    if rcvMsg[rcvMsg.find('ERROR') + 6] == 'P':
                        rcvMsgT = 'NO CONNECTION'
                        rcvMsgT2 = ''
                    else:
                        self.label10.config(fg='green')
                        self.label11.config(fg='green')
                        rcvMsgT = 'CONNECTION OK'
                        rcvMsgT2 = ''
                elif rcvMsg.find('010005') == -1:
                    self.label10.config(fg='red')
                    self.label11.config(fg='red')
                    rcvMsgT = 'UNKNOWN ERROR'
                    rcvMsgT2 = ''
                else:
                    rcvMsg = rcvMsg[rcvMsg.find('010005'):]
                    self.label10.config(fg='green')
                    self.label11.config(fg='green')
                    rcvMsgT = 'CONNECTION OK'
                    rcvMsgT2 = rcvMsg[rcvMsg.find('(') + 1:rcvMsg.find(')')]

            self.result1.set(rcvMsgT)
            self.result2.set(rcvMsgT2)

        # ENC key En
        elif a == 8:
            self.ekeyEn_2_var.set('')
            sendBuf += b'104325()\r\n\x00\x00\x00'
            if self.ekeyEnVar.get():
                encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                sendBuf = sendBuf[:3] + encryptor.encrypt(sendBuf[3:])
            sendBuf += self.calCrc(sendBuf[3:], 32)
            sendBuf += b'\x7E'
            self.ser.write(sendBuf)
            self.ser.timeout = 0.5
            rcvMsg = self.ser.read(3)
            if rcvMsg == b'':
                self.ekeyEn_2.config(fg='red')
                rcvMsgT = 'NO RESPONSE'
            else:
                self.ser.timeout = 3
                rcvMsg = self.ser.read(int.from_bytes(rcvMsg[1:], "big"))
                if self.ekeyEnVar.get():
                    encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                    rcvMsg = encryptor.decrypt(rcvMsg[:int(len(rcvMsg) / 16) * 16])

                rcvMsg = str(rcvMsg[8:])
                if rcvMsg[:15].find('ERROR') != -1:
                    self.ekeyEn_2.config(fg='red')
                    if rcvMsg[rcvMsg.find('ERROR') + 6] == 'P':
                        rcvMsgT = 'FORMAT ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'PASSWORD ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'DATA ERROR'
                    else:
                        rcvMsgT = 'UNKNOWN ERROR'
                elif rcvMsg.find('CORRECT') == -1:
                    self.ekeyEn_2.config(fg='red')
                    rcvMsgT = 'UNKNOWN ERROR'
                else:
                    rcvMsg = rcvMsg[rcvMsg.find('CORRECT'):]
                    self.ekeyEn_2.config(fg='black')
                    rcvMsgT = rcvMsg[rcvMsg.find('(') + 4:rcvMsg.find(')')]
            rcvMsgT = ' ' + rcvMsgT
            self.ekeyEn_2_var.set(rcvMsgT)

        if portState:
            self.ser.close()

    def readAllObises(self):
        self.openPort()
        if self.portOpenSucc == 0:
            self.serialNumVar.set('')
            self.portVar.set('')
            self.ipVar.set('')
            self.edbPassVar.set('')
            self.encKeyVar.set('')
            self.filters2.delete("0.0", END)
            return
        self.readFunc(1, 0)
        time.sleep(0.1)
        self.readFunc(2, 0)
        time.sleep(0.1)
        self.readFunc(3, 0)
        time.sleep(0.1)
        self.readFunc(4, 0)
        time.sleep(0.1)
        self.readFunc(5, 0)
        time.sleep(0.1)
        self.readFunc(8, 0)
        self.ser.close()

    def writeFunc(self, a, portState):
        if portState:
            self.openPort()
            if self.portOpenSucc == 0:
                if a == 1:
                    self.serialNumVar.set('')
                elif a == 2:
                    self.portVar.set('')
                    self.ipVar.set('')
                elif a == 3:
                    self.edbPassVar.set('')
                elif a == 4:
                    self.encKeyVar.set('')
                elif a == 5:
                    self.filters2.delete("0.0", END)
                return

        if len(self.passVar.get().replace(' ', '')) != 8:
            self.serialNumVar.set('')
            self.label10.config(fg='red')
            self.result1.set('Password length!')
            self.ser.close()
            return

        if a == 1:
            self.serialNumVar.set(' ')
            data = b'W5\x02010000(' + bytes(self.serialNum.get().replace(' ', ''), 'utf-8') + b')\r\n'
            dataL = len(data) + 12
            totLen = math.ceil((dataL + 4) / 16) * 16
            totLen += 3
            sendStr = b'\x7E'
            sendStr += bytes([int(totLen / 256), totLen % 256])
            sendStr += b'\x00\x03'
            sendStr += bytes([int(dataL / 256), dataL % 256])
            sendStr += b'\xFF\x23\x00\x00'
            sendStr += bytes(self.passVar.get().replace(' ', ''), 'utf-8')
            sendStr += data
            sendStr += bytes(totLen - dataL - 7)
            if self.ekeyEnVar.get():
                encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                sendStr = sendStr[:3] + encryptor.encrypt(sendStr[3:])
            sendStr += self.calCrc(sendStr[3:], totLen - 3)
            sendStr += b'\x7E'
            self.ser.write(sendStr)
            self.ser.timeout = 0.5
            rcvMsg = self.ser.read(3)
            if rcvMsg == b'':
                self.serialNum2.config(fg='red')
                rcvMsgT = 'NO RESPONSE'
            else:
                self.ser.timeout = 3
                rcvMsg = self.ser.read(int.from_bytes(rcvMsg[1:], "big"))
                if self.ekeyEnVar.get():
                    encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                    rcvMsg = encryptor.decrypt(rcvMsg[:int(len(rcvMsg) / 16) * 16])

                rcvMsg = str(rcvMsg[8:])
                if rcvMsg[:15].find('ERROR') != -1:
                    self.serialNum2.config(fg='red')
                    if rcvMsg[rcvMsg.find('ERROR') + 6] == 'P':
                        rcvMsgT = 'FORMAT ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'PASSWORD ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'DATA ERROR'
                    else:
                        rcvMsgT = 'UNKNOWN ERROR'
                elif rcvMsg.find('CORRECT') == -1:
                    self.serialNum2.config(fg='red')
                    rcvMsgT = 'UNKNOWN ERROR'
                else:
                    rcvMsg = rcvMsg[rcvMsg.find('CORRECT'):]
                    rcvMsgT = rcvMsg[rcvMsg.find('(') + 1:rcvMsg.find(')')]
                    if rcvMsg.find('OK') != -1:
                        self.serialNum2.config(fg='green')
                    else:
                        self.serialNum2.config(fg='red')
            rcvMsgT = ' ' + rcvMsgT
            self.serialNumVar.set(rcvMsgT)

        elif a == 2:
            self.ipVar.set('')
            self.portVar.set('')
            data = b'W5\x02102025("'
            data += bytes(self.ip.get().replace(' ', ''), 'utf-8')
            data += b'",'
            data += bytes(self.port.get().replace(' ', ''), 'utf-8')
            data +=b')\r\n'
            dataL = len(data) + 12
            totLen = math.ceil((dataL + 4) / 16) * 16
            totLen += 3
            sendStr = b'\x7E'
            sendStr += bytes([int(totLen / 256), totLen % 256])
            sendStr += b'\x00\x03'
            sendStr += bytes([int(dataL / 256), dataL % 256])
            sendStr += b'\xFF\x23\x00\x00'
            sendStr += bytes(self.passVar.get().replace(' ', ''), 'utf-8')
            sendStr += data
            sendStr += bytes(totLen - dataL - 7)
            if self.ekeyEnVar.get():
                encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                sendStr = sendStr[:3] + encryptor.encrypt(sendStr[3:])
            sendStr += self.calCrc(sendStr[3:], totLen - 3)
            sendStr += b'\x7E'
            self.ser.write(sendStr)
            self.ser.timeout = 0.5
            rcvMsg = self.ser.read(3)
            if rcvMsg == b'':
                self.ip2.config(fg='red')
                self.port2.config(fg='red')
                rcvMsgT = 'NO RESPONSE'
            else:
                self.ser.timeout = 3
                rcvMsg = self.ser.read(int.from_bytes(rcvMsg[1:], "big"))
                if self.ekeyEnVar.get():
                    encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                    rcvMsg = encryptor.decrypt(rcvMsg[:int(len(rcvMsg) / 16) * 16])

                rcvMsg = str(rcvMsg[8:])
                if rcvMsg[:15].find('ERROR') != -1:
                    self.ip2.config(fg='red')
                    self.port2.config(fg='red')
                    if rcvMsg[rcvMsg.find('ERROR') + 6] == 'P':
                        rcvMsgT = 'FORMAT ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'PASSWORD ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'DATA ERROR'
                    else:
                        rcvMsgT = 'UNKNOWN ERROR'
                elif rcvMsg.find('CORRECT') == -1:
                    self.ip2.config(fg='red')
                    self.port2.config(fg='red')
                    rcvMsgT = 'UNKNOWN ERROR'
                else:
                    rcvMsg = rcvMsg[rcvMsg.find('CORRECT'):]
                    rcvMsgT = rcvMsg[rcvMsg.find('(') + 1:rcvMsg.find(')')]
                    if rcvMsg.find('OK') != -1:
                        self.ip2.config(fg='green')
                        self.port2.config(fg='green')
                    else:
                        self.ip2.config(fg='red')
                        self.port2.config(fg='red')
            rcvMsgT = ' ' + rcvMsgT
            self.ipVar.set(rcvMsgT)
            self.portVar.set(rcvMsgT)

        # GW password
        elif a == 3:
            self.edbPassVar.set('')
            data = b'W5\x02104305(' + bytes(self.edbPass.get().replace(' ', ''), 'utf-8') + b')\r\n'
            dataL = len(data) + 12
            totLen = math.ceil((dataL + 4) / 16) * 16
            totLen += 3
            sendStr = b'\x7E'
            sendStr += bytes([int(totLen / 256), totLen % 256])
            sendStr += b'\x00\x03'
            sendStr += bytes([int(dataL / 256), dataL % 256])
            sendStr += b'\xFF\x23\x00\x00'
            sendStr += bytes(self.passVar.get().replace(' ', ''), 'utf-8')
            # sendStr += b'\x01'
            sendStr += data
            sendStr += bytes(totLen - dataL - 7)
            if self.ekeyEnVar.get():
                encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                sendStr = sendStr[:3] + encryptor.encrypt(sendStr[3:])
            sendStr += self.calCrc(sendStr[3:], totLen - 3)
            sendStr += b'\x7E'
            self.ser.write(sendStr)
            self.ser.timeout = 0.5
            rcvMsg = self.ser.read(3)
            if rcvMsg == b'':
                self.edbPass2.config(fg='red')
                rcvMsgT = 'NO RESPONSE'
            else:
                self.ser.timeout = 3
                rcvMsg = self.ser.read(int.from_bytes(rcvMsg[1:], "big"))
                if self.ekeyEnVar.get():
                    encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                    rcvMsg = encryptor.decrypt(rcvMsg[:int(len(rcvMsg) / 16) * 16])

                rcvMsg = str(rcvMsg[8:])
                if rcvMsg[:15].find('ERROR') != -1:
                    self.edbPass2.config(fg='red')
                    if rcvMsg[rcvMsg.find('ERROR') + 6] == 'P':
                        rcvMsgT = 'FORMAT ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'PASSWORD ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'DATA ERROR'
                    else:
                        rcvMsgT = 'UNKNOWN ERROR'
                elif rcvMsg.find('CORRECT') == -1:
                    self.edbPass2.config(fg='red')
                    rcvMsgT = 'UNKNOWN ERROR'
                else:
                    rcvMsg = rcvMsg[rcvMsg.find('CORRECT'):]
                    rcvMsgT = rcvMsg[rcvMsg.find('(') + 1:rcvMsg.find(')')]
                    if rcvMsg.find('OK') != -1:
                        self.edbPass2.config(fg='green')
                    else:
                        self.edbPass2.config(fg='red')
            rcvMsgT = ' ' + rcvMsgT
            self.edbPassVar.set(rcvMsgT)

        elif a == 4:
            self.encKeyVar.set('')
            data = b'W5\x02104315(' + bytes(self.encKey_1.get().replace(' ', ''), 'utf-8') + b')\r\n'
            dataL = len(data) + 12
            totLen = math.ceil((dataL + 4) / 16) * 16
            totLen += 3
            sendStr = b'\x7E'
            sendStr += bytes([int(totLen / 256), totLen % 256])
            sendStr += b'\x00\x03'
            sendStr += bytes([int(dataL / 256), dataL % 256])
            sendStr += b'\xFF\x23\x00\x00'
            sendStr += bytes(self.passVar.get().replace(' ', ''), 'utf-8')
            sendStr += data
            sendStr += bytes(totLen - dataL - 7)
            if self.ekeyEnVar.get():
                encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                sendStr = sendStr[:3] + encryptor.encrypt(sendStr[3:])
            sendStr += self.calCrc(sendStr[3:], totLen - 3)
            sendStr += b'\x7E'
            self.ser.write(sendStr)
            self.ser.timeout = 0.5
            rcvMsg = self.ser.read(3)
            if rcvMsg == b'':
                self.encKey2.config(fg='red')
                rcvMsgT = 'NO RESPONSE'
            else:
                self.ser.timeout = 3
                rcvMsg = self.ser.read(int.from_bytes(rcvMsg[1:], "big"))
                if self.ekeyEnVar.get():
                    encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                    rcvMsg = encryptor.decrypt(rcvMsg[:int(len(rcvMsg) / 16) * 16])

                rcvMsg = str(rcvMsg[8:])
                if rcvMsg[:15].find('ERROR') != -1:
                    self.encKey2.config(fg='red')
                    if rcvMsg[rcvMsg.find('ERROR') + 6] == 'P':
                        rcvMsgT = 'FORMAT ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'PASSWORD ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'DATA ERROR'
                    else:
                        rcvMsgT = 'UNKNOWN ERROR'
                elif rcvMsg.find('CORRECT') == -1:
                    self.encKey2.config(fg='red')
                    rcvMsgT = 'UNKNOWN ERROR'
                else:
                    rcvMsg = rcvMsg[rcvMsg.find('CORRECT'):]
                    rcvMsgT = rcvMsg[rcvMsg.find('(') + 1:rcvMsg.find(')')]
                    if rcvMsg.find('OK') != -1:
                        self.encKey2.config(fg='green')
                    else:
                        self.encKey2.config(fg='red')
            rcvMsgT = ' ' + rcvMsgT
            self.encKeyVar.set(rcvMsgT)

        elif a == 5:
            self.filters2.delete("0.0", END)
            data = b'W5\x02010009(' + bytes(str(self.filters.get("0.0", END)).replace('\n', ','), 'utf-8')[:str(self.filters.get("0.0", END)).__len__()-1] + b')\r\n'
            dataL = len(data) + 12
            totLen = math.ceil((dataL + 4) / 16) * 16
            totLen += 3
            sendStr = b'\x7E'
            sendStr += bytes([int(totLen / 256), totLen % 256])
            sendStr += b'\x00\x03'
            sendStr += bytes([int(dataL / 256), dataL % 256])
            sendStr += b'\xFF\x23\x00\x00'
            sendStr += bytes(self.passVar.get().replace(' ', ''), 'utf-8')
            sendStr += data
            sendStr += bytes(totLen - dataL - 7)
            if self.ekeyEnVar.get():
                encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                sendStr = sendStr[:3] + encryptor.encrypt(sendStr[3:])
            sendStr += self.calCrc(sendStr[3:], totLen - 3)
            sendStr += b'\x7E'
            self.ser.write(sendStr)
            self.ser.timeout = 5
            rcvMsg = self.ser.read(3)
            if rcvMsg == b'':
                self.filters2.config(fg='red')
                rcvMsgT = 'NO RESPONSE'
            else:
                self.ser.timeout = 3
                rcvMsg = self.ser.read(int.from_bytes(rcvMsg[1:], "big"))
                if self.ekeyEnVar.get():
                    encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                    rcvMsg = encryptor.decrypt(rcvMsg[:int(len(rcvMsg) / 16) * 16])

                rcvMsg = str(rcvMsg[8:])
                if rcvMsg[:15].find('ERROR') != -1:
                    self.filters2.config(fg='red')
                    if rcvMsg[rcvMsg.find('ERROR') + 6] == 'P':
                        rcvMsgT = 'FORMAT ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'PASSWORD ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'DATA ERROR'
                    else:
                        rcvMsgT = 'UNKNOWN ERROR'
                elif rcvMsg.find('CORRECT') == -1:
                    self.filters2.config(fg='red')
                    rcvMsgT = 'UNKNOWN ERROR'
                else:
                    rcvMsg = rcvMsg[rcvMsg.find('CORRECT'):]
                    rcvMsgT = rcvMsg[rcvMsg.find('(') + 1:rcvMsg.find(')')]
                    if rcvMsg.find('OK') != -1:
                        self.filters2.config(fg='green')
                    else:
                        self.filters2.config(fg='red')
            self.filters2.insert(INSERT, ' ' + rcvMsgT)

        elif a == 6:
            self.serialNumVar.set(' ')
            data = b'W5\x02101015(' + bytes(self.sms1.get().replace(' ', ''), 'utf-8') + b')\r\n'
            dataL = len(data) + 12
            totLen = math.ceil((dataL + 4) / 16) * 16
            totLen += 3
            sendStr = b'\x7E'
            sendStr += bytes([int(totLen / 256), totLen % 256])
            sendStr += b'\x00\x03'
            sendStr += bytes([int(dataL / 256), dataL % 256])
            sendStr += b'\xFF\x23\x00\x00'
            sendStr += bytes(self.passVar.get().replace(' ', ''), 'utf-8')
            sendStr += data
            sendStr += bytes(totLen - dataL - 7)
            if self.ekeyEnVar.get():
                encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                sendStr = sendStr[:3] + encryptor.encrypt(sendStr[3:])
            sendStr += self.calCrc(sendStr[3:], totLen - 3)
            sendStr += b'\x7E'
            self.ser.write(sendStr)
            self.ser.timeout = 0.5
            rcvMsg = self.ser.read(3)
            if rcvMsg == b'':
                self.sms2.config(fg='red')
                rcvMsgT = 'NO RESPONSE'
            else:
                self.ser.timeout = 3
                rcvMsg = self.ser.read(int.from_bytes(rcvMsg[1:], "big"))
                if self.ekeyEnVar.get():
                    encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                    rcvMsg = encryptor.decrypt(rcvMsg[:int(len(rcvMsg) / 16) * 16])

                rcvMsg = str(rcvMsg[8:])
                if rcvMsg[:15].find('ERROR') != -1:
                    self.sms2.config(fg='red')
                    if rcvMsg[rcvMsg.find('ERROR') + 6] == 'P':
                        rcvMsgT = 'FORMAT ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'PASSWORD ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'DATA ERROR'
                    else:
                        rcvMsgT = 'UNKNOWN ERROR'
                elif rcvMsg.find('CORRECT') == -1:
                    self.sms2.config(fg='red')
                    rcvMsgT = 'UNKNOWN ERROR'
                else:
                    rcvMsg = rcvMsg[rcvMsg.find('CORRECT'):]
                    rcvMsgT = rcvMsg[rcvMsg.find('(') + 1:rcvMsg.find(')')]
                    if rcvMsg.find('OK') != -1:
                        self.sms2.config(fg='green')
                    else:
                        self.sms2.config(fg='red')
            rcvMsgT = ' ' + rcvMsgT
            self.smsVar.set(rcvMsgT)

        elif a == 8:
            self.ekeyEn_2_var.set('')
            if self.ekeyEn_1.get().replace(' ', '') != '1' and self.ekeyEn_1.get().replace(' ', '') != '0':
                self.ekeyEn_2.config(fg='red')
                self.ekeyEn_2_var.set(' BAD DATA')
                if portState:
                    self.ser.close()
                return
            data = b'W5\x02104325(' + bytes([int(self.ekeyEn_1.get().replace(' ', ''))]) + b')\r\n'
            dataL = len(data) + 12
            totLen = math.ceil((dataL + 4) / 16) * 16
            totLen += 3
            sendStr = b'\x7E'
            sendStr += bytes([int(totLen / 256), totLen % 256])
            sendStr += b'\x00\x03'
            sendStr += bytes([int(dataL / 256), dataL % 256])
            sendStr += b'\xFF\x23\x00\x00'
            sendStr += bytes(self.passVar.get().replace(' ', ''), 'utf-8')
            sendStr += data
            sendStr += bytes(totLen - dataL - 7)
            if self.ekeyEnVar.get():
                encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                sendStr = sendStr[:3] + encryptor.encrypt(sendStr[3:])
            sendStr += self.calCrc(sendStr[3:], totLen - 3)
            sendStr += b'\x7E'
            self.ser.write(sendStr)
            self.ser.timeout = 0.5
            rcvMsg = self.ser.read(3)
            if rcvMsg == b'':
                self.ekeyEn_2.config(fg='red')
                rcvMsgT = 'NO RESPONSE'
            else:
                self.ser.timeout = 3
                rcvMsg = self.ser.read(int.from_bytes(rcvMsg[1:], "big"))
                if self.ekeyEnVar.get():
                    encryptor = AES.new(bytes(self.ekeyVar.get().replace(' ', ''), 'utf-8'), self.encMode)
                    rcvMsg = encryptor.decrypt(rcvMsg[:int(len(rcvMsg) / 16) * 16])

                rcvMsg = str(rcvMsg[8:])
                if rcvMsg[:15].find('ERROR') != -1:
                    self.ekeyEn_2.config(fg='red')
                    if rcvMsg[rcvMsg.find('ERROR') + 6] == 'P':
                        rcvMsgT = 'FORMAT ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'PASSWORD ERROR'
                    elif rcvMsg[rcvMsg.find('ERROR') + 6] == 'Q':
                        rcvMsgT = 'DATA ERROR'
                    else:
                        rcvMsgT = 'UNKNOWN ERROR'
                elif rcvMsg.find('CORRECT') == -1:
                    self.ekeyEn_2.config(fg='red')
                    rcvMsgT = 'UNKNOWN ERROR'
                else:
                    rcvMsg = rcvMsg[rcvMsg.find('CORRECT'):]
                    rcvMsgT = rcvMsg[rcvMsg.find('(') + 1:rcvMsg.find(')')]
                    if rcvMsg.find('OK') != -1:
                        self.ekeyEn_2.config(fg='green')
                    else:
                        self.ekeyEn_2.config(fg='red')
            rcvMsgT = ' ' + rcvMsgT
            self.ekeyEn_2_var.set(rcvMsgT)

        if portState:
            self.ser.close()



    def writeAllObises(self):
        self.openPort()
        if self.portOpenSucc == 0:
            self.serialNumVar.set('')
            self.portVar.set('')
            self.ipVar.set('')
            self.edbPassVar.set('')
            self.encKeyVar.set('')
            self.filters2.delete("0.0", END)
            return
        self.writeFunc(1, 0)
        time.sleep(0.1)
        self.writeFunc(2, 0)
        time.sleep(0.1)
        self.writeFunc(3, 0)
        time.sleep(0.1)
        self.writeFunc(4, 0)
        time.sleep(0.1)
        self.writeFunc(5, 0)
        time.sleep(0.1)
        self.writeFunc(8, 0)
        self.ser.close()

    def openPort(self):
        try:
            self.ser = serial.Serial(self.comBox.get(), baudrate=19200, bytesize=8, timeout=0.5, parity=serial.PARITY_EVEN, rtscts=0)
            if self.result1.get().find('Can not open') != -1:
                self.result1.set('')
            self.portOpenSucc = 1
        except:
            self.result1.set('')
            self.result2.set('')
            self.label10.config(fg='red')
            self.result1.set('Can not open the port!')
            self.portOpenSucc = 0

    def calCrc(self, inStr, inLen):
        dnpCrcTable = [
            0x0000, 0x3D65, 0x7ACA, 0x47AF, 0xF594, 0xC8F1, 0x8F5E, 0xB23B, 0xD64D, 0xEB28, 0xAC87, 0x91E2, 0x23D9,
            0x1EBC, 0x5913, 0x6476, 0x91FF, 0xAC9A, 0xEB35, 0xD650, 0x646B, 0x590E, 0x1EA1, 0x23C4, 0x47B2, 0x7AD7,
            0x3D78, 0x001D, 0xB226, 0x8F43, 0xC8EC, 0xF589, 0x1E9B, 0x23FE, 0x6451, 0x5934, 0xEB0F, 0xD66A, 0x91C5,
            0xACA0, 0xC8D6, 0xF5B3, 0xB21C, 0x8F79, 0x3D42, 0x0027, 0x4788, 0x7AED, 0x8F64, 0xB201, 0xF5AE, 0xC8CB,
            0x7AF0, 0x4795, 0x003A, 0x3D5F, 0x5929, 0x644C, 0x23E3, 0x1E86, 0xACBD, 0x91D8, 0xD677, 0xEB12, 0x3D36,
            0x0053, 0x47FC, 0x7A99, 0xC8A2, 0xF5C7, 0xB268, 0x8F0D, 0xEB7B, 0xD61E, 0x91B1, 0xACD4, 0x1EEF, 0x238A,
            0x6425, 0x5940, 0xACC9, 0x91AC, 0xD603, 0xEB66, 0x595D, 0x6438, 0x2397, 0x1EF2, 0x7A84, 0x47E1, 0x004E,
            0x3D2B, 0x8F10, 0xB275, 0xF5DA, 0xC8BF, 0x23AD, 0x1EC8, 0x5967, 0x6402, 0xD639, 0xEB5C, 0xACF3, 0x9196,
            0xF5E0, 0xC885, 0x8F2A, 0xB24F, 0x0074, 0x3D11, 0x7ABE, 0x47DB, 0xB252, 0x8F37, 0xC898, 0xF5FD, 0x47C6,
            0x7AA3, 0x3D0C, 0x0069, 0x641F, 0x597A, 0x1ED5, 0x23B0, 0x918B, 0xACEE, 0xEB41, 0xD624, 0x7A6C, 0x4709,
            0x00A6, 0x3DC3, 0x8FF8, 0xB29D, 0xF532, 0xC857, 0xAC21, 0x9144, 0xD6EB, 0xEB8E, 0x59B5, 0x64D0, 0x237F,
            0x1E1A, 0xEB93, 0xD6F6, 0x9159, 0xAC3C, 0x1E07, 0x2362, 0x64CD, 0x59A8, 0x3DDE, 0x00BB, 0x4714, 0x7A71,
            0xC84A, 0xF52F, 0xB280, 0x8FE5, 0x64F7, 0x5992, 0x1E3D, 0x2358, 0x9163, 0xAC06, 0xEBA9, 0xD6CC, 0xB2BA,
            0x8FDF, 0xC870, 0xF515, 0x472E, 0x7A4B, 0x3DE4, 0x0081, 0xF508, 0xC86D, 0x8FC2, 0xB2A7, 0x009C, 0x3DF9,
            0x7A56, 0x4733, 0x2345, 0x1E20, 0x598F, 0x64EA, 0xD6D1, 0xEBB4, 0xAC1B, 0x917E, 0x475A, 0x7A3F, 0x3D90,
            0x00F5, 0xB2CE, 0x8FAB, 0xC804, 0xF561, 0x9117, 0xAC72, 0xEBDD, 0xD6B8, 0x6483, 0x59E6, 0x1E49, 0x232C,
            0xD6A5, 0xEBC0, 0xAC6F, 0x910A, 0x2331, 0x1E54, 0x59FB, 0x649E, 0x00E8, 0x3D8D, 0x7A22, 0x4747, 0xF57C,
            0xC819, 0x8FB6, 0xB2D3, 0x59C1, 0x64A4, 0x230B, 0x1E6E, 0xAC55, 0x9130, 0xD69F, 0xEBFA, 0x8F8C, 0xB2E9,
            0xF546, 0xC823, 0x7A18, 0x477D, 0x00D2, 0x3DB7, 0xC83E, 0xF55B, 0xB2F4, 0x8F91, 0x3DAA, 0x00CF, 0x4760,
            0x7A05, 0x1E73, 0x2316, 0x64B9, 0x59DC, 0xEBE7, 0xD682, 0x912D, 0xAC48]

        crc = 0
        for i in range(inLen):
            crc = ((crc << 8) ^ dnpCrcTable[((crc >> 8) ^ inStr[i]) & 0x00FF]) & 0xFFFF
        crc ^= 0xFFFF
        return bytes([int(crc / 256) & 0xFF, crc & 0xFF])


if __name__ == "__main__":
    tool = Tk()
    tool.title('GateWay Configuration V1.1')
    preGui(tool)
    tool.mainloop()

