
from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSignal
import pafy
import vlc
import threading
class PlayVideo(threading.Thread,QtCore.QObject):
    finished = QtCore.pyqtSignal()
    def __init__(self,conn):
        QtCore.QObject.__init__(self)
        threading.Thread.__init__(self)
        self.conn = conn
        self.cur = self.conn.cursor()
        self.url = None
        self.player = None
        self.urls = []
        self.thumbnails = []

    def run(self):

        video = pafy.new(self.url)
        best = video.streams[0]
        
        playurl = best.url
        instance = vlc.Instance()
        self.player = instance.media_player_new()
        Media = instance.media_new(playurl)
        self.player.set_media(Media)
        self.getThumbnails()
        self.finished.emit()

    def getUrl(self,id,playlistName):
        self.cur.execute("SELECT url FROM video WHERE id='"+id+"' AND playlistName='"+playlistName+"';")
        urls = self.cur.fetchall()
        for d in range (0,len(urls)):
            self.urls.append(urls[d][0])
        self.url=urls[0][0]

    def getThumbnails(self):
        
        for url in self.urls :
            thumbnail = pafy.new(url)
            value = thumbnail.getbestthumb()
            self.thumbnails.append(str(value))

    def changeVolum(self,value):
        self.player.audio_set_volume(value)