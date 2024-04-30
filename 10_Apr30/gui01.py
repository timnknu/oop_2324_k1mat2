import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=379
        height=220
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_353=tk.Button(root)
        GButton_353["text"] = "Старт"
        GButton_353.place(x=60,y=140,width=111,height=54)
        GButton_353["command"] = self.GButton_353_command

        GLabel_119=tk.Label(root)
        GLabel_119["text"] = "Кількість секунд"
        GLabel_119.place(x=30,y=50,width=70,height=25)

        GButton_925=tk.Button(root)
        GButton_925["text"] = "Стоп"
        GButton_925.place(x=280,y=160,width=70,height=25)
        GButton_925["command"] = self.GButton_925_command

        GLineEdit_759=tk.Entry(root)
        GLineEdit_759["borderwidth"] = "1px"
        GLineEdit_759["text"] = "Entry"
        GLineEdit_759.place(x=170,y=50,width=70,height=25)

    def GButton_353_command(self):
        print("command")


    def GButton_925_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
