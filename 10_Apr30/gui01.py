import tkinter as tk
import tkinter.messagebox

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

        start_btn = tk.Button(root, text = "Старт",
                                command = self.start_onlick
                                )
        start_btn.place(x=60,y=140,width=111,height=54)

        GLabel_119=tk.Label(root, text = "Кількість секунд")
        GLabel_119.place(x=30,y=50,width=70,height=25)

        stop_btn=tk.Button(root, text = "Стоп",
                           command = self.stop_onclick)
        stop_btn.place(x=280,y=160,width=70,height=25)

        self.s = tk.StringVar()
        GLineEdit_759 = tk.Entry(root, textvariable=self.s)
        GLineEdit_759.place(x=170,y=50,width=70,height=25)
        self.s.set("5")
        #
        self.is_active = False

    def on_timer(self):
        if not self.is_active:
            ans = tk.messagebox.askquestion(title="питання",
                                           message="Точно зупинити відлік часу???",
                                           type=tkinter.messagebox.YESNO)
            #print(ans)
            if ans == 'yes':
                return
            else:
                self.is_active = True
        #

        old_text = self.s.get()
        old_value = int(old_text)
        if old_value == 0:
            tk.messagebox.showwarning(title="ура", message="таймер готовий")
            return # перериваємо виконання методу
        #

        new_s = str(old_value-1)
        self.s.set(new_s)
        root.after(1000, self.on_timer) # плануємо виклик цього ж метода в майбутньому через 1 с

    def start_onlick(self):
        #print("AAAAA")
        #self.s.set("HELLO!!!!!")
        self.is_active = True
        root.after(1000, self.on_timer)


    def stop_onclick(self):
        self.is_active = False
        #ans = tk.messagebox.askquestion(title="питання",
        #                                message="Значення:" + self.s.get(),
        #                                type=tkinter.messagebox.YESNO)
        #print(ans)



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
