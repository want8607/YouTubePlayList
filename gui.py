
from ctypes import alignment
from PyQt5 import QtCore, QtGui, QtWidgets
import urllib.request
# from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
# from PyQt5.QtMultimediaWidgets import QVideoWidget
class Ui_MainWindow(object):
    def __init__(self):
        QtGui.QFontDatabase.addApplicationFont("Nanumsquare_ac_TTF/Nanumsquare_acR.ttf")

        self.buttonStyle = "color: white;background-color: #D83030; font-size: 16pt; font-family: 나눔스퀘어_ac;"
        self.inputLineStyle = "color: black; background-color: white; font-size: 16pt; font-family: 나눔스퀘어_ac;"        
        self.pageBackgroundColor = "background-color: #404040;"
        self.alarmBackgroundColor = "background-color:black;"
        self.opcityBackgroundColor = "background-color: black;"
        self.noticeStyle = "color: white; font-size:16pt; font-family: 나눔스퀘어_ac;"
        self.pixmap = QtGui.QPixmap('picture/22.png')
        self.listViewStlye = "font-size:16pt; font-family: 나눔스퀘어_ac; background-color:white;"
        self.plusIcon = QtGui.QPixmap("picture/plus.png")
        self.loadingGif = QtGui.QMovie("picture/loading.gif")
        
    def setupUi(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setFixedSize(1600,900)
        self.MainWindow.setStyleSheet(self.pageBackgroundColor)

        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1600, 900))
        self.stackedWidget.setObjectName("stackedWidget")
    
    #로그인 페이지

        self.loginPage = QtWidgets.QWidget()
        self.loginPage.setObjectName("loginPage")

        self.log_logo = QtWidgets.QLabel(self.loginPage)
        self.log_logo.setGeometry(QtCore.QRect(300,150,1000,251))
        self.log_logo.setPixmap(self.pixmap.scaled(self.log_logo.size()))
        
        self.log_idInput = QtWidgets.QLineEdit(self.loginPage)
        self.log_idInput.setGeometry(QtCore.QRect(650, 580, 300, 50))
        self.log_idInput.setObjectName("log_idInput")
        self.log_idInput.setStyleSheet(self.inputLineStyle)
        self.log_idInput.setPlaceholderText("ID")
        self.log_idInput.setAlignment(QtCore.Qt.AlignCenter)

        self.log_passInput = QtWidgets.QLineEdit(self.loginPage)
        self.log_passInput.setGeometry(QtCore.QRect(650, 640, 300, 50))
        self.log_passInput.setObjectName("log_passInput")
        self.log_passInput.setStyleSheet(self.inputLineStyle)
        self.log_passInput.setPlaceholderText("PASSWORD")
        self.log_passInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.log_passInput.setAlignment(QtCore.Qt.AlignCenter)

        self.logInButton = QtWidgets.QPushButton(self.loginPage)
        self.logInButton.setGeometry(QtCore.QRect(650, 730, 300, 51))
        self.logInButton.setText("로그인")
        self.logInButton.setObjectName("logInButton")
        self.logInButton.setStyleSheet(self.buttonStyle)
        
        self.registButton = QtWidgets.QPushButton(self.loginPage)
        self.registButton.setGeometry(QtCore.QRect(650, 790, 300, 51))
        self.registButton.setText("회원가입")
        self.registButton.setObjectName("registButton")
        self.registButton.setStyleSheet(self.buttonStyle)
        #알림창
        self.log_alarm = QtWidgets.QWidget(self.loginPage)
        self.log_alarm.setGeometry(QtCore.QRect(450,280,700,270))
        self.log_alarm.setStyleSheet(self.alarmBackgroundColor)
        self.log_alarm.setHidden(True)

        self.log_okButton = QtWidgets.QPushButton(self.log_alarm)
        self.log_okButton.setGeometry(QtCore.QRect(290,210,121,40))
        self.log_okButton.setStyleSheet(self.buttonStyle)
        self.log_okButton.setText("확인")

        self.log_text = QtWidgets.QLabel(self.log_alarm)
        self.log_text.setGeometry(QtCore.QRect(50,70,601,61))
        self.log_text.setStyleSheet(self.noticeStyle)
        self.log_text.setAlignment(QtCore.Qt.AlignCenter)
        #회원가입 창
        self.opacityEffect = QtWidgets.QGraphicsOpacityEffect()
        self.opacityEffect.setOpacity(0.6)

        self.opacityWidget = QtWidgets.QWidget(self.loginPage)
        self.opacityWidget.setStyleSheet(self.opcityBackgroundColor)
        self.opacityWidget.setGeometry(QtCore.QRect(0,0,1600,900))
        self.opacityWidget.setGraphicsEffect(self.opacityEffect)
        self.opacityWidget.setHidden(True)

        self.registWidget = QtWidgets.QWidget(self.loginPage)
        self.registWidget.setGeometry(QtCore.QRect(350,200,900,500))
        self.registWidget.setStyleSheet(self.pageBackgroundColor)
        self.registWidget.setHidden(True)

        self.regist_idInput = QtWidgets.QLineEdit(self.registWidget)
        self.regist_idInput.setGeometry(QtCore.QRect(300, 120, 300, 50))
        self.regist_idInput.setObjectName("regist_idInput")
        self.regist_idInput.setStyleSheet(self.inputLineStyle)
        self.regist_idInput.setPlaceholderText("원하는 아이디 입력")
        self.regist_idInput.setAlignment(QtCore.Qt.AlignCenter) 

        self.regist_passInput = QtWidgets.QLineEdit(self.registWidget)
        self.regist_passInput.setGeometry(QtCore.QRect(300, 190, 300, 50))
        self.regist_passInput.setObjectName("regist_passInput")
        self.regist_passInput.setStyleSheet(self.inputLineStyle)
        self.regist_passInput.setPlaceholderText("비밀번호 입력")
        self.regist_passInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.regist_passInput.setAlignment(QtCore.Qt.AlignCenter)

        self.regist_passInput2 = QtWidgets.QLineEdit(self.registWidget)
        self.regist_passInput2.setGeometry(QtCore.QRect(300, 260, 300, 50))
        self.regist_passInput2.setObjectName("regist_passInput2")
        self.regist_passInput2.setStyleSheet(self.inputLineStyle)
        self.regist_passInput2.setPlaceholderText("비밀번호 확인")
        self.regist_passInput2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.regist_passInput2.setAlignment(QtCore.Qt.AlignCenter)

        self.regist_registButton = QtWidgets.QPushButton(self.registWidget)
        self.regist_registButton.setGeometry(QtCore.QRect(370,390,150,50))
        self.regist_registButton.setStyleSheet(self.buttonStyle)
        self.regist_registButton.setText("회원가입")

        self.regist_exitButton = QtWidgets.QPushButton(self.registWidget)
        self.regist_exitButton.setGeometry(QtCore.QRect(809,10,81,50))
        self.regist_exitButton.setStyleSheet(self.buttonStyle)
        self.regist_exitButton.setText("닫기")

        #알림창
        self.regist_alarm = QtWidgets.QWidget(self.registWidget)
        self.regist_alarm.setGeometry(QtCore.QRect(119,90,701,270))
        self.regist_alarm.setStyleSheet(self.alarmBackgroundColor)
        self.regist_alarm.setHidden(True)
        
        self.regist_okButton = QtWidgets.QPushButton(self.regist_alarm)
        self.regist_okButton.setGeometry(QtCore.QRect(290,200,121,40))
        self.regist_okButton.setStyleSheet(self.buttonStyle)
        self.regist_okButton.setText("확인")

        self.regist_text = QtWidgets.QLabel(self.regist_alarm)
        self.regist_text.setGeometry(QtCore.QRect(50,70,601,61))
        self.regist_text.setStyleSheet(self.noticeStyle)
        self.regist_text.setAlignment(QtCore.Qt.AlignCenter)
        self.stackedWidget.addWidget(self.loginPage)

    #플레이리스트 페이지
        self.playlistPage = QtWidgets.QWidget()
        self.playlistPage.setObjectName("playlistPage")
        self.stackedWidget.addWidget(self.playlistPage)

        self.addPlaylistButton = QtWidgets.QPushButton(self.playlistPage)
        self.addPlaylistButton.setGeometry(QtCore.QRect(680,760,240,40))
        self.addPlaylistButton.setStyleSheet(self.buttonStyle)
        self.addPlaylistButton.setText("재생목록 추가")

        self.logoutButton = QtWidgets.QPushButton(self.playlistPage)
        self.logoutButton.setGeometry(QtCore.QRect(1430,30,120,40))
        self.logoutButton.setStyleSheet(self.buttonStyle)
        self.logoutButton.setText("로그아웃")

        self.playlistLogo = QtWidgets.QLabel(self.playlistPage)
        self.playlistLogo.setGeometry(QtCore.QRect(45,21,301,101))
        self.playlistLogo.setPixmap(self.pixmap.scaled(self.playlistLogo.size()))

        self.playlistView = QtWidgets.QListView(self.playlistPage)
        self.playlistView.setGeometry(QtCore.QRect(435,150,730,561))
        self.playlistView.setStyleSheet(self.pageBackgroundColor+"border:#404040")
        # self.playlistView.setSpacing(6)

        #재생목록 추가창
        self.opacityEffect2 = QtWidgets.QGraphicsOpacityEffect()
        self.opacityEffect2.setOpacity(0.6)
        self.opacityWidget2 = QtWidgets.QWidget(self.playlistPage)
        self.opacityWidget2.setStyleSheet(self.opcityBackgroundColor)
        self.opacityWidget2.setGeometry(QtCore.QRect(0,0,1600,900))
        self.opacityWidget2.setGraphicsEffect(self.opacityEffect2)
        self.opacityWidget2.setHidden(True)

        self.addListWidget = QtWidgets.QWidget(self.playlistPage)
        self.addListWidget.setStyleSheet(self.pageBackgroundColor)
        self.addListWidget.setGeometry(QtCore.QRect(410,320,781,191))
        self.addListWidget.setHidden(True)

        self.addListWidget_name = QtWidgets.QLineEdit(self.addListWidget)
        self.addListWidget_name.setGeometry(QtCore.QRect(80,80,451,41))
        self.addListWidget_name.setStyleSheet(self.inputLineStyle)
        self.addListWidget_name.setPlaceholderText("원하는 이름을 입력하세요")
        self.addListWidget_name.setAlignment(QtCore.Qt.AlignCenter)

        self.addListWidget_close = QtWidgets.QPushButton(self.addListWidget)
        self.addListWidget_close.setGeometry(QtCore.QRect(684,10,91,31))
        self.addListWidget_close.setStyleSheet(self.buttonStyle)
        self.addListWidget_close.setText("닫기")

        self.addListWidget_add = QtWidgets.QPushButton(self.addListWidget)
        self.addListWidget_add.setGeometry(QtCore.QRect(590,80,171,41))
        self.addListWidget_add.setStyleSheet(self.buttonStyle)
        self.addListWidget_add.setText("재생목록 생성")

        #URL 추가창
        self.addUrlWidget = QtWidgets.QWidget(self.playlistPage)
        self.addUrlWidget.setStyleSheet(self.pageBackgroundColor)
        self.addUrlWidget.setGeometry(QtCore.QRect(410,320,781,191))
        self.addUrlWidget.setHidden(True)

        self.addUrlWidget_name = QtWidgets.QLineEdit(self.addUrlWidget)
        self.addUrlWidget_name.setGeometry(QtCore.QRect(80,80,451,41))
        self.addUrlWidget_name.setStyleSheet(self.inputLineStyle)
        self.addUrlWidget_name.setPlaceholderText("영상의 URL을 입력하세요")
        self.addUrlWidget_name.setAlignment(QtCore.Qt.AlignCenter)

        self.addUrlWidget_close = QtWidgets.QPushButton(self.addUrlWidget)
        self.addUrlWidget_close.setGeometry(QtCore.QRect(684,10,91,31))
        self.addUrlWidget_close.setStyleSheet(self.buttonStyle)
        self.addUrlWidget_close.setText("닫기")

        self.addUrlWidget_add = QtWidgets.QPushButton(self.addUrlWidget)
        self.addUrlWidget_add.setGeometry(QtCore.QRect(590,80,171,41))
        self.addUrlWidget_add.setStyleSheet(self.buttonStyle)
        self.addUrlWidget_add.setText("영상추가")

        #알림창
        self.addList_alarm = QtWidgets.QWidget(self.playlistPage)
        self.addList_alarm.setGeometry(QtCore.QRect(450,290,701,270))
        self.addList_alarm.setStyleSheet(self.alarmBackgroundColor)
        self.addList_alarm.setHidden(True)
        
        self.addList_okButton = QtWidgets.QPushButton(self.addList_alarm)
        self.addList_okButton.setGeometry(QtCore.QRect(290,200,121,40))
        self.addList_okButton.setStyleSheet(self.buttonStyle)
        self.addList_okButton.setText("확인")

        self.addList_text = QtWidgets.QLabel(self.addList_alarm)
        self.addList_text.setGeometry(QtCore.QRect(50,70,601,61))
        self.addList_text.setStyleSheet(self.noticeStyle)
        self.addList_text.setAlignment(QtCore.Qt.AlignCenter)

    #재생 페이지    
        self.playPage = QtWidgets.QWidget()
        self.playPage.setObjectName("playPage")

        self.videoWidget = QtWidgets.QWidget(self.playPage)
        self.videoWidget.setGeometry(QtCore.QRect(20,30,1280,720))


        self.thumbnailListView = QtWidgets.QListView(self.playPage)
        self.thumbnailListView.setGeometry(QtCore.QRect(1325,100,271,771))
        self.thumbnailListView.setStyleSheet(self.pageBackgroundColor+"border:#404040")

        


        self.stackedWidget.addWidget(self.playPage)
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
        
        self.MainWindow.show()

    #로딩 창
        self.opacityEffect3 = QtWidgets.QGraphicsOpacityEffect()
        self.opacityEffect3.setOpacity(0.6)
        self.loadingWidget = QtWidgets.QLabel(self.playlistPage)
        self.loadingWidget.setAlignment(QtCore.Qt.AlignCenter)
        self.loadingWidget.setGeometry(QtCore.QRect(0,0,1600,900))
        self.loadingWidget.setGraphicsEffect(self.opacityEffect3)
        self.loadingWidget.setHidden(True)
        self.loadingWidget.setMovie(self.loadingGif)
        self.loadingGif.start()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))




