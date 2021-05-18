from pynput import keyboard
from win32gui import GetWindowText, GetForegroundWindow

class KeyBoard:
    def __init__(self,player):

        self.getKeyboard =keyboard.Listener(on_press=self.on_press,on_release=self.on_release)
        self.player = player

    def on_press(self,key):
        current_window = GetWindowText(GetForegroundWindow())
        desired_window_name = "YouTubePlayer"
        if current_window == desired_window_name:
            self.controlVideoWithKeyBoard(key)

    def on_release(self,key):
        pass

    def controlVideoWithKeyBoard(self,key):
        
        if key == keyboard.Key.left :
            
            self.player.set_time(self.player.get_time()-10000)
        elif key == keyboard.Key.right :
            self.player.set_time(self.player.get_time()+10000)
        elif key == keyboard.Key.space :
            self.player.pause()

    def getKeyBoard(self):
        self.getKeyboard.start()
    
