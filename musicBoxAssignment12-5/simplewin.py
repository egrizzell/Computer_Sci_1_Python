import tkinter

class simplewin:
    def __init__(self):
        self.root = tkinter.Tk()

    def add_label(self, text):
        tkinter.Label(self.root, text=text).pack()

    def add_button(self, text, onclick):
        tkinter.Button(self.root, text=text, command=onclick).pack()

    def add_key_handler(self, callback):
        self.root.bind('<Key>', callback)

    def run(self):
        self.root.mainloop()

    def quit(self):
        self.root.destroy()
        
