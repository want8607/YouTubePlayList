import os
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def __init__(self):
        QtGui.QFontDatabase.addApplicationFont("Nanumsquare_ac_TTF/Nanumsquare_acR.ttf")

        self.buttonStyle = "color: white;background-color: #D83030; font-size: 16pt; font-family: 나눔스퀘어_ac;"
        self.controlButtonStyle = "QPushButton{border : 0px;} QPushButton::pressed{background-color : black;} QPushButton::hover{border : 2px solid black}"
        self.thumbNailButtonStyle = "QPushButton{border : 0px;} QPushButton::pressed{background-color : black;} QPushButton::hover{border : 2px solid #D83030}"
        self.thumbNailButtonStyle2 = "background-color: #D83030;"
        self.inputLineStyle = "color: black; background-color: white; font-size: 16pt; font-family: 나눔스퀘어_ac;"        
        self.pageBackgroundColor = "background-color: #404040;"
        self.alarmBackgroundColor = "background-color:black;"
        self.opcityBackgroundColor = "background-color: black;"
        self.noticeStyle = "color: white; font-size:16pt; font-family: 나눔스퀘어_ac;"
        self.pixmap = QtGui.QPixmap('picture/22.png')
        self.listViewStlye = "QPushButton{font-size:16pt; font-family: 나눔스퀘어_ac; background-color:white;} QPushButton::hover{font-size:16pt; font-family: 나눔스퀘어_ac; background-color:white; border : 2px solid #D83030}"
        self.plusIcon = QtGui.QPixmap("picture/plus.png")
        self.trashIcon = QtGui.QPixmap("picture/trash.png")
        self.loadingGif = QtGui.QMovie("picture/loading.gif")
        self.playButtonIcon = QtGui.QPixmap("picture/재생.png")
        self.pauseButtonIcon = QtGui.QPixmap("picture/정지.png")
        self.volumButtonIcon = QtGui.QPixmap("picture/음량.png")
        self.nextButtonIcon = QtGui.QPixmap("picture/다음.png")
        self.lastButtonIcon = QtGui.QPixmap("picture/이전.png")
        self.minimizeButtonIcon = QtGui.QPixmap("picture/축소.png")
        self.maximizeButtonIcon = QtGui.QPixmap("picture/확대.png")
        self.windowIcon = QtGui.QIcon("picture/windowIcon.png")
        self.title = "YouTubePlayer"
        self.pointingHandCursor = QtGui.QCursor(QtCore.Qt.PointingHandCursor)

    def setupUi(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setWindowTitle(self.title)
        self.MainWindow.setWindowIcon(self.windowIcon)
        self.MainWindow.setFixedSize(1600,900)
        self.MainWindow.setStyleSheet(self.pageBackgroundColor)

        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setFocusPolicy(QtCore.Qt.NoFocus)
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
        self.logInButton.setCursor(self.pointingHandCursor)
        self.logInButton.setText("로그인")
        self.logInButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.logInButton.setObjectName("logInButton")
        self.logInButton.setStyleSheet(self.buttonStyle)
        self.registButton = QtWidgets.QPushButton(self.loginPage)
        self.registButton.setGeometry(QtCore.QRect(650, 790, 300, 51))
        self.registButton.setCursor(self.pointingHandCursor)
        self.registButton.setText("회원가입")
        self.registButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.registButton.setObjectName("registButton")
        self.registButton.setStyleSheet(self.buttonStyle)
        #알림창
        self.log_alarm = QtWidgets.QWidget(self.loginPage)
        self.log_alarm.setGeometry(QtCore.QRect(450,280,700,270))
        self.log_alarm.setStyleSheet(self.alarmBackgroundColor)
        self.log_alarm.setHidden(True)

        self.log_okButton = QtWidgets.QPushButton(self.log_alarm)
        self.log_okButton.setCursor(self.pointingHandCursor)
        self.log_okButton.setGeometry(QtCore.QRect(290,210,121,40))
        self.log_okButton.setFocusPolicy(QtCore.Qt.NoFocus)
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
        self.regist_registButton.setCursor(self.pointingHandCursor)
        self.regist_registButton.setGeometry(QtCore.QRect(370,390,150,50))
        self.regist_registButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.regist_registButton.setStyleSheet(self.buttonStyle)
        self.regist_registButton.setText("회원가입")

        self.regist_exitButton = QtWidgets.QPushButton(self.registWidget)
        self.regist_exitButton.setCursor(self.pointingHandCursor)
        self.regist_exitButton.setGeometry(QtCore.QRect(809,10,81,50))
        self.regist_exitButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.regist_exitButton.setStyleSheet(self.buttonStyle)
        self.regist_exitButton.setText("닫기")

        #알림창
        self.regist_alarm = QtWidgets.QWidget(self.registWidget)
        self.regist_alarm.setGeometry(QtCore.QRect(119,90,701,270))
        self.regist_alarm.setStyleSheet(self.alarmBackgroundColor)
        self.regist_alarm.setHidden(True)
        
        self.regist_okButton = QtWidgets.QPushButton(self.regist_alarm)
        self.regist_okButton.setCursor(self.pointingHandCursor)
        self.regist_okButton.setGeometry(QtCore.QRect(290,200,121,40))
        self.regist_okButton.setFocusPolicy(QtCore.Qt.NoFocus)
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
        self.addPlaylistButton.setCursor(self.pointingHandCursor)
        self.addPlaylistButton.setGeometry(QtCore.QRect(680,760,240,40))
        self.addPlaylistButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.addPlaylistButton.setStyleSheet(self.buttonStyle)
        self.addPlaylistButton.setText("재생목록 추가")

        self.logoutButton = QtWidgets.QPushButton(self.playlistPage)
        self.logoutButton.setCursor(self.pointingHandCursor)
        self.logoutButton.setGeometry(QtCore.QRect(1430,30,120,40))
        self.logoutButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.logoutButton.setStyleSheet(self.buttonStyle)
        self.logoutButton.setText("로그아웃")

        self.playlistLogo = QtWidgets.QLabel(self.playlistPage)
        self.playlistLogo.setGeometry(QtCore.QRect(45,21,301,101))
        self.playlistLogo.setPixmap(self.pixmap.scaled(self.playlistLogo.size()))

        self.playlistView = QtWidgets.QListView(self.playlistPage)
        self.playlistView.setGeometry(QtCore.QRect(435,180,801,561))
        self.playlistView.setStyleSheet(self.pageBackgroundColor+"border:#404040")
        

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
        self.addListWidget_close.setCursor(self.pointingHandCursor)
        self.addListWidget_close.setGeometry(QtCore.QRect(684,10,91,31))
        self.addListWidget_close.setStyleSheet(self.buttonStyle)
        self.addListWidget_close.setText("닫기")

        self.addListWidget_add = QtWidgets.QPushButton(self.addListWidget)
        self.addListWidget_add.setCursor(self.pointingHandCursor)
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
        self.addUrlWidget_close.setCursor(self.pointingHandCursor)
        self.addUrlWidget_close.setGeometry(QtCore.QRect(684,10,91,31))
        self.addUrlWidget_close.setStyleSheet(self.buttonStyle)
        self.addUrlWidget_close.setFocusPolicy(QtCore.Qt.NoFocus)
        self.addUrlWidget_close.setText("닫기")

        self.addUrlWidget_add = QtWidgets.QPushButton(self.addUrlWidget)
        self.addUrlWidget_add.setCursor(self.pointingHandCursor)
        self.addUrlWidget_add.setGeometry(QtCore.QRect(590,80,171,41))
        self.addUrlWidget_add.setStyleSheet(self.buttonStyle)
        self.addUrlWidget_add.setFocusPolicy(QtCore.Qt.NoFocus)
        self.addUrlWidget_add.setText("영상추가")

        # 삭제 알림창
        self.deleteWidget = QtWidgets.QWidget(self.playlistPage)
        self.deleteWidget.setGeometry(QtCore.QRect(450,290,701,270))
        self.deleteWidget.setStyleSheet(self.alarmBackgroundColor)
        self.deleteWidget.setHidden(True)
        
        self.delete_okButton = QtWidgets.QPushButton(self.deleteWidget)
        self.delete_okButton.setCursor(self.pointingHandCursor)
        self.delete_okButton.setGeometry(QtCore.QRect(200,200,121,40))
        self.delete_okButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.delete_okButton.setStyleSheet(self.buttonStyle)
        self.delete_okButton.setText("삭제")

        self.delete_noButton = QtWidgets.QPushButton(self.deleteWidget)
        self.delete_noButton.setCursor(self.pointingHandCursor)
        self.delete_noButton.setGeometry(QtCore.QRect(370,200,121,40))
        self.delete_noButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.delete_noButton.setStyleSheet(self.buttonStyle)
        self.delete_noButton.setText("취소")

        self.delete_text = QtWidgets.QLabel(self.deleteWidget)
        self.delete_text.setGeometry(QtCore.QRect(140,20,421,61))
        self.delete_text.setText("삭제 하시겠습니까?")
        self.delete_text.setStyleSheet(self.noticeStyle)
        self.delete_text.setAlignment(QtCore.Qt.AlignCenter)
        #알림창
        self.addList_alarm = QtWidgets.QWidget(self.playlistPage)
        self.addList_alarm.setGeometry(QtCore.QRect(450,290,701,270))
        self.addList_alarm.setStyleSheet(self.alarmBackgroundColor)
        self.addList_alarm.setHidden(True)
        
        self.addList_okButton = QtWidgets.QPushButton(self.addList_alarm)
        self.addList_okButton.setCursor(self.pointingHandCursor)
        self.addList_okButton.setGeometry(QtCore.QRect(290,200,121,40))
        self.addList_okButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.addList_okButton.setStyleSheet(self.buttonStyle)
        self.addList_okButton.setText("확인")

        self.addList_text = QtWidgets.QLabel(self.addList_alarm)
        self.addList_text.setGeometry(QtCore.QRect(50,70,601,61))
        self.addList_text.setStyleSheet(self.noticeStyle)
        self.addList_text.setAlignment(QtCore.Qt.AlignCenter)
       
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

    #재생 페이지    
        self.playPage = QtWidgets.QWidget()
        self.playPage.setObjectName("playPage")

        self.videoWidget = QtWidgets.QWidget(self.playPage)
        self.videoWidget.setGeometry(QtCore.QRect(20,30,1280,720))

        self.thumbnailListView = QtWidgets.QListView(self.playPage)
        self.thumbnailListView.setGeometry(QtCore.QRect(1325,100,271,771))
        self.thumbnailListView.setStyleSheet(self.pageBackgroundColor+"border:#404040")

        self.videoTitle = QtWidgets.QLabel(self.playPage)
        self.videoTitle.setGeometry(QtCore.QRect(30,790,621,71))
        self.videoTitle.setFocusPolicy(QtCore.Qt.NoFocus)
        self.videoTitle.setStyleSheet(self.inputLineStyle)

        #영상 control
        self.playButton = QtWidgets.QPushButton(self.playPage)
        self.playButton.setStyleSheet(self.controlButtonStyle)
        self.playButton.setCursor(self.pointingHandCursor)
        self.playButton.setGeometry(QtCore.QRect(690,790,71,71))
        self.playButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.playButton.setIcon(QtGui.QIcon(self.playButtonIcon))
        self.playButton.setIconSize(QtCore.QSize(120,120))

        self.pauseButton = QtWidgets.QPushButton(self.playPage)
        self.pauseButton.setStyleSheet(self.controlButtonStyle)
        self.pauseButton.setCursor(self.pointingHandCursor)
        self.pauseButton.setGeometry(QtCore.QRect(770,790,71,71))
        self.pauseButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pauseButton.setIcon(QtGui.QIcon(self.pauseButtonIcon))
        self.pauseButton.setIconSize(QtCore.QSize(120,120))

        self.volumButton = QtWidgets.QPushButton(self.playPage)
        self.volumButton.setStyleSheet(self.controlButtonStyle)
        self.volumButton.setCursor(self.pointingHandCursor)
        self.volumButton.setGeometry(QtCore.QRect(1150,790,71,71))
        self.volumButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.volumButton.setIcon(QtGui.QIcon(self.volumButtonIcon))
        self.volumButton.setIconSize(QtCore.QSize(120,120))

        self.volumslider = QtWidgets.QSlider(self.playPage)
        self.volumButton.setCursor(self.pointingHandCursor)
        self.volumslider.setGeometry(QtCore.QRect(1170,620,31,160))
        self.volumslider.setRange(0,100)
        self.volumslider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.volumslider.setHidden(True)
        self.volumslider.setSliderPosition(100)

        self.minimizeButton = QtWidgets.QPushButton(self.playPage)
        self.minimizeButton.setStyleSheet(self.controlButtonStyle)
        self.minimizeButton.setCursor(self.pointingHandCursor)
        self.minimizeButton.setGeometry(QtCore.QRect(1240,790,71,71))
        self.minimizeButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.minimizeButton.setIcon(QtGui.QIcon(self.minimizeButtonIcon))
        self.minimizeButton.setIconSize(QtCore.QSize(120,120))

        self.goBackToPlaylistButton = QtWidgets.QPushButton(self.playPage)
        self.goBackToPlaylistButton.setCursor(self.pointingHandCursor)
        self.goBackToPlaylistButton.setGeometry(QtCore.QRect(1442,20,131,41))
        self.goBackToPlaylistButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.goBackToPlaylistButton.setStyleSheet(self.buttonStyle)
        self.goBackToPlaylistButton.setText("뒤로가기")

        self.stackedWidget.addWidget(self.playPage)
        self.MainWindow.setCentralWidget(self.centralwidget)

        #최소화화면
        self.MainWindow2 = QtWidgets.QMainWindow()
        self.MainWindow2.setWindowIcon(self.windowIcon)
        self.MainWindow2.setFixedSize(821,121)
        self.MainWindow2.setWindowTitle(self.title)
        self.MainWindow2.setStyleSheet(self.pageBackgroundColor)
        self.MainWindow2.hide()
        self.centralwidget2 = QtWidgets.QWidget(self.MainWindow2)
        self.centralwidget2.setGeometry(QtCore.QRect(0,0,821,121))
        
        self.videoTitle2 = QtWidgets.QLabel(self.centralwidget2)
        self.videoTitle2.setGeometry(QtCore.QRect(10,34,381,51))
        self.videoTitle2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.videoTitle2.setStyleSheet(self.inputLineStyle)
    
        self.playButton2 = QtWidgets.QPushButton(self.centralwidget2)
        self.playButton2.setStyleSheet(self.controlButtonStyle)
        self.playButton2.setCursor(self.pointingHandCursor)
        self.playButton2.setGeometry(QtCore.QRect(500,30,60,60))
        self.playButton2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.playButton2.setIcon(QtGui.QIcon(self.playButtonIcon))
        self.playButton2.setIconSize(QtCore.QSize(120,120))

        self.pauseButton2 = QtWidgets.QPushButton(self.centralwidget2)
        self.pauseButton2.setStyleSheet(self.controlButtonStyle)
        self.pauseButton2.setCursor(self.pointingHandCursor)
        self.pauseButton2.setGeometry(QtCore.QRect(580,30,60,60))
        self.pauseButton2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pauseButton2.setIcon(QtGui.QIcon(self.pauseButtonIcon))
        self.pauseButton2.setIconSize(QtCore.QSize(100,100))

        self.lastButton = QtWidgets.QPushButton(self.centralwidget2)
        self.lastButton.setStyleSheet(self.controlButtonStyle)
        self.lastButton.setCursor(self.pointingHandCursor)
        self.lastButton.setGeometry(QtCore.QRect(420,30,60,60))
        self.lastButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lastButton.setIcon(QtGui.QIcon(self.lastButtonIcon))
        self.lastButton.setIconSize(QtCore.QSize(100,100))

        self.nextButton = QtWidgets.QPushButton(self.centralwidget2)
        self.nextButton.setStyleSheet(self.controlButtonStyle)
        self.nextButton.setCursor(self.pointingHandCursor)
        self.nextButton.setGeometry(QtCore.QRect(660,30,60,60))
        self.nextButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.nextButton.setIcon(QtGui.QIcon(self.nextButtonIcon))
        self.nextButton.setIconSize(QtCore.QSize(100,100))

        self.maximizeButton = QtWidgets.QPushButton(self.centralwidget2)
        self.maximizeButton.setStyleSheet(self.controlButtonStyle)
        self.maximizeButton.setCursor(self.pointingHandCursor)
        self.maximizeButton.setGeometry(QtCore.QRect(740,30,60,60))
        self.maximizeButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.maximizeButton.setIcon(QtGui.QIcon(self.maximizeButtonIcon))
        self.maximizeButton.setIconSize(QtCore.QSize(100,100))

        self.MainWindow.show()



