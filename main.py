# import tkinter as tk
# from tkinter import ttk, Label, Button
# from PIL import ImageTk, Image

# class AutomatedAttendanceSystem:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1500x790+0+0")
#         self.root.title('Automated Attendance System')
        
#         # Store references to prevent garbage collection
#         self.images = []

#         # Load and place images
#         self.add_image(r"C:\Users\anwis\OneDrive\Desktop\automated_attendance_system\assets\help.png", 0, 0, 500, 150)
#         self.add_image(r"C:\Users\anwis\OneDrive\Desktop\automated_attendance_system\assets\help.png", 500, 0, 500, 150)
#         self.add_image(r"C:\Users\anwis\OneDrive\Desktop\automated_attendance_system\assets\help.png", 1000, 0, 500, 150)

#         # Background image
#         bg_img = Image.open(r"C:\Users\anwis\OneDrive\Desktop\automated_attendance_system\assets\bg.jpg")
#         bg_img = bg_img.resize((1500, 670), Image.LANCZOS)
#         self.photoimg3 = ImageTk.PhotoImage(bg_img)
#         self.images.append(self.photoimg3)

#         bg_lbl = Label(self.root, image=self.photoimg3)
#         bg_lbl.place(x=0, y=130, width=1500, height=670)

#         # Title on top of the background image
#         title_lbl = Label(self.root, text="AUTOMATED ATTENDANCE SYSTEM", font=("times new roman", 40, "bold"), fg="white", bg="blue")
#         title_lbl.place(x=0, y=130, width=1500, height=50)

        # # Student Button and Label
        # self.add_button_with_label(
        #     img_path=r"C:\Users\anwis\OneDrive\Desktop\automated_attendance_system\assets\bg.jpg",
        #     x=100, y=200, width=225, height=225,
        #     text="Student Details", text_y_offset=15
        # )

        # Detector Button and Label
#         self.add_button_with_label(
#             img_path=r"C:\Users\anwis\OneDrive\Desktop\automated_attendance_system\assets\bg.jpg",
#             x=400, y=200, width=225, height=225,
#             text="Face Detector", text_y_offset=15
#         )

#     def add_image(self, path, x, y, width, height):
#         img = Image.open(path)
#         img = img.resize((width, height), Image.LANCZOS)
#         photoimg = ImageTk.PhotoImage(img)
#         self.images.append(photoimg)

#         p_lbl = Label(self.root, image=photoimg)
#         p_lbl.place(x=x, y=y, width=width, height=height)

#     def add_button_with_label(self, img_path, x, y, width, height, text, text_y_offset):
#         img = Image.open(img_path)
#         img = img.resize((width, height), Image.LANCZOS)
#         photoimg = ImageTk.PhotoImage(img)
#         self.images.append(photoimg)

#         button = Button(self.root, image=photoimg, cursor="hand2")
#         button.place(x=x, y=y, width=width, height=height)

#         label = Button(self.root, text=text, cursor="hand2", font=("times new roman", 20, "bold"), fg="white", bg="black")
#         label.place(x=x, y=y + height + text_y_offset, width=width, height=40)

# if __name__ == "__main__":
#     root = tk.Tk()
#     obj = AutomatedAttendanceSystem(root)
#     root.mainloop()
