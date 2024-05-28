import tkinter as tk
import DroneFunctions

class MyGUI(tk.Tk):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (Tk)
        self.geometry("625x600")
        self.resizable(False,False)
        self.title("DroneHive")  # Set the title of the window
        self.MasterFrame = tk.Frame(self)
        self.buttonFrame1 = tk.Frame(self.MasterFrame)
        self.buttonFrame2 = tk.Frame(self.MasterFrame)

        self.Frame1 = tk.Frame(self.buttonFrame1)
        self.Frame2 = tk.Frame(self.buttonFrame2)
        self.LFrame1 = tk.LabelFrame(self.MasterFrame,text="drone info",width=100,height=80)

        self.button1 = tk.Button(self.Frame1, text="⇑", command=lambda: self.button_clicked(1), width=10, height=5)
        self.button2 = tk.Button(self.Frame1, text="↑", command=lambda: self.button_clicked(2), width=10, height=5)
        self.button3 = tk.Button(self.Frame1, text="⇓", command=lambda: self.button_clicked(3), width=10, height=5)
        self.button4 = tk.Button(self.Frame1, text="↻", command=lambda: self.button_clicked(4), width=10, height=5)
        self.button9 = tk.Button(self.Frame1, text="Show Data", command=lambda: self.button_clicked(5), width=10, height=5)

        self.button5 = tk.Button(self.Frame2, text="←", command=lambda: self.button_clicked(6), width=10, height=5)
        self.button6 = tk.Button(self.Frame2, text="↓", command=lambda: self.button_clicked(7), width=10, height=5)
        self.button7 = tk.Button(self.Frame2, text="→", command=lambda: self.button_clicked(8), width=10, height=5)
        self.button8 = tk.Button(self.Frame2, text="Video", command=lambda: self.button_clicked(9), width=10, height=5)
        self.button10 = tk.Button(self.Frame2, text="Exit", command=lambda: self.button_clicked(10), width=10,
                    height=5)
        self.label_data = tk.Label(self.LFrame1,width=30,height=10)
        self.label_data.pack()
        # must fix the pack to be horizontal and on two lines
        self.button1.pack(side=tk.LEFT)  # Pack the button into the window with some padding
        self.button2.pack(side=tk.LEFT)  # Pack the button into the window with some padding
        self.button3.pack(side=tk.LEFT)
        self.button4.pack(side=tk.LEFT)
        self.button5.pack(side=tk.LEFT)
        self.button6.pack(side=tk.LEFT)
        self.button7.pack(side=tk.LEFT)  # Pack the button into the window with some padding
        self.button8.pack(side=tk.LEFT)
        self.button9.pack(side=tk.LEFT)
        self.button10.pack(side=tk.LEFT)

        self.MasterFrame.pack(side=tk.BOTTOM)
        self.LFrame1.pack(side=tk.RIGHT)

        self.buttonFrame1.pack(side=tk.BOTTOM)
        self.buttonFrame2.pack(side=tk.BOTTOM)

        self.Frame1.pack(side=tk.LEFT)
        self.Frame2.pack(side=tk.LEFT)

    def button_clicked(self, index):  # fix the buttons
        if index == 1:
            DroneFunctions.SocketSending(DroneFunctions.MoveByKey('q'))
        if index == 2:
            DroneFunctions.SocketSending(DroneFunctions.MoveByKey('w'))
        if index == 3:
            DroneFunctions.SocketSending(DroneFunctions.MoveByKey('e'))
        if index == 4:
            DroneFunctions.SocketSending(DroneFunctions.MoveByKey('r'))
        if index == 5:
            DroneFunctions.SocketSending(DroneFunctions.MoveByKey('a'))
        if index == 6:
            DroneFunctions.SocketSending(DroneFunctions.MoveByKey('s'))
        if index == 7:
            DroneFunctions.SocketSending(DroneFunctions.MoveByKey('d'))
        if index == 8:
            DroneFunctions.SocketSending(DroneFunctions.MoveByKey('e'))
        if index == 9:#data show
            DroneFunctions.SocketSending(DroneFunctions.MoveByKey('z'))
        if index == 10:
            DroneFunctions.sock.close()
            self.destroy()

    def update_data_label(self, data):
        self.label_data.config(text=data)
    def mainloop(self, n: int = ...):
        DroneFunctions.CallVideoThread()
        while DroneFunctions.isRunning:
            self.update_idletasks()
            self.update()


app = MyGUI()

DroneFunctions.gui_instance = app

