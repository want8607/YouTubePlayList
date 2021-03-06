import sys
import urllib
from vlc import State
import gui
import sqlite3
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
from Login import Login
from Registration import Registration
from Playlist import Playlist
from PlayVideo import PlayVideo


class Main:

    def __init__(self):
        self.connectDatabase()
        self.loginPage()
        self.playlistPage()
        self.playlist = Playlist(self.conn)
        self.lastNum = 0

#데이터베이스 연결    

    def connectDatabase(self):

        self.conn = sqlite3.connect("week8.db")
        self.cur = self.conn.cursor()           
        
#초기페이지
    def loginPage(self):

        ui.stackedWidget.setCurrentIndex(0)
        ui.regist_exitButton.clicked.connect(lambda : self.registWindow(True))
        ui.registButton.clicked.connect(lambda: self.registWindow(False))
        ui.regist_registButton.clicked.connect(self.registrate)
        ui.logInButton.clicked.connect(self.loginProcess)

    def registWindow(self,a):

        ui.opacityWidget.setHidden(a)
        ui.registWidget.setHidden(a)

    def loginProcess(self):

        self.id = ui.log_idInput.text()
        password = ui.log_passInput.text()
        self.login = Login(self.conn)
        self.login.checkResult(self.id,password)

        if self.login.loginResult == 1:
            ui.stackedWidget.setCurrentIndex(1)
            self.showList()
        elif self.login.loginResult == 2 :
            self.login_alarm("아이디 혹은 비밀번호를 다시 입력해주세요")
    
    #아이디 알림
    def login_alarm(self,text):

        ui.log_alarm.setHidden(False)
        ui.log_okButton.clicked.connect(lambda : ui.log_alarm.setHidden(True))
        ui.log_text.setText(text)
#회원가입
        
    def registrate(self):

        regist_id = ui.regist_idInput.text()
        noBlank_id = "".join(regist_id.split())
        regist_pass = ui.regist_passInput.text()
        noBlank_pass = "".join(regist_pass.split())
        regist_pass2 = ui.regist_passInput2.text()

        registration = Registration(self.conn)
        registration.checkWantId(regist_id)

        if regist_id =='' or regist_pass =='':
            self.regist_alarm("아이디 비밀번호를 입력해주세요")
        elif regist_id != noBlank_id or regist_pass != noBlank_pass:
            self.regist_alarm("아이디 혹은 비밀번호에 공백이 포함되어있습니다.")
        else:
            if registration.checkWantIdResult == True:
                self.regist_alarm("아이디 중복체크를 다시 해주세요")

            elif registration.checkWantIdResult == False and regist_pass != regist_pass2:
                self.regist_alarm("비밀번호을 다시 확인 해주세요")

            elif registration.checkWantIdResult == False and regist_pass == regist_pass2:
                registration.addUserInfo(regist_id, regist_pass)
                self.registWindow(True)
                ui.regist_idInput.setText('')
                ui.regist_passInput.setText('')
                ui.regist_passInput2.setText('')
                self.login_alarm("회원가입 성공")

        
    #회원가입 알림창
    def regist_alarm(self,text):

        ui.regist_alarm.setHidden(False)
        ui.regist_text.setText(text)
        ui.regist_okButton.clicked.connect(lambda : ui.regist_alarm.setHidden(True))

