
from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSignal
import pafy
import vlc
import threading
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
        self.player.set_media_list(self.medialist)
        self.medialist = instance.media_list_new()
        for i in range(0,len(self.playUrls)):   
            media = instance.media_new(self.playUrls[i])
            # self.medias.append(media)
            self.medialist.add_media(media)
        self.getThumbnails()
        self.finished.emit()

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
        
        self.player.set_media(self.medias[mediaNum])
        self.player.play()

    def playFirstUrl(self):

        self.choiceVideo(state,0)

    def endPlayer(self):
        self.checkState.start(self.player)
        