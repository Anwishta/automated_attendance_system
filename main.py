import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

class Automated_attendance_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title('Automated Attendance System')

if __name__=="__main__":
    root= tk.Tk()
    obj = Automated_attendance_system(root)
    root.mainloop()

