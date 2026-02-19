from tkinter import *
import tkinter as tk
from tkinter import messagebox
import webbrowser
import secrets, string, sys, os
import customtkinter as ctk
from pathlib import Path
import platformdirs
from PIL import Image


window = tk.Tk()
window.geometry("420x420")
window.title("Password-Generator")
window.config(background="#a6d485")
window.resizable(False, False)



def path(rel_path):
    
    try:
        pathh = sys._MEIPASS
    except Exception:
        pathh = os.path.abspath(".")
    return os.path.join(pathh, rel_path)



icon2 = ctk.CTkImage(
    light_image=Image.open(path("Tkinter-Password-Generator-projekt/save.png")),
    dark_image=Image.open(path("Tkinter-Password-Generator-projekt/save.png")),
    size=(18, 18)
)

icon3 = ctk.CTkImage(
    light_image=Image.open(path("Tkinter-Password-Generator-projekt/open.png")),
    dark_image=Image.open(path("Tkinter-Password-Generator-projekt/open.png")),
    size=(18, 18)
)



def extt():
    window.destroy()

ext = ctk.CTkButton(master=window, 
                    text="exit",
                    command=extt,  
                    corner_radius=10, 
                    border_width=2,
                    width=3,
                    font=("Tienne", 13, "bold"),
                    fg_color="#a6d485",       
                    text_color="#2e3b3a",      
                    hover_color="#6b944d")     

ext.place(x=360, y=380)



label = ctk.CTkLabel(window,
                     text="Welcome to Password Generator",
                     font=("Arial", 14, "bold"),
                     fg_color="transparent", 
                     padx=20,
                     pady=10
                     )
label.pack()



def generate():
    symbols = string.ascii_letters + string.digits + "!@W#$j%^&*"
    passwort = ''.join(secrets.choice(symbols) for _ in range(12))
    resultat_label.config(text=passwort)

resultat_label = Label(window, text="", font=("Tienne", 14, "bold"))
resultat_label.pack(pady=10)
resultat_label.config(bg="#a6d485")


button = ctk.CTkButton(master=window, text="-Generate-", command=generate, font=("Tienne", 15, "bold"),
              corner_radius=10,
              width=70,
              height=30,
              border_width=2,
              fg_color="#a6d485",       
              text_color="#2e3b3a",      
              hover_color="#6b944d",)
button.place(relx=0.5, rely=0.3, anchor="center")



def copy():
    passwort = resultat_label.cget("text")
    if passwort:
        window.clipboard_clear()
        window.clipboard_append(passwort)
        window.update()

button_copy = ctk.CTkButton(master=window, text="-Copy-", command=copy, font=("Tienne", 15, "bold"),
              fg_color="#a6d485",       
              text_color="#2e3b3a",      
              hover_color="#6b944d",
              corner_radius=10,
              height=30,
              width=70,
              border_width=2,)
button_copy.place(relx=0.5, rely=0.4, anchor="center")



def save():
    password = resultat_label.cget("text")
    if not password:
        messagebox.showwarning(title="Warning", message="First, generate a password.")
    else:
        desktop = platformdirs.user_desktop_dir()
        if not desktop:
            messagebox.showerror(title="Error", message="There was an error finding the desktop.")
        else:
            file_path = Path(desktop) / "Password_.txt"
            with open(file_path, "a", encoding="utf-8") as file:
                file.write(password + "\n")
        

button_save = ctk.CTkButton(master=window,
                     text="",
                     image=icon2, 
                     command=save,
                     corner_radius=100,
                     height=25,
                     width=5,
                     border_width=2,
                     fg_color="#a6d485",       
                     text_color="#2e3b3a",      
                     hover_color="#6b944d",)
button_save.place(x=10, y=380)


def webb():
    web = webbrowser.open("https://github.com/niwobyte")  


button_website = ctk.CTkButton(master=window,
                               text="",
                               command=webb,
                               image=icon3,
                               corner_radius=100,
                               height=25,
                               width=5,
                               border_width=2,
                               fg_color="#a6d485",
                               text_color="#2e3b3a",
                               hover_color="#6b944d")
button_website.place(x=60, y=380)



window.mainloop()