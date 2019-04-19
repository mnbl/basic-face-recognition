import sys

user = 'nil'

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

def welcome_gui(user1):
    '''Starting point when module is the main routine.'''
    global val, w, root, user
    user= user1
    root = tk.Tk()
    top = welcomePage (root)
    root.mainloop()

w = None
def create_welcomePage(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = welcomePage (w)
    return (w, top)

def destroy_welcomePage():
    global w
    w.destroy()
    w = None

class welcomePage:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("337x376+640+143")
        top.title("Welcome")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.148, rely=0.16, relheight=0.631
                , relwidth=0.745)
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(width=251)

        self.msg = tk.Message(self.Canvas1)
        self.msg.place(relx=0.239, rely=0.29, relheight=0.27, relwidth=0.526)
        self.msg.configure(text='Welcome '+ user)
        self.msg.configure(width=132)

        self.exit = tk.Button(top)
        self.exit.place(relx=0.4, rely=0.817, height=31, width=101)
        self.exit.configure(command= self.exitwindow)
        self.exit.configure(text='''Exit''')
        self.exit.configure(width=101)

    def exitwindow(self):
        sys.exit()

if __name__ == '__main__':
    welcome_gui(user)





