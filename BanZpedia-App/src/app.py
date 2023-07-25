import tkinter
import customtkinter
from PIL import ImageTk, Image
import subprocess
import sys

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("600x440")
app.title('BanZ System')

def start_function():
    app.destroy()

    # Add the code to run the script path using subprocess
    script_path = r""
    subprocess.Popen([sys.executable, script_path])

def exit_function():
    app.quit()

img1 = ImageTk.PhotoImage(Image.open(r""))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2 = customtkinter.CTkLabel(master=frame, text="BanZPedia Application", font=('Century Gothic', 20))
l2.place(x=50, y=45)

button1 = customtkinter.CTkButton(master=frame, width=220, text="Start", command=start_function, corner_radius=6)
button1.place(x=50, y=110)

button2 = customtkinter.CTkButton(master=frame, width=220, text="Exit", command=exit_function, corner_radius=6)
button2.place(x=50, y=165)

app.mainloop()
