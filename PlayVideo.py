
from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSignal
import pafy
import vlc
import threading
import time
from CheckVideoState import CheckVideoState

class PlayVideo(threading.Thread,QtCore.QObject):
    finished = QtCore.pyqtSignal()

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
        self.checkState = CheckVideoState()
        self.clicked = False

    def run(self):
        url = self.urls
        for u in self.urls :
            video = pafy.new(u)
            self.videos.append(video)

        for v in self.videos:
            b = v.streams[0]
            self.bests.append(b)
        count = 0
        for j in range(0,len(self.urls)):
            playurl = self.bests[j].url
            self.playUrls.append(playurl)
            

        instance = vlc.Instance()
        self.player = instance.media_player_new()
        for i in range(0,len(self.playUrls)):   
            media = instance.media_new(self.playUrls[i])
            self.medias.append(media)

        self.getThumbnails()
        self.finished.emit()
        self.q = 0
        while True:
            self.autoNext(self.q)
            self.q = self.selectedNum
            self.clicked =False

    def autoNext(self,t):

        for m in range(t,len(self.medias)):

            self.player.set_media(self.medias[m])
            a = True
            self.player.play()
            while a:
                time.sleep(0.5)               
                if self.clicked == True:
                    print("dddddddddd")
                    a = False
                    clicked2 = True
                if str(self.player.get_state()) == 'State.Ended':
                    a = False
                    clicked2 = False
            if clicked2 == True:
                break        
            if m == len(self.medias)-1 and clicked2 == False:
                    self.selectedNum = 0
                

    def getUrl(self,id,playlistName):
        self.cur.execute("SELECT url FROM video WHERE id='"+id+"' AND playlistName='"+playlistName+"';")
        urls = self.cur.fetchall()
        for d in range (0,len(urls)):
            self.urls.append(urls[d][0])

    def getThumbnails(self):
        
        for url in self.urls :
            thumbnail = pafy.new(url)
            value = thumbnail.getbestthumb()
            self.thumbnails.append(str(value))

    def changeVolum(self,value):

        self.player.audio_set_volume(value)

    def choiceVideo(self,state,mediaNum):
        
        self.clicked = True
        self.selectedNum = mediaNum
        
    
    # def playAnother(self,num):
        
    #     self.q = num


    def endPlayer(self):
        self.checkState.start(self.player)

#리스트 클릭하면 신호주고 동영상 여기 스레드에서 계속 실행하면서 연속재생 해결
#중요한건 다른 영상 눌렀을 때 다른 미디어 셋팅하고 동영상을 for 문을 탈출해서 실행시켜야함