#재생목록
    def playlistPage(self):

        ui.logoutButton.clicked.connect(self.logout)
        ui.addPlaylistButton.clicked.connect(lambda : self.addPlaylistWindow(False))
        ui.addListWidget_close.clicked.connect(lambda : self.addPlaylistWindow(True))
        ui.addListWidget_add.clicked.connect(self.addPlaylist)
        ui.addUrlWidget_close.clicked.connect(lambda: self.addUrlWindow(True))
        ui.goBackToPlaylistButton.clicked.connect(self.goBackToPlaylist)
        ui.addUrlWidget_add.clicked.connect(self.clickAddUrlButton)
        ui.addList_okButton.clicked.connect(lambda : ui.addList_alarm.setHidden(True))
        ui.delete_okButton.clicked.connect(lambda:self.deleteAdmit(self.playlistName))
        ui.delete_noButton.clicked.connect(self.cancelDelete)
        self.playVideo = PlayVideo(self.conn)
        self.playVideo.setDaemon(True)
        self.playVideo.goBackToPlaylist = True
        self.playVideo.start()
        self.playVideo.finished.connect(self.endLoading)
        self.playVideo.played.connect(self.playingChange)
        ui.minimizeButton.clicked.connect(self.clickMiniButton)
        ui.volumButton.clicked.connect(self.clickVolumButton)
        ui.maximizeButton.clicked.connect(self.clickMaxiButton)
        ui.nextButton.clicked.connect(self.clickNextButton)
        ui.lastButton.clicked.connect(self.clickLastButton)
        ui.pauseButton.clicked.connect(self.playVideo.pause)
        ui.playButton.clicked.connect(self.playVideo.play)
        ui.volumslider.valueChanged.connect(self.playVideo.changeVolum)
        #최소화창    
        ui.pauseButton2.clicked.connect(self.playVideo.pause)
        ui.playButton2.clicked.connect(self.playVideo.play)
        
        self.volumeClicked = False
    #로그아웃
    def logout(self):

        ui.log_passInput.setText('')
        ui.log_idInput.setText('')
        ui.stackedWidget.setCurrentIndex(0)
        
    #플레이리스트 생성
    def addPlaylistWindow(self,a):

        ui.opacityWidget2.setHidden(a)
        ui.addListWidget.setHidden(a)
        ui.addListWidget_name.setText('')

    def addPlaylist(self):
        
        wantPlaylistName = ui.addListWidget_name.text()
        if wantPlaylistName == '':
            self.playlist_alarm("이름을 입력하세요")
        else:
            self.playlist.addDataToDatabase(self.id, wantPlaylistName) 
            
            if self.playlist.checkResult == True:
                self.playlist_alarm("재생목록 생성 완료")
                self.showList()
                
            elif self.playlist.checkResult == False:
                self.playlist_alarm("이미 존재하는 이름입니다")
                
    #플레이리스트 알림창
    def playlist_alarm(self,text):

        ui.addList_alarm.setHidden(False)
        ui.addList_text.setText(text)
        
    
    #플레이리스트 LISTVIEW
    def showList(self):

        self.playlist.getPlaylist(self.id)
        model = QtGui.QStandardItemModel(ui.playlistView)
        ui.playlistView.setModel(model)
        self.produceButton()
        for j in range (0,len(self.playlist.playlists)) :
            item = QtGui.QStandardItem(self.playlist.playlists[j][0])
            item.setSizeHint(QtCore.QSize(740,80))        
            model.appendRow(item)
            ui.playlistView.setIndexWidget(item.index(),self.playlistWidget[j]) 
    
    #버튼 생성
    def produceButton(self):

        self.listButtons = []
        self.plusButtons = []
        self.trashButtons = []
        self.playlistWidget = []
        for i in range(0,len(self.playlist.playlists)):
            self.playlistWidget.append(QtWidgets.QWidget())
            self.listButtons.append(QtWidgets.QPushButton(self.playlistWidget[i]))
            self.listButtons[i].setText(self.playlist.playlists[i][0])
            self.listButtons[i].setCursor(ui.pointingHandCursor)
            self.listButtons[i].setStyleSheet(ui.listViewStlye)
            self.listButtons[i].setFocusPolicy(QtCore.Qt.NoFocus)
            self.listButtons[i].setGeometry(QtCore.QRect(0, 10, 571, 61))
            self.listButtons[i].clicked.connect(lambda state,x = i:self.clickListButton(state,x))
            self.plusButtons.append(QtWidgets.QPushButton(self.playlistWidget[i]))
            self.plusButtons[i].setIcon(QtGui.QIcon(ui.plusIcon))
            self.plusButtons[i].setCursor(ui.pointingHandCursor)
            self.plusButtons[i].setStyleSheet(ui.listViewStlye)
            self.plusButtons[i].setFocusPolicy(QtCore.Qt.NoFocus)
            self.plusButtons[i].setGeometry(QtCore.QRect(575, 10, 71, 61))
            self.plusButtons[i].clicked.connect(lambda state,x = i: self.clickPlusButton(state,x))
            self.trashButtons.append(QtWidgets.QPushButton(self.playlistWidget[i]))
            self.trashButtons[i].setIcon(QtGui.QIcon(ui.trashIcon))
            self.trashButtons[i].setIconSize(QtCore.QSize(60,60))
            self.trashButtons[i].setCursor(ui.pointingHandCursor)
            self.trashButtons[i].setStyleSheet(ui.listViewStlye)
            self.trashButtons[i].setFocusPolicy(QtCore.Qt.NoFocus)
            self.trashButtons[i].setGeometry(QtCore.QRect(650, 10, 71, 61))
            self.trashButtons[i].clicked.connect(lambda state,x = i: self.clickTrashButton(state,x))
            
    
    #영상 추가창
    def addUrlWindow(self,hidden):
        ui.opacityWidget2.setHidden(hidden)
        ui.addUrlWidget.setHidden(hidden)
        ui.addUrlWidget_name.setText('')

    def clickPlusButton(self,state,index1):
        self.addUrlWindow(False)
        self.playlistName = self.playlist.playlists[index1][0]
        

    def clickAddUrlButton(self):
        
        url = ui.addUrlWidget_name.text()
        if url == '':
            self.playlist_alarm("url을 입력하세요")
        else :
            self.playlist.addUrlToDatabase(self.id,self.playlistName,url)
            self.playlist_alarm("영상이 추가되었습니다")
            ui.addUrlWidget_name.setText('')
    
    #재생목록 삭제창
    def clickTrashButton(self,state,m):
        print(88)
        self.deleteWindow(False)
        self.playlistName = self.playlist.playlists[m][0]
        
        
    def deleteAdmit(self,playlistName):
        self.playlist.deletePlaylist(self.id,playlistName)
        self.showList()
        self.deleteWindow(True)

    def cancelDelete(self):
        self.deleteWindow(True)

    def deleteWindow(self,hidden):
        ui.opacityWidget2.setHidden(hidden)
        ui.deleteWidget.setHidden(hidden)
        
    #재생목록선택
    def clickListButton(self,state,index2):
        
        self.playlistName = self.playlist.playlists[index2][0]
        self.playVideo.getUrl(self.id,self.playlistName)

        if len(self.playVideo.urls) == 0:
            self.playlist_alarm("영상을 추가해 주세요")
        else:
            ui.loadingWidget.setHidden(False)
            self.playVideo.goBackToPlaylist = False
        
    def endLoading(self): 

        self.playVideo.player.set_hwnd(ui.videoWidget.winId())
        self.showThumbnail()
        ui.stackedWidget.setCurrentIndex(2)
        ui.loadingWidget.setHidden(True)
        
        
