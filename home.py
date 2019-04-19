import sys
from register import register_gui
from welcome import welcome_gui
from main import FaceRecognition

main = FaceRecognition()

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def home_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = HomePage (root)
    root.mainloop()

w = None
def create_HomePage(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = HomePage (w)
    return (w, top)

def destroy_HomePage():
    global w
    w.destroy()
    w = None

class HomePage:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("369x468+650+150")
        top.title("Face Recognition")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.136, rely=0.085, relheight=0.6, relwidth=0.762)

        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(width=281)

        self.Message1 = tk.Message(self.Canvas1)
        self.Message1.place(relx=0.178, rely=0.142, relheight=0.658
                , relwidth=0.648)
        self.Message1.configure(text='''A simple login system using face recognnition application in python''')
        self.Message1.configure(width=182)

        self.register = tk.Button(top)
        self.register.place(relx=0.136, rely=0.812, height=41, width=111)
        self.register.configure(text='''Register''')
        self.register.configure(width=111)

        self.login = tk.Button(top)
        self.login.place(relx=0.542, rely=0.812, height=41, width=111)
        self.login.configure(text='''Login''')
        self.login.configure(width=111)

        self.register.configure(command= self.registerHome)
        self.login.configure(command= self.loginHome)

    def registerHome(self):
        register_gui()
    
    def loginHome(self):
        main.trainFace()
        user = main.recognizeFace()
        welcome_gui(user)


if __name__ == '__main__':
    home_gui()





