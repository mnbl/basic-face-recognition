import sys
from main import FaceRecognition

faceRecognise = FaceRecognition()

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

def register_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = RegisterPage (root)
    root.mainloop()

w = None
def create_RegisterPage(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = RegisterPage (w)
    return (w, top)

def destroy_RegisterPage():
    global w
    w.destroy()
    w = None

class RegisterPage:
    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("430x465+638+215")
        top.title("Register")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.07, rely=0.086, relheight=0.69, relwidth=0.84)
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(width=361)

        self.id = tk.Label(self.Canvas1)
        self.id.place(relx=0.028, rely=0.249, height=31, width=108)
        self.id.configure(text='''ID''')
        self.id.configure(width=108)

        self.name = tk.Label(self.Canvas1)
        self.name.place(relx=0.028, rely=0.436, height=31, width=108)
        self.name.configure(activebackground="#f9f9f9")
        self.name.configure(text='''Name''')

        self.Entry1 = tk.Entry(self.Canvas1)
        self.Entry1.place(relx=0.499, rely=0.249,height=23, relwidth=0.46)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")

        self.Entry2 = tk.Entry(self.Canvas1)
        self.Entry2.place(relx=0.499, rely=0.436,height=23, relwidth=0.46)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")

        self.faceRegister = tk.Button(self.Canvas1)
        self.faceRegister.place(relx=0.277, rely=0.685, height=31, width=131)
        self.faceRegister.configure(text='''Register A Face''')
        self.faceRegister.configure(command= self.reconiseFace)
        self.faceRegister.configure(width=131)

        self.Message1 = tk.Message(self.Canvas1)
        self.Message1.place(relx=0.139, rely=0.093, relheight=0.078
                , relwidth=0.698)
        self.Message1.configure(text='''Create An Account''')
        self.Message1.configure(width=252)

        self.exit = tk.Button(top)
        self.exit.place(relx=0.4, rely=0.817, height=31, width=101)
        self.exit.configure(command= self.exitwindow)
        self.exit.configure(text='''Exit''')
        self.exit.configure(width=101)

    def exitwindow(self):
        sys.exit()

    def reconiseFace(self):
        entry1 = self.Entry1.get()
        entry2 = self.Entry2.get()

        FaceRecognition.faceDetect(entry1, entry2)

if __name__ == '__main__':
    register_gui()





