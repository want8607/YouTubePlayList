class Login:

    def __init__(self,conn):

        self.loginResult = 0
        self.conn = conn
        self.cur = self.conn.cursor()
        self.id = 0
        self.password = 0
        
    def checkResult(self,id,password):
            
            self.cur.execute("SELECT id,password FROM user WHERE id ='"+id+"';")
            self.userdata = self.cur.fetchall()
            if len(self.userdata) == 1:
                if self.userdata[0][1] == password :
                    print("로그인 성공")
                    self.id = id
                    self.password = password
                    self.loginResult = 1

                else :
                    self.loginResult = 2
                    
            else: 
                self.loginResult = 2