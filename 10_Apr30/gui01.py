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

        GButton_353 = tk.Button(root, text = "Старт",
                                command = self.GButton_353_command
                                )
        GButton_353.place(x=60,y=140,width=111,height=54)

        GLabel_119=tk.Label(root, text = "Кількість секунд")
        GLabel_119.place(x=30,y=50,width=70,height=25)

        GButton_925=tk.Button(root, text = "Стоп",
                              command = self.GButton_925_command)
        GButton_925.place(x=280,y=160,width=70,height=25)

        GLineEdit_759=tk.Entry(root)
        GLineEdit_759.place(x=170,y=50,width=70,height=25)

    def GButton_353_command(self):
        print("AAAAA")


    def GButton_925_command(self):
        print("bbbb")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
