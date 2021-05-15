from pynput import keyboard

class KeyBoard:
    def __init__(self,player):

        self.getKeyboard =keyboard.Listener(on_press=self.on_press,on_release=self.on_release)
        self.player = player

    def on_press(self,key):

        self.controlVideoWithKeyBoard(key)

    def on_release(self,key):
        pass

    def controlVideoWithKeyBoard(self,key):
        
        if key == keyboard.Key.left :
            print(str(self.player.get_time()))
            self.player.set_time(self.player.get_time()-10000)
        elif key == keyboard.Key.right :
            self.player.set_time(self.player.get_time()+10000)
        elif key == keyboard.Key.space :
            self.player.pause()

    def getKeyBoard(self):
        self.getKeyboard.start()