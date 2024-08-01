import tkinter as tk
from tkinter import ttk, Label
from PIL import ImageTk, Image

class Automated_attendance_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title('Automated Attendance System')
        
        # Load and resize image
        img = Image.open(r"C:\Users\anwis\OneDrive\Desktop\automated_attendance_system\assets\help.png")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # Create and place label with image
        p_lbl = Label(self.root, image=self.photoimg)
        p_lbl.place(x=0, y=0, width=500, height=150)

if __name__=="__main__":
    root = tk.Tk()
    obj = Automated_attendance_system(root)
    root.mainloop()
