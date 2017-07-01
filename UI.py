from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtNetwork import *
import re
import os
import sys
import socket
import subprocess
class UI:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.tWindow = QWidget()
        self.tWindow.setWindowTitle("Assignment")
        
        self.box = QVBoxLayout()
        
        self.dstBox = QHBoxLayout()
        
        self.dstLabel = QLabel("IP/URL")
        self.dstInput = QLineEdit()
        self.dstInput.setPlaceholderText("IP address")
        
        self.portLabel = QLabel("Port")
        self.portInput = QLineEdit()
        self.portInput.setPlaceholderText("Port number")
        
        self.pingButton = QPushButton("Ping")
        self.pingButton.clicked.connect(self.pingAction)
        
        self.dstBox.addWidget(self.dstLabel)
        self.dstBox.addWidget(self.dstInput)
        self.dstBox.addWidget(self.portLabel)
        self.dstBox.addWidget(self.portInput)
        self.dstBox.addWidget(self.pingButton)
        
        self.b1Box = QHBoxLayout()
        
        self.routeButton = QPushButton("Traceroute")
        self.portButton = QPushButton("List Port")
        self.portButton.clicked.connect(self.portAction)
        
        self.b1Box.addWidget(self.routeButton)
        self.b1Box.addWidget(self.portButton)
        
        self.b2Box = QHBoxLayout()
        
        self.scanButton = QPushButton("Scan Hosts")
        self.sendButton = QPushButton("Send Packet")
        
        self.b2Box.addWidget(self.scanButton)
        self.b2Box.addWidget(self.sendButton)
        
        self.resultBox = QVBoxLayout()
        
        self.resultLabel = QLabel("Result:")
        self.resultWindow = QListWidget()
        
        
        self.resultBox.addWidget(self.resultLabel)
        self.resultBox.addWidget(self.resultWindow)
        

        self.box.addLayout(self.dstBox)
        self.box.addLayout(self.b1Box)
        self.box.addLayout(self.b2Box)
        self.box.addLayout(self.resultBox)
        
        self.tWindow.setLayout(self.box)
        
        
        self.tWindow.show()
        sys.exit(self.app.exec_())                                                                                                                                                  

    def portAction(self):
        interfaces = QNetworkInterface()
        self.resultWindow.addItem(interfaces)
        
    def pingAction(self):
        
        cmd = "ping " +  self.dstInput.text() + " -c 4"
        p = subprocess.Popen(cmd,  stdout=subprocess.PIPE,  stderr = subprocess.STDOUT,  shell = True)
        
        pingTime = 0
        
        while True:
            line = p.stdout.readline()
            matchObj = re.match(r"(.*) bytes from (.*?) .*",  str(line),  re.M|re.I)
            if matchObj:
                pingTime += 1
            if not line:
                break
        
        
        if pingTime != 0:
            self.resultWindow.addItem("Successfully pinged the host: " + self.dstInput.text() + " for " + str(pingTime) + " times")
        else:
            self.resultWindow.addItem("Failed to ping the host: " + self.dstInput.text())
        self.resultWindow.addItem("End")
        p.kill()
        """for line in iter(p.stdout.readline,  b''):
            self.resultWindow.addItem(str(line))
        p.stdout.close()                                                                           
        p.kill()"""


s = UI()
