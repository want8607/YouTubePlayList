class Playlist:
    def __init__(self,conn):
        self.conn = conn
        self.cur = self.conn.cursor()
        self.checkResult = False
        self.playlists = None

    def addDataToDatabase(self,id,playlist):

        self.cur.execute("SELECT playlistName FROM playlist WHERE id ='"+id+"' AND playlistName ='"+playlist+"';")
        self.overlapCheck = self.cur.fetchall()

        if len(self.overlapCheck) == 0: 
            self.cur.execute("INSERT INTO playlist VALUES('"+id+"','"+playlist+"');")
            self.conn.commit()
            self.checkResult = True
        else :
            self.checkResult = False
    
    def getPlaylist(self,id):

        self.cur.execute("SELECT playlistName FROM playlist WHERE id ='"+ id +"';")
        self.playlists = self.cur.fetchall()

    def addUrlToDatabase(self,id,playlistName,url):

        self.cur.execute("INSERT INTO video VALUES('"+id+"','"+playlistName+"','"+url+"');")
        self.conn.commit()

    def deletePlaylist(self,id,playlistName):
        self.cur.execute("DELETE FROM playlist WHERE id ='"+id+"' AND playlistName ='"+playlistName+"';")
        self.conn.commit()

        