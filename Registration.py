class Registration:
    def __init__(self,conn):
        self.conn = conn
        self.cur = self.conn.cursor()
        self.checkWantIdResult = 0

    def checkWantId(self,wantId) : #아이디 중복체크
        
        self.cur.execute("SELECT id FROM user WHERE id='"+ wantId +"';")
        self.wantIdData = self.cur.fetchall() 

        if len(self.wantIdData) == 0 :
            self.checkWantIdResult = False
        else : 
            self.checkWantIdResult = True

    def addUserInfo(self,wantId,wantPassword): #데이터베이스에 정보 추가 

        self.cur.execute("INSERT INTO user VALUES ('"+ wantId +"','"+ wantPassword +"');") #id 비번 추가 
        self.conn.commit()