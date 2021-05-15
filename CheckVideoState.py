import threading
import vlc
import time
from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSignal

class CheckVideoState(threading.Thread,QtCore.QObject):
    
    ended = QtCore.pyqtSignal()

    def __init__(self):
        QtCore.QObject.__init__(self)
        threading.Thread.__init__(self)
        self.checkResult = False
    
    def run(self,player):

        while True:
            time.sleep(1)  
            self.getVideoState(player) 
            if self.checkResult == True:
                break

    def getVideoState(self,player):

        if player.get_state() == "Ended":
            self.ended.emit()
            self.checkResult = True