
from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSignal
from pynput import keyboard
from KeyBoard import KeyBoard
import pafy
import vlc
import threading
import time

class PlayVideo(threading.Thread,QtCore.QObject):
    finished = QtCore.pyqtSignal()
    played = QtCore.pyqtSignal()
    def __init__(self,conn):
        QtCore.QObject.__init__(self)
        threading.Thread.__init__(self)
        self.conn = conn
        self.cur = self.conn.cursor()
        self.thumbnails = []
        self.urls = []
        self.videos = []
        self.bests = []
        self.playUrls = []
        self.medias = []
        self.titles= []
        self.clicked = False
        self.goBackToPlaylist = 0
        self.selectedNum = 0
        self.lastClicked = False
        self.playingVideoNum = 0
        
    def run(self):
        instance = vlc.Instance()
        self.player = instance.media_player_new()
        keyboard = KeyBoard(self.player)
        keyboard.getKeyBoard()
    
        while True:
            try:
                if self.goBackToPlaylist == False:
                
                    for u in self.urls :
                        video = pafy.new(u)
                        self.videos.append(video)

                    for v in self.videos:
                        b = v.streams[0]
                        self.bests.append(b)

                    for j in range(0,len(self.urls)):
                        playurl = self.bests[j].url
                        self.playUrls.append(playurl)       

                    
                    for i in range(0,len(self.playUrls)):   
                        media = instance.media_new(self.playUrls[i])
                        self.medias.append(media)

                    self.getThumbnails()
                    self.finished.emit()
                    self.q = 0
                    while True:
                        if self.goBackToPlaylist == True:
                            break
                        else:
                            self.autoNext(self.q)
                            self.q = self.selectedNum
                            self.clicked =False
                elif self.goBackToPlaylist == True:
                    time.sleep(0.5)
            except:
                pass 
            
             
                
                
    #뒤로가기 누르면 play쪽 나가고 전체에 if 줘서 플레이 리스트 클릭하면 실행
    
    def autoNext(self,t):
        clicked2 = False
        for m in range(t,len(self.medias)):
            self.player.set_media(self.medias[m])
            self.title = self.titles[m]
            self.playingVideoNum = m
            self.played.emit()
            a = True
            self.player.play()         
            while a:
                time.sleep(0.5)
                if self.goBackToPlaylist == True: #뒤로가기 클릭
                    self.player.stop()
                    a = False
                    clicked2 = True

                if self.clicked == True: #다른 영상 클릭 
                    
                    a = False
                    clicked2 = True

                if str(self.player.get_state()) == 'State.Ended': #영상재생끝나면 
                    a = False
                    clicked2 = False
                
                if self.lastClicked == True: #이전버튼 누르면 
                    a = False
                    clicked2 = True
            
            if self.lastClicked == True:
                if m == 0:
                    self.selectedNum = 0
                    self.lastClicked = False
                else:    
                    self.selectedNum = m-1
                    self.lastClicked = False
            
            if clicked2 == True:
                break        

            if m == len(self.medias)-1 and clicked2 == False and self.lastClicked == False:
                    self.selectedNum = 0
            

    def getUrl(self,id,playlistName):
        self.cur.execute("SELECT url FROM video WHERE id='"+id+"' AND playlistName='"+playlistName+"';")
        urls = self.cur.fetchall()
        for d in range (0,len(urls)):
            self.urls.append(urls[d][0])

    def getThumbnails(self):
        
        for url in self.urls :
            pf = pafy.new(url)
            thumbNail = pf.getbestthumb()
            title = pf.title
            self.thumbnails.append(str(thumbNail))
            self.titles.append(str(title))

    def changeVolum(self,value):

        self.player.audio_set_volume(value)

    def choiceVideo(self,state,mediaNum):
        
        self.clicked = True
        self.selectedNum = mediaNum

    def initPlayer(self):
        self.thumbnails = []
        self.urls = []
        self.videos = []
        self.bests = []
        self.playUrls = []
        self.medias = []
        self.titles= []
        self.clicked = False
        self.selectedNum = 0
    
     #다음영상
    def clickNextButton(self):
        self.player.set_time(self.player.get_length())

    def clickLastButton(self):
        self.lastClicked = True

    def pause(self):
        self.player.pause()

    def play(self):
        self.player.play()