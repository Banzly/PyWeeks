# # import tkinter as tk
# # from PIL import ImageTk, Image
# # from tkinter import ttk
# # import threading
# # import os
# # import sys
# # import subprocess


# # # Rest of the code remains the same...

# # # Create the Tkinter window
# # window = tk.Tk()
# # window.title("Ban'Z App")
# # window.geometry("600x400")

# # # Load the background image
# # background_image = ImageTk.PhotoImage(Image.open(r""))
# # background_label = tk.Label(window, image=background_image)
# # background_label.place(x=0, y=0, relwidth=1, relheight=1)

# # # Create the title label
# # title_label = ttk.Label(window, text="Ban'Z System", font=("Arial", 16), style="Title.TLabel")
# # title_label.pack(pady=50, anchor='n')

# # # Function to start the Gesture Controller when the "Start" button is clicked
# # def start_button_click():
# #     thread = threading.Thread(target=start_virtual_mouse)
# #     thread.start()

# # # Execute the Python script after the thread starts
# # subprocess.Popen([sys.executable, "-i", "D:\\SKRIPSI\\Virual-Mouse\\src\\Virtual_Mouse.py"])

# # # Create the "Start" button
# # style = ttk.Style()
# # style.configure("TButton", font=("Arial", 12), relief="raised", background="#f0f0f0", foreground="#333333")
# # start_button = ttk.Button(window, text="Start", command=start_button_click, style="TButton")
# # start_button.pack(pady=20)

# # # Function to exit the application when the "Exit" button is clicked
# # def exit_button_click():
# #     window.destroy()

# # # Create the "Exit" button
# # exit_button = ttk.Button(window, text="Exit", command=exit_button_click, style="TButton")
# # exit_button.pack(pady=10, anchor='s')

# # # Run the Tkinter main loop
# # window.mainloop()

# import tkinter as tk
# from PIL import ImageTk, Image
# from tkinter import ttk
# import os
# import sys

# # Create the Tkinter window
# window = tk.Tk()
# window.title("Ban'Z App")
# window.geometry("600x400")

# # Load the background image
# background_image = ImageTk.PhotoImage(Image.open(r""))
# background_label = tk.Label(window, image=background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)

# # Create the title label
# title_label = ttk.Label(window, text="Ban'Z System", font=("Arial", 16), style="Title.TLabel")
# title_label.pack(pady=50, anchor='n')

# # Function to start the Virtual Mouse script when the "Start" button is clicked
# def start_button_click():
#     script_path = r"D:\\SKRIPSI\\Virual-Mouse\\src\\Virtual_Mouse.py"
#     os.system(f"{sys.executable} {script_path}")

# # Create the "Start" button
# style = ttk.Style()
# style.configure("TButton", font=("Arial", 12), relief="raised", background="#f0f0f0", foreground="#333333")
# start_button = ttk.Button(window, text="Start", command=start_button_click, style="TButton")
# start_button.pack(pady=20)

# # Function to exit the application when the "Exit" button is clicked
# def exit_button_click():
#     window.destroy()

# # Create the "Exit" button
# exit_button = ttk.Button(window, text="Exit", command=exit_button_click, style="TButton")
# exit_button.pack(pady=10, anchor='s')

# # Run the Tkinter main loop
# window.mainloop()


# import tkinter
# import customtkinter
# from PIL import ImageTk,Image

# customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
# customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


# app = customtkinter.CTk()  #creating cutstom tkinter window
# app.geometry("600x440")
# app.title('BanZ System')



# def button_function():
#     app.destroy()            # destroy current window and creating new one 
#     w = customtkinter.CTk()  
#     w.geometry("1280x720")
#     w.title('Welcome')
#     l1=customtkinter.CTkLabel(master=w, text="Home Page",font=('Century Gothic',60))
#     l1.place(relx=0.5, rely=0.5,  anchor=tkinter.CENTER)
#     w.mainloop()
    


# img1=ImageTk.PhotoImage(Image.open(r""))
# l1=customtkinter.CTkLabel(master=app,image=img1)
# l1.pack()

# #creating custom frame
# frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
# frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# l2=customtkinter.CTkLabel(master=frame, text="BanZPedia Application",font=('Century Gothic',20))
# l2.place(x=50, y=45)


# #Create custom button
# button1 = customtkinter.CTkButton(master=frame, width=220, text="Start", command=button_function, corner_radius=6)
# button1.place(x=50, y=110)



# # You can easily integrate authentication system 

# app.mainloop()

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

img1 = ImageTk.PhotoImage(Image.open(r"D:\SKRIPSI\Virual-Mouse\BG_GUI\pattern.png"))
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
