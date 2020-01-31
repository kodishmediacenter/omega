#!/usr/bin/python

from paramiko import SSHClient
import paramiko

def data():

        Nome='{}'.format(E1.get())
        Senha='{}'.format(E2.get())
        Dias='{}'.format(E3.get())
        
        ssh = SSH()
        ssh.exec_cmd("mkdir /var/www/html/"+Nome+"")
        ssh.exec_cmd("cd /var/www/html/"+Nome+"")
        ssh.exec_cmd("mkdir "+Senha+"")
        ssh.exec_cmd("ln -s /var/www/core /var/www/html/"+Nome+"/"+Senha+"")
        ssh.exec_cmd('echo "rm -r /var/www/html/'+Nome+'" > /var/www/core/'+Nome+'.txt')
        ssh.exec_cmd('at -f /var/www/core/'+Nome+'.txt now +'+Dias+' days')    

class SSH:
    def __init__(self):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()

        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname='104.41.42.124',username='keysey',password='keysey')

    def exec_cmd(self,cmd):
        stdin,stdout,stderr = self.ssh.exec_command(cmd)
        if stderr.channel.recv_exit_status() != 0:
            print (stderr.read())
        else:
            print (stdout.read())

from tkinter import *
from tkinter.ttk import Combobox

top = Tk()
L1 = Label(top, text = "Nome")
L1.place(x = 10,y = 10)
E1 = Entry(top, bd = 3)
E1.place(x = 130,y = 10)

L2 = Label(top,text = "Senha")
L2.place(x = 10,y = 50)
E2 = Entry(top,bd = 3)
E2.place(x = 130,y = 50)

L3 = Label(top,text = "Quantidades de Dias")
L3.place(x = 10,y = 90)
E3 = Entry(top,bd = 3)
E3.place(x = 130,y = 90)

b=Button(text='Cadastrar', command=data)
b.pack(side=LEFT)

top.geometry("500x500+10+10")        
    
