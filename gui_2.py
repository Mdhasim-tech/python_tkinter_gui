from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.geometry("700x600")
label1=Label(text="This is a label")
label1.pack()
#adding a picture to the gui for png images
#photo=PhotoImage(file="1.png")
#adding a picture to the gui for jpg images
image=Image.open("1.jpg")
photo=ImageTk.PhotoImage(image)
label2=Label(image=photo)
label2.pack()
root.mainloop()

