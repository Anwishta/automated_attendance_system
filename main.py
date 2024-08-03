import tkinter as tk
from tkinter import ttk, Label
from PIL import ImageTk, Image

class AutomatedAttendanceSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title('Automated Attendance System')
        
        # Store references to prevent garbage collection
        self.images = []

        # Load and place images
        self.add_image(r"C:\Users\anwis\OneDrive\Desktop\automated_attendance_system\assets\help.png", 0, 0, 500, 150)
        self.add_image(r"C:\Users\anwis\OneDrive\Desktop\automated_attendance_system\assets\help.png", 500, 0, 500, 150)
        self.add_image(r"C:\Users\anwis\OneDrive\Desktop\automated_attendance_system\assets\help.png", 1000, 0, 500, 150)

        # Background image
        bg_img = Image.open(r"C:\Users\anwis\OneDrive\Desktop\automated_attendance_system\assets\bg.jpg")
        bg_img = bg_img.resize((1500, 670), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(bg_img)
        self.images.append(self.photoimg3)

        bg_lbl = Label(self.root, image=self.photoimg3)
        bg_lbl.place(x=0, y=130, width=1500, height=670)

        # Title on top of the background image
        title_lbl = Label(bg_lbl, text="AUTOMATED ATTENDANCE SYSTEM", font=("times new roman", 40, "bold"), fg="white", bg="blue")
        title_lbl.place(x=0, y=0, width=1500, height=50)

        # student
        bg_img4 = Image.open(r"C:\Users\anwis\OneDrive\Desktop\automated_attendance_system\assets\bg.jpg")
        bg_img4 = bg_img4.resize((250, 250), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(bg_img4)

        b1 = Button(bg_img, image=self.photoimg4, cursor = "hand")
        b1.place(x=200, y =100, width=250, height=250)

    def add_image(self, path, x, y, width, height):
        img = Image.open(path)
        img = img.resize((width, height), Image.LANCZOS)
        photoimg = ImageTk.PhotoImage(img)
        self.images.append(photoimg)

        p_lbl = Label(self.root, image=photoimg)
        p_lbl.place(x=x, y=y, width=width, height=height)

if __name__ == "__main__":
    root = tk.Tk()
    obj = AutomatedAttendanceSystem(root)
    root.mainloop()

