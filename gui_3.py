from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry("700x600")
'''photo=PhotoImage(file="2.png")
label=Label(image=photo)
label.pack()'''

img=Image.open("hasim pic.jpg")
photo=ImageTk.PhotoImage(img)
label=Label(image=photo)
label.pack()
root.mainloop()