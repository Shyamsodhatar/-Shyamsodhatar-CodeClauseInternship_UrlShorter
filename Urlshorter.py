import tkinter
import customtkinter
import pyshorteners
from PIL import ImageTk,Image
from tkinter import messagebox

def short_url():
    url_entry=url.get()
    result=pyshorteners.Shortener().tinyurl.short(url_entry)
    entry_text_2.insert(0,result)
    
    messagebox.showinfo("Done!!","Url Shorted Successfully..")
def clear():
    entry_text_2.delete(0,tkinter.END)
    url.delete(0,tkinter.END)

    
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root=customtkinter.CTk()
root.geometry("800x800")
root.title("URl Shortner ")

img1=ImageTk.PhotoImage(Image.open('b.png'))
l1=customtkinter.CTkLabel(master=root,image=img1)
l1.pack()

frame=customtkinter.CTkFrame(master=l1,width=500,height=500,corner_radius=15)
frame.place(rely=0.5,relx=0.5,anchor=tkinter.CENTER)

l2=customtkinter.CTkLabel(master=frame,text="Generate Short URl",font=("italic bold",20),text_color="red")
l2.pack()
l2.place(x=150,y=50)

entry=customtkinter.CTkLabel(master=frame,text="Past your Url Here:",font=("times new roman bold",20))
entry.pack()
entry.place(x=30,y=150)

url=customtkinter.CTkEntry(master=frame,font=("arial",20),width=290)
url.pack()
url.place(x=200,y=150)

btn=customtkinter.CTkButton(master=frame,text="Generate Short Link",width=200,command=short_url)
btn.pack()
btn.place(x=200,y=250)


entry_2=customtkinter.CTkLabel(master=frame,text="Shorted URL Link:",font=("times new roman bold",20))
entry_2.pack()
entry_2.place(x=30,y=330)

entry_text_2=customtkinter.CTkEntry(master=frame,font=("arial",20),width=290)
entry_text_2.pack()
entry_text_2.place(x=200,y=330)

clear=customtkinter.CTkButton(master=frame,text="Clear",width=200 ,command=clear)
clear.pack()
clear.place(x=200,y=400)
root.mainloop()