#동영상 재생 페이지 

    def showThumbnail(self):

        model = QtGui.QStandardItemModel(ui.thumbnailListView)
        ui.thumbnailListView.setModel(model)
        self.produceThumbnail()
        for n in range (0,len(self.playVideo.urls)) : 
            item2 = QtGui.QStandardItem(self.playVideo.urls[n][0])
            item2.setSizeHint(QtCore.QSize(232,141))        
            model.appendRow(item2)
            ui.thumbnailListView.setIndexWidget(item2.index(),self.thumbnailButtons[n]) 
    
    #뒤로가기
    def goBackToPlaylist(self):
        self.playVideo.goBackToPlaylist = True
        self.lastNum = 0
        ui.stackedWidget.setCurrentIndex(1)
        self.playVideo.initPlayer()        

    #버튼 생성
    def produceThumbnail(self):
        self.thumbnailButtons = []
        for m in range(0,len(self.playVideo.urls)):
            self.thumbnailButtons.append(QtWidgets.QPushButton(ui.thumbnailListView))
            url = self.playVideo.thumbnails[m]
            data = urllib.request.urlopen(url).read()
            image = QtGui.QImage()
            image.loadFromData(data)
            pixmap = QtGui.QPixmap(image.scaled(232,131))
            icon = QtGui.QIcon(pixmap)
            self.thumbnailButtons[m].setIcon(icon)
            self.thumbnailButtons[m].setCursor(ui.pointingHandCursor)
            if m == 0:
                self.thumbnailButtons[m].setStyleSheet(ui.thumbNailButtonStyle2)
            else:    
                self.thumbnailButtons[m].setStyleSheet(ui.thumbNailButtonStyle)
            self.thumbnailButtons[m].setFocusPolicy(QtCore.Qt.NoFocus)
            self.thumbnailButtons[m].setIconSize(QtCore.QSize(232,131))
            self.thumbnailButtons[m].clicked.connect(lambda state,x = m:self.playVideo.choiceVideo(state,x))
    
    def playingChange(self):
        self.clickThumbnailButton(self.playVideo.playingVideoNum)
        self.chageTitle()

    def clickThumbnailButton(self,x):
        self.thumbnailButtons[self.lastNum].setStyleSheet(ui.thumbNailButtonStyle)
        self.lastNum = x
        self.thumbnailButtons[x].setStyleSheet(ui.thumbNailButtonStyle2)

    #조작버튼
    
    def clickVolumButton(self):
        if self.volumeClicked == False:
            ui.volumslider.setHidden(False)
            self.volumeClicked = True
        elif self.volumeClicked == True:
            ui.volumslider.setHidden(True)
            self.volumeClicked = False

    #제목바꾸기
    def chageTitle(self):
        if len(self.playVideo.title) > 25:
            
            ui.videoTitle.setText(self.playVideo.title[:35]+"...")
            ui.videoTitle2.setText(self.playVideo.title[:25]+"...")
        else:
            ui.videoTitle.setText(self.playVideo.title)
            ui.videoTitle2.setText(self.playVideo.title)
    #최소화
    def clickMiniButton(self):
        ui.MainWindow.hide()
        ui.MainWindow2.show()

    #최대화
    def clickMaxiButton(self):
        ui.MainWindow2.hide()
        ui.MainWindow.show()

    #다음영상
    def clickNextButton(self):
        self.playVideo.clickNextButton()
    
    #이전영상
    def clickLastButton(self):
        self.playVideo.clickLastButton()

    #재생목록 삭제
    #비디오 삭제

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    ui = gui.Ui_MainWindow()

    ui.setupUi()
    
    main = Main()
    sys.exit(app.exec_())

